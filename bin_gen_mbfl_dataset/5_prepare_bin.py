#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os

script_path = Path(os.path.realpath(__file__))
bin_gen_mbfl_dir = script_path.parent
main_dir = bin_gen_mbfl_dir.parent

def build_musicup():
    muiscup_build_sh = bin_gen_mbfl_dir / '00_build_musicup.sh'
    musicup_exe = main_dir.parent / 'MUSICUP/music'
    if musicup_exe.exists():
        print('musicup already exists')
        return
    
    cmd = ['bash', muiscup_build_sh]
    res = sp.run(cmd)
    if res.returncode != 0:
        print('build musicup failed: {}'.format(res))
        exit(1)

if __name__ == '__main__':
    build_musicup()