#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import sys

script_path = Path(os.path.realpath(__file__))
bin_dir = script_path.parent
main_dir = bin_dir.parent

clangPP = Path('/usr/bin/clang++-13')

def build_jsoncpp(project_dir, dir_name):
    build_dir = project_dir / dir_name

    if not build_dir.exists():
        build_dir.mkdir()
    if build_dir.exists():
        cmd = ['rm', '-rf', build_dir]
        sp.call(cmd, cwd=main_dir)
        print('>> removed directory: {}'.format(build_dir))
        build_dir.mkdir()
    
    cmd = [
        'cmake',
        '-DCMAKE_CXX_COMPILER={}'.format(clangPP),
        '-DCMAKE_CXX_FLAGS=-O0 -fprofile-arcs -ftest-coverage -g -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION --save-temps',
        # '-DCMAKE_CXX_FLAGS=-O0 -fprofile-arcs -ftest-coverage -g -fno-omit-frame-pointer -gline-tables-only -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION',
        '-DBUILD_SHARED_LIBS=OFF', '-G',
        'Unix Makefiles',
        '../'
    ]
  
    res = sp.call(cmd, cwd=build_dir)
    if res != 0:
        print('cmake failed: {}'.format(res))
        exit(1)

    return

def make_jsoncpp(project_dir, dir_name):
    build_dir = project_dir / dir_name
    cmd = ['make', '-j20']
    res = sp.call(cmd, cwd=build_dir)
    if res != 0:
        print('make failed: {}'.format(res))
        exit(1)
    return

if __name__ == "__main__":
    core_id = sys.argv[1]
    core_dir = main_dir / core_id
    jsoncpp_dir = core_dir / 'jsoncpp_template'

    build_jsoncpp(jsoncpp_dir, 'build')
    make_jsoncpp(jsoncpp_dir, 'build')