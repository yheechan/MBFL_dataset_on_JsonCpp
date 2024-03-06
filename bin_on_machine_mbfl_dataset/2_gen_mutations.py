#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os
import sys

script_path = Path(os.path.realpath(__file__))
bin_dir = script_path.parent
main_dir = bin_dir.parent

def initiate_directory(core_dir):
    assert core_dir.exists()
    mutations_dir = core_dir / 'mutations'
    if mutations_dir.exists():
        cmd = ['rm', '-rf', mutations_dir]
        sp.call(cmd, cwd=main_dir)
        print('>> removed directory: {}'.format(mutations_dir))
        mutations_dir.mkdir()
    if not mutations_dir.exists():
        mutations_dir.mkdir()
    
    output_dirs = []
    files = ['json_reader.cpp', 'json_value.cpp', 'json_writer.cpp']
    for file in files:
        file_dir = mutations_dir / file
        output_dirs.append(file_dir)
        if not file_dir.exists():
            file_dir.mkdir()
    
    return mutations_dir, output_dirs
            
# /home/yangheechan/mbfl-dataset-gen/structure-project/MUSICUP/music
# /home/yangheechan/mbfl-dataset-gen/structure-project/MUSICUP/jsoncpp_template/src/lib_json/json_reader.cpp
# -o /home/yangheechan/mbfl-dataset-gen/structure-project/MUSICUP/outputs.0/mutations-json_reader.cpp
# -l 1 -p /home/yangheechan/mbfl-dataset-gen/structure-project/MUSICUP/jsoncpp_template/build/compile_commands.json
# > /home/yangheechan/mbfl-dataset-gen/structure-project/MUSICUP/outputs.0/mutations-json_reader.cpp/output.0 2>&1

def gen_mutations(jsoncpp_dir, mutations_dir, output_dirs):
    # musicup
    musicup_exe = main_dir / 'bin_on_machine_mbfl_dataset/musicup'
    assert musicup_exe.exists()

    # build command file path
    compile_commands = jsoncpp_dir / 'build/compile_commands.json'

    # target file
    target_file_paths = [jsoncpp_dir / 'src/lib_json' / target.name for target in output_dirs]

    for target_file, output_dir in zip(target_file_paths, output_dirs):
        # real_output_dir = output_dir / 'line_74'
        # real_output_dir.mkdir()

        cmd = [
            musicup_exe,
            str(target_file),
            # '-rs', str(target_file)+':74',
            # '-re', str(target_file)+':74',
            '-o', str(output_dir),
            # '-o', str(real_output_dir),
            '-l', '5',
            '-p', str(compile_commands),
            '>' , str(output_dir / 'output.0'), '2>&1'
        ]
        res = sp.call(cmd)
        if res != 0:
            print('musicup failed: {}'.format(res))
            exit(1)
        # break

if __name__ == "__main__":
    core_id = sys.argv[1]
    core_dir = main_dir / core_id
    jsoncpp_dir = core_dir / 'jsoncpp_template'

    mutations_dir, outputs_dirs = initiate_directory(core_dir)
    gen_mutations(jsoncpp_dir, mutations_dir, outputs_dirs)

