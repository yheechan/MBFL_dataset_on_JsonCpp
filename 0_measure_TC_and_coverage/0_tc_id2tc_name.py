#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent

if __name__ == "__main__":
    jsoncpp_test = main_dir / 'jsoncpp_template/build/src/test_lib_json/jsoncpp_test'
    cmd = [jsoncpp_test, '--list-tests']
    process = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, encoding='utf-8')
    
    tcid2tcname_txt = main_dir / 'data_in_need/tcid2tcname.csv'
    tcid2tcname_fp = open(tcid2tcname_txt, 'w')
    tcid2tcname_fp.write('tc_id,tc_name\n')
    
    tc_cnt = 1
    while True:
        line = process.stdout.readline()
        if line == '' and process.poll() is not None:
            break
        line = line.strip()
        if line == '':
            continue
        
        tcid2tcname_fp.write('TC{},{}\n'.format(tc_cnt, line))
        tc_cnt += 1