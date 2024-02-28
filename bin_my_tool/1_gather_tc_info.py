#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent

def custom_sort(tc):
    return int(tc[3:])

if __name__ == "__main__":
    data_per_bug_dir = main_dir / 'data_per_bug'
    
    # get directory names in list of data_per_bug
    bug_dirs_list = [d.name for d in data_per_bug_dir.iterdir()]
    assert len(bug_dirs_list) == 153, len(bug_dirs_list)

    bug_dirs_list = sorted(bug_dirs_list, key=custom_sort)

    data = main_dir / 'data_24_02_26'
    if not data.exists():
        data.mkdir()
    
    tc_info_per_bug = data / 'testcase_info_per_bug_version'
    if not tc_info_per_bug.exists():
        tc_info_per_bug.mkdir()

    for bug_version in bug_dirs_list:
        bug_version_dir = tc_info_per_bug / bug_version
        if not bug_version_dir.exists():
            bug_version_dir.mkdir()
        
        testcase_info_dir = data_per_bug_dir / bug_version / 'data/testcase_info'

        cmd = ['cp', '-r', str(testcase_info_dir), str(bug_version_dir)]
        res = sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE, encoding='utf-8')
        if res.returncode != 0:
            print(res.stderr)
            exit(1)
    
    print('Done')