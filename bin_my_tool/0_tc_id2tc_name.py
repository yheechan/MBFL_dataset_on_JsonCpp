#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os
import time

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent

if __name__ == "__main__":
    begin_time = time.time()

    # make build dir
    jsoncpp_dir = main_dir / 'jsoncpp_template'
    build_dir = jsoncpp_dir / 'build'
    if not build_dir.exists():
        build_dir.mkdir()
    if build_dir.exists():
        cmd = ['rm', '-rf', build_dir]
        sp.call(cmd, cwd=main_dir)
        print('>> removed directory: {}'.format(build_dir))
        build_dir.mkdir()
    
    # build jsoncpp
    cmd = [
        'cmake',
        '-DCMAKE_EXPORT_COMPILE_COMMANDS=ON',
        '-DCMAKE_CXX_COMPILER=/usr/bin/clang++-13',
        '-DCMAKE_CXX_FLAGS=-O0 -fprofile-arcs -ftest-coverage -g -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION --save-temps',
        '-DBUILD_SHARED_LIBS=OFF', '-G',
        'Unix Makefiles',
        '../'
    ]
    res = sp.call(cmd, cwd=build_dir)
    if res != 0:
        print('cmake failed: {}'.format(res))
        exit(1)

    # make jsoncpp
    cmd = ['make', '-j20']
    res = sp.call(cmd, cwd=build_dir)
    if res != 0:
        print('make failed: {}'.format(res))
        exit(1)
    
    end_time = time.time()
    print('>> elapsed time for compilation: {}s'.format(end_time - begin_time))



    jsoncpp_test = main_dir / 'jsoncpp_template/build/src/test_lib_json/jsoncpp_test'
    cmd = [jsoncpp_test, '--list-tests']
    process = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, encoding='utf-8')
    
    tcid2tcname_txt = main_dir / 'data_in_need/tcid2tcname.csv'
    tcid2tcname_fp = open(tcid2tcname_txt, 'w')
    tcid2tcname_fp.write('tc_id,tc_name\n')
    
    tc_dict = {}
    tc_cnt = 1
    while True:
        line = process.stdout.readline()
        if line == '' and process.poll() is not None:
            break
        line = line.strip()
        if line == '':
            continue
        
        tcid2tcname_fp.write('TC{},{}\n'.format(tc_cnt, line))
        tc_dict['TC{}'.format(tc_cnt)] = line
        tc_cnt += 1

    tcid2tcname_fp.close()    

    # run testcases
    begin_time = time.time()
    for tc_id in tc_dict:
        cmd = [jsoncpp_test, '--test', tc_dict[tc_id]]
        res = sp.call(cmd)
        if res != 0:
            print('test {} failed: {}'.format(tc_id, res))
            exit(1)
        else:
            print('test {} passed: {}'.format(tc_id, res))
    
    end_time = time.time()
    print('>> elapsed time for running testcases: {}s'.format(end_time - begin_time))
