#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os

script_path = Path(os.path.realpath(__file__))
bin_gen_mbfl_dir = script_path.parent
main_dir = bin_gen_mbfl_dir.parent

def clone_musicup(muisicup_dir):
    name = muisicup_dir.name
    parent_dir = muisicup_dir.parent

    # clone
    cmd = ['git', 'clone', 'https://github.com/swtv-kaist/MUSICUP.git', name]
    res = sp.run(cmd, cwd=parent_dir)
    if res.returncode != 0:
        print('clone musicup failed: {}'.format(res))
        exit(1)
    
    # checkout to develop
    cmd = ['git', 'checkout', 'develop']
    res = sp.run(cmd, cwd=muisicup_dir)
    if res.returncode != 0:
        print('checkout musicup failed: {}'.format(res))
        exit(1)
    
def build_musicup():
    musicup_dir = main_dir.parent / 'MUSICUP'

    # if music doesn't exist clone from github
    if not musicup_dir.exists():
        clone_musicup(musicup_dir)

    musicup_exe = main_dir.parent / 'MUSICUP/music'
    if musicup_exe.exists():
        print('musicup already built')
        return
    
    cmd = ['make', 'LLVM_BUILD_PATH=/usr/lib/llvm-13', '-j20']
    res = sp.run(cmd, cwd=musicup_dir)
    if res.returncode != 0:
        print('build musicup failed: {}'.format(res))
        exit(1)
    
    musicup_in_bin = main_dir / 'bin_on_machine_mbfl_dataset/musicup'
    if not musicup_in_bin.exists():
        cmd = ['cp', musicup_exe, musicup_in_bin]
        res = sp.run(cmd)
        if res.returncode != 0:
            print('copy musicup to bin failed: {}'.format(res))
            exit(1)

if __name__ == '__main__':
    build_musicup()