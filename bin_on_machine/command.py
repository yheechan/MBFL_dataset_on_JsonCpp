#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os
import sys
import time

script_file_path = Path(os.path.realpath(__file__))
bin_dir = script_file_path.parent
main_dir = bin_dir.parent

build_jsoncpp = bin_dir / '0_build_jsoncpp.py'
extract_line2function = bin_dir / '1_extract_line2function.py'
run_testcases = bin_dir / '2_run_testcases.py'
postprocess_cov = bin_dir / '3_postprocess_cov.py'

def build_jsoncpp_exec(core_id):
    # 0. build jsoncpp
    cmd = [build_jsoncpp, core_id]
    begin_time = time.time()
    print('0. start build jsoncpp')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{} {:.2f} secs] - Failed build jsoncpp: {}'.format(core_id, curr_time - begin_time, res))
        sys.exit(1)
    
    curr_time = time.time()
    print('[{} {:.2f} secs] - Success build jsoncpp: {}'.format(core_id, curr_time - begin_time, res))

def extract_line2function_exec(core_id):
    # 1. extract line2function
    cmd = [extract_line2function, core_id]
    begin_time = time.time()
    print('1. start extract line2function')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{} {:.2f} secs] - Failed extract line2function: {}'.format(core_id, curr_time - begin_time, res))
        sys.exit(1)
    
    curr_time = time.time()
    print('[{} {:.2f} secs] - Success extract line2function: {}'.format(core_id, curr_time - begin_time, res))

def run_testcases_exec(core_id):
    # 2. run testcases
    cmd = [run_testcases, core_id, 'gen_cov']
    begin_time = time.time()
    print('2. start run testcases')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{} {:.2f} secs] - Failed run testcases: {}'.format(core_id, curr_time - begin_time, res))
        sys.exit(1)
    
    curr_time = time.time()
    print('[{} {:.2f} secs] - Success run testcases: {}'.format(core_id, curr_time - begin_time, res))

def postprocess_cov_exec(core_id):
    # 3. postprocess coverage
    cmd = [postprocess_cov, core_id]
    begin_time = time.time()
    print('3. start postprocess coverage')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{} {:.2f} secs] - Failed postprocess coverage: {}'.format(core_id, curr_time - begin_time, res))
        sys.exit(1)
    
    curr_time = time.time()
    print('[{} {:.2f} secs] - Success postprocess coverage: {}'.format(core_id, curr_time - begin_time, res))

if __name__ == "__main__":
    core_id = sys.argv[1]

    start_time = time.time()

    build_jsoncpp_exec(core_id)
    extract_line2function_exec(core_id)
    run_testcases_exec(core_id)
    postprocess_cov_exec(core_id)

    end_time = time.time()
    print('Total time: {:.2f} secs'.format(end_time - start_time))