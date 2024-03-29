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

def run_command(bash_name, machinecore2bug, experiment_name, mutation_size, l_cnt, target_machines):
    designated_machines = []
    if target_machines[0] == '' and len(target_machines) == 1:
        designated_machines = machinecore2bug.keys()
    else:
        designated_machines = target_machines

    bash_file = open(bash_name, 'w')
    bash_file.write('date\n')
    
    cnt = 0
    for machine in machinecore2bug:
        if machine not in designated_machines:
            continue
        
        for core in machinecore2bug[machine]:
            bug_version = machinecore2bug[machine][core]
            command = 'ssh {} \"cd {}/bin_on_machine_mbfl_dataset && ./command.py {} {} {} > output.{} 2>&1\" & \n'.format(
                machine, experiment_name, core, mutation_size, l_cnt, core
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
    mutation_size = int(sys.argv[2])
    l_cnt = sys.argv[3]
    target_machines = sys.argv[4].split(' ')
    
    machinecore2bug = get_machinecore2bug()
    run_command('8_run_command.sh', machinecore2bug, experiment_name, mutation_size, l_cnt, target_machines)
