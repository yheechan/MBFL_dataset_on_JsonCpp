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

if __name__ == "__main__":
    core_id = sys.argv[1]
    
    start_time = time.time()

    # 0. build jsoncpp
    cmd = [build_jsoncpp, core_id]
    curr_time = time.time()
    print('[{} {}] - start build jsoncpp'.format(core_id, curr_time - start_time))
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    
    if res != 0:
        curr_time = time.time()
        print('[{} {}] - Failed build jsoncpp: {}'.format(core_id, curr_time - start_time, res))
        sys.exit(1)
        
    curr_time = time.time()
    print('[{} {}]- Success build jsoncpp: {}'.format(core_id, curr_time - start_time, res))
    
    
    # 1. extract line2function
    cmd = [extract_line2function, core_id]
    curr_time = time.time()
    print('[{} {}] - start extract line2function'.format(core_id, curr_time - start_time))
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    
    if res != 0:
        curr_time = time.time()
        print('[{} {}] - Failed extract line2function: {}'.format(core_id, curr_time - start_time, res))
        sys.exit(1)
        
    curr_time = time.time()
    print('[{} {}] - Success extract line2function: {}'.format(core_id, curr_time - start_time, res))
    
    
    # 2. run testcases
    cmd = [run_testcases, core_id, 'gen_cov']
    curr_time = time.time()
    print('[{} {}] - start run testcases'.format(core_id, curr_time - start_time))
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    
    if res != 0:
        curr_time = time.time()
        print('[{} {}] - Failed run testcases: {}'.format(core_id, curr_time - start_time, res))
        sys.exit(1)
    
    curr_time = time.time()
    print('[{} {}] - Success run testcases: {}'.format(core_id, curr_time - start_time, res))
    
    
    # 3. postprocess coverage
    cmd = [postprocess_cov, core_id]
    curr_time = time.time()
    print('[{} {}] - start postprocess coverage'.format(core_id, curr_time - start_time))
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    
    if res != 0:
        curr_time = time.time()
        print('[{} {}] - Failed postprocess coverage: {}'.format(core_id, curr_time - start_time, res))
        sys.exit(1)
        
    curr_time = time.time()
    print('[{} {}] - Success postprocess coverage: {}'.format(core_id, curr_time - start_time, res))
    
    curr_time = time.time()
    print('[{} {}] - Done'.format(core_id, curr_time - start_time))
