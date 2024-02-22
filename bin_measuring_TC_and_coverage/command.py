#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os
import sys
import time

script_file_path = Path(os.path.realpath(__file__))
bin_dir = script_file_path.parent
main_dir = bin_dir.parent

map_bug2id = bin_dir / '0_map_bug2id.py'
make_template = bin_dir / '1_make_template.py'
reset_mbfl_py = bin_dir / '2_reset_mbfl.py'
reset_mbfl_sh = bin_dir / '2_reset_mbfl.sh'
send_template_py = bin_dir / '3_send_template.py'
send_template_sh = bin_dir / '3_send_template.sh'
distribute_bug_versions_py = bin_dir / '4_distribute_bug_versions.py'
distribute_bug_versions_sh = bin_dir / '4_distribute_bug_versions.sh'
prepare_bin = bin_dir / '5_prepare_bin.py'
send_bin_py = bin_dir / '6_send_bin.py'
send_bin_sh = bin_dir / '6_send_bin.sh'
run_command_py = bin_dir / '7_run_command.py'
run_command_sh = bin_dir / '7_run_command.sh'
retreive_data_py = bin_dir / '8_retrieve_data.py'
retreive_data_sh = bin_dir / '8_retrieve_data.sh'

def map_bug2id_exec():
    # 0. map bug2id
    cmd = [map_bug2id]
    begin_time = time.time()
    print('0. start map bug2id')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed map bug2id: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success map bug2id: {}'.format(curr_time - begin_time, res))

def make_template_exec():
    # 1. make template
    cmd = [make_template]
    begin_time = time.time()
    print('1. start make template')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed make template: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success make template: {}'.format(curr_time - begin_time, res))

def reset_mbfl_exec():
    # 2. reset mbfl.py
    cmd = [reset_mbfl_py]
    begin_time = time.time()
    print('2. start reset mbfl.py')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed reset mbfl.py: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success reset mbfl.py: {}'.format(curr_time - begin_time, res))

    
    cmd = ['bash', reset_mbfl_sh]
    begin_time = time.time()
    print('2. start reset mbfl.sh')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed reset mbfl.sh: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success reset mbfl.sh: {}'.format(curr_time - begin_time, res))

def send_template_exec():
    # 3. send template
    cmd = [send_template_py]
    begin_time = time.time()
    print('3. start send template.py')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed send template.py: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success send template.py: {}'.format(curr_time - begin_time, res))

    cmd = ['bash', send_template_sh]
    begin_time = time.time()
    print('3. start send template.sh')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed send template.sh: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success send template.sh: {}'.format(curr_time - begin_time, res))

def distribute_bug_versions_exec():
    # 4. distribute bug versions
    cmd = [distribute_bug_versions_py]
    begin_time = time.time()
    print('4. start distribute bug versions.py')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed distribute bug versions.py: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success distribute bug versions.py: {}'.format(curr_time - begin_time, res))

    cmd = ['bash', distribute_bug_versions_sh]
    begin_time = time.time()
    print('4. start distribute bug versions.sh')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed distribute bug versions.sh: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success distribute bug versions.sh: {}'.format(curr_time - begin_time, res))

def prepare_bin_exec():
    # 5. prepare bin
    cmd = [prepare_bin]
    begin_time = time.time()
    print('5. start prepare bin')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed prepare bin: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success prepare bin: {}'.format(curr_time - begin_time, res))

def send_bin_exec():
    # 6. send bin
    cmd = [send_bin_py]
    begin_time = time.time()
    print('6. start send bin.py')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed send bin.py: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success send bin.py: {}'.format(curr_time - begin_time, res))

    cmd = ['bash', send_bin_sh]
    begin_time = time.time()
    print('6. start send bin.sh')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed send bin.sh: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success send bin.sh: {}'.format(curr_time - begin_time, res))

def run_command_exec():
    # 7. run command
    cmd = [run_command_py]
    begin_time = time.time()
    print('7. start run command.py')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed run command.py: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success run command.py: {}'.format(curr_time - begin_time, res))

    cmd = ['bash', run_command_sh]
    begin_time = time.time()
    print('7. start run command.sh')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed run command.sh: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success run command.sh: {}'.format(curr_time - begin_time, res))

def retreive_data_exec():
    # 8. retreive data
    cmd = [retreive_data_py]
    begin_time = time.time()
    print('8. start retreive data.py')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed retreive data.py: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success retreive data.py: {}'.format(curr_time - begin_time, res))

    cmd = ['bash', retreive_data_sh]
    begin_time = time.time()
    print('8. start retreive data.sh')
    res = sp.call(cmd, cwd=bin_dir, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    if res != 0:
        curr_time = time.time()
        print('[{:.2f} secs] - Failed retreive data.sh: {}'.format(curr_time - begin_time, res))
        sys.exit(1)

    curr_time = time.time()
    print('[{:.2f} secs] - Success retreive data.sh: {}'.format(curr_time - begin_time, res))

if __name__ == "__main__":
    
    start_time = time.time()

    map_bug2id_exec()
    make_template_exec()
    reset_mbfl_exec()
    send_template_exec()
    distribute_bug_versions_exec()
    prepare_bin_exec()
    send_bin_exec()
    run_command_exec()
    retreive_data_exec()

    end_time = time.time()
    print('Total time: {:.2f} secs'.format(end_time - start_time))