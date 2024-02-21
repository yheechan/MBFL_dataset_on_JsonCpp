#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import pandas as pd

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent

def make_clone(template_name):
    cmd = [
        'git', 'clone', 'https://github.com/open-source-parsers/jsoncpp.git', template_name
    ]

    reset_cmd = ['git', 'reset', '--hard', '83946a2']

    res = sp.call(cmd, cwd=main_dir)
    if res != 0:
        print('Error: {}'.format(res))
        return
    
    template_dir = main_dir / template_name
    res = sp.call(reset_cmd, cwd=template_dir)
    if res != 0:
        print('Error: {}'.format(res))
        return

def change_files(template_name):
    project_path = main_dir / template_name
    selected_bug_dir = main_dir / 'new_bug_versions_jsoncpp/original_version'
    src_dir = main_dir / 'past_data/src'

    value_file = [
        project_path / 'src/lib_json/json_value.cpp',
        selected_bug_dir / 'json_value.cpp'
    ]
    reader_file = [
        project_path / 'src/lib_json/json_reader.cpp',
        selected_bug_dir / 'json_reader.cpp'
    ]
    test_main_file = [
        project_path / 'src/test_lib_json/main.cpp',
        src_dir / 'main.cpp'
    ]
    cmakeFile = [
        project_path / 'CMakeLists.txt',
        src_dir / 'CMakeLists.txt'
    ]
    
    # copy new version
    cmd = ['cp', value_file[1], value_file[0]]
    res = sp.call(cmd, cwd=project_path)
    print('copy 1: ', res)

    cmd = ['cp', reader_file[1], reader_file[0]]
    res = sp.call(cmd, cwd=project_path)
    print('copy 2: ', res)

    cmd = ['cp', test_main_file[1], test_main_file[0]]
    res = sp.call(cmd, cwd=project_path)
    print('copy 3: ', res)

    cmd = ['cp', cmakeFile[1], cmakeFile[0]]
    res = sp.call(cmd, cwd=project_path)
    print('copy 4: ', res)
        

if __name__ == '__main__':
    make_clone('jsoncpp_template')
    change_files('jsoncpp_template')