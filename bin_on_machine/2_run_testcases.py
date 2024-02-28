#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import sys

script_path = Path(os.path.realpath(__file__))
bin_dir = script_path.parent
main_dir = bin_dir.parent

gcovr = Path('/home/yangheechan/.local/bin/gcovr')
clangPP = Path('/usr/bin/clang++-13')

def get_tc_dict(jsoncpp_test):
    cmd = [jsoncpp_test, '--list-tests']
    process = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.STDOUT, encoding='utf-8')

    tc_cnt = 1
    tc_dict = {}
    while True:
            line = process.stdout.readline()
            if line == '' and process.poll() is not None:
                break
            line = line.strip()
            if line == '':
                continue
            tc_id = 'TC{}'.format(tc_cnt)
            tc_dict[tc_id] = line
            tc_cnt += 1
    return tc_dict

def reset_gcda(jsoncpp_dir):
    project_path = jsoncpp_dir
    cmd = [
        'find', '.', '-type',
        'f', '-name', '*.gcda',
        '-delete'
    ]
    res = sp.call(cmd, cwd=project_path)

def gen_cov_json(core_dir, jsoncpp_dir, tc_id):
    data_dir = core_dir / 'data'
    if not data_dir.exists():
        data_dir.mkdir()
    coverage_dir = data_dir / 'coverage_data'
    if not coverage_dir.exists():
        coverage_dir.mkdir()
    cov_per_tc_dir = coverage_dir / 'coverage_per_tc'
    if not cov_per_tc_dir.exists():
        cov_per_tc_dir.mkdir()
    
    cov_file_name = tc_id + '.cov.json'
    cov_file_path = cov_per_tc_dir / cov_file_name
    cmd = [
        gcovr,
        '--gcov-executable', 'llvm-cov gcov',
        '--json-pretty', '-o', cov_file_path
    ]
    res = sp.call(cmd, cwd=jsoncpp_dir)
    return cov_file_path

def gen_cov_summary_json(core_dir, jsoncpp_dir, tc_id):
    data_dir = core_dir / 'data'
    if not data_dir.exists():
        data_dir.mkdir()
    coverage_dir = data_dir / 'coverage_data'
    if not coverage_dir.exists():
        coverage_dir.mkdir()
    cov_summary_dir = coverage_dir / 'coverage_summary_per_tc'
    if not cov_summary_dir.exists():
        cov_summary_dir.mkdir()
    
    cov_summary_file_name = tc_id + '.cov.summary.json'
    cov_summary_file_path = cov_summary_dir / cov_summary_file_name
    cmd = [
        gcovr,
        '--gcov-executable', 'llvm-cov gcov',
        '--json-summary-pretty', '-o', cov_summary_file_path
    ]
    res = sp.call(cmd, cwd=jsoncpp_dir)
    return cov_summary_file_path

def run_tc(core_dir, jsoncpp_test, tc_dict, jsoncpp_dir, gen_cov=False):
    failing_tc_dict = {}
    passing_tc_dict = {}

    for tc_id, tc_name in tc_dict.items():
        # reset gcda files before any TC runs
        reset_gcda(jsoncpp_dir)

        # run single TC
        cmd = ['timeout', '2s', jsoncpp_test, '--test', tc_name]
        res = sp.call(cmd, stdout=sp.PIPE, stderr=sp.STDOUT, encoding='utf-8')
        if res != 0:
            failing_tc_dict[tc_id] = tc_name
            print('test failed: {} {}'.format(tc_id, tc_name))
        else:
            passing_tc_dict[tc_id] = tc_name
            print('test passed: {} {}'.format(tc_id, tc_name))

        # measure coverage using gcovr
        if gen_cov:
            cov_path = gen_cov_json(core_dir, jsoncpp_dir, tc_id)
            cov_summ_path = gen_cov_summary_json(core_dir, jsoncpp_dir, tc_id)
    
    # reset gcda files after all TC runs
    reset_gcda(jsoncpp_dir)
    
    return failing_tc_dict, passing_tc_dict

def rebuild_jsoncpp(build_dir):
    cmd = ['rm', '-rf', str(build_dir)]
    res = sp.run(cmd)
    if res.returncode != 0:
        print('Error: {}'.format(res))
        return
    
    build_dir.mkdir()

    cmd = [
        'cmake',
        '-DCMAKE_EXPORT_COMPILE_COMMANDS=ON',
        '-DCMAKE_CXX_COMPILER={}'.format(clangPP),
        # '-DCMAKE_CXX_FLAGS=-O0 -fprofile-arcs -ftest-coverage -g -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION --save-temps',
        '-DCMAKE_CXX_FLAGS=-O0 -fprofile-arcs -ftest-coverage -g -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION',
        # '-DCMAKE_CXX_FLAGS=-DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION',
        '-DBUILD_SHARED_LIBS=OFF', '-G',
        'Unix Makefiles',
        '../'
    ]
  
    res = sp.call(cmd, cwd=build_dir)
    if res != 0:
        print('cmake failed: {}'.format(res))
        exit(1)
    
    cmd = ['make', '-j20']
    res = sp.call(cmd, cwd=build_dir)
    if res != 0:
        print('make failed: {}'.format(res))
        exit(1)

    return

def write_tc_info(core_dir, tc_dict, tc_type):
    data_dir = core_dir / 'data'
    if not data_dir.exists():
        data_dir.mkdir()
    tc_dir = data_dir / 'testcase_info'
    if not tc_dir.exists():
        tc_dir.mkdir()
    
    tc_file_name = '{}.csv'.format(tc_type)
    tc_file_path = tc_dir / tc_file_name
    tc_file_fp = open(tc_file_path, 'w')
    tc_file_fp.write('tc_id,tc_name\n')
    for tc_id, tc_name in tc_dict.items():
        tc_file_fp.write('{},{}\n'.format(tc_id, tc_name))
    tc_file_fp.close()
    return

if __name__ == "__main__":
    core_id = sys.argv[1]
    gen_cov = True if sys.argv[2] == 'gen_cov' else False
    core_dir = main_dir / core_id
    jsoncpp_dir = core_dir / 'jsoncpp_template'
    build_dir = jsoncpp_dir / 'build'
    jsoncpp_test = build_dir / 'src/test_lib_json/jsoncpp_test'

    rebuild_jsoncpp(build_dir)

    tc_dict = get_tc_dict(jsoncpp_test)
    failing_tc_dict, passing_tc_dict = run_tc(
        core_dir, jsoncpp_test, tc_dict, jsoncpp_dir, gen_cov=gen_cov)

    print('{} fails + {} pass = {} total'.format(
        len(failing_tc_dict), len(passing_tc_dict),
        len(failing_tc_dict)+len(passing_tc_dict))
    )

    write_tc_info(core_dir, failing_tc_dict, 'failing_testcases')
    write_tc_info(core_dir, passing_tc_dict, 'passing_testcases')
    