#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os
import sys

script_file_path = Path(os.path.realpath(__file__))
bin_dir = script_file_path.parent
main_dir = bin_dir.parent

def get_machinecore2bug():
    machinecore2bug_file = main_dir / 'data_in_need/machinecore2bug.csv'
    machinecore2bug_fp = open(machinecore2bug_file, 'r')
    lines = machinecore2bug_fp.readlines()
    
    machinecore2bug = {}
    for line in lines[1:]:
        info = line.strip().split(',')
        machine = info[0]
        core = info[1]
        bug_version = info[2]
        
        if machine not in machinecore2bug:
            machinecore2bug[machine] = {}
        machinecore2bug[machine][core] = bug_version
    return machinecore2bug

def run_command(bash_name, machinecore2bug, experiment_name, command_name):
    bash_file = open(bash_name, 'w')
    bash_file.write('date\n')
    
    cnt = 0
    for machine in machinecore2bug:
        for core in machinecore2bug[machine]:
            bug_version = machinecore2bug[machine][core]
            command = 'ssh {} \"cd {}/bin_on_machine_mbfl_dataset && ./{} {} > {}.output.{} 2>&1\" & \n'.format(
                machine, experiment_name, command_name, core, command_name, core
            )
            bash_file.write(command)
            
            if cnt % 5 == 0:
                bash_file.write("sleep 1s\n")
                # bash_file.write("wait\n")
            cnt += 1
    
    bash_file.write('echo ssh done, waiting...\n')
    bash_file.write('date\n')
    bash_file.write('wait\n')
    bash_file.write('date\n')

    cmd = ['chmod', '+x', bash_name]
    res = sp.call(cmd, cwd=bin_dir)

if __name__ == "__main__":
    experiment_name = sys.argv[1]
    command_name = sys.argv[2]
    
    machinecore2bug = get_machinecore2bug()
    run_command('8-1_run_selective_command.sh', machinecore2bug, experiment_name, command_name)
