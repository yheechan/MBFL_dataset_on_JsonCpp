#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import pandas as pd

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent

def build_and_copy_extractor():
    extractor_dir = main_dir / 'extractor'
    cmd = ['make', '-j20']
    res = sp.run(cmd, cwd=extractor_dir)
    if res.returncode != 0:
        print('make extractor failed: {}'.format(res))
        exit(1)
    
    bin_on_machine_dir = main_dir / 'bin_on_machine'
    cmd = ['cp', extractor_dir / 'extractor', bin_on_machine_dir]
    res = sp.run(cmd)
    if res.returncode != 0:
        print('cp extractor failed: {}'.format(res))
        exit(1)
    return    

if __name__ == '__main__':
    build_and_copy_extractor()
    