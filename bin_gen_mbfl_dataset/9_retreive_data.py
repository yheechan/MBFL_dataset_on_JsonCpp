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

def retreive_data(bash_name, machinecore2bug, datset_dir_name, experiment_name, target_machines):
    # mbfl_dataset_12mts-240308
    data_per_bug = main_dir / datset_dir_name
    if not data_per_bug.exists():
        data_per_bug.mkdir()
    
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
            bug_version_dir = data_per_bug / bug_version
            if bug_version_dir.exists():
                user_input = input("Do you want to remove {}? (y/n): ".format(bug_version_dir))
                if user_input == 'n':
                    continue
                
                # remove bug_version_dir
                cmd = 'rm -rf {}'.format(bug_version_dir)
                res  = sp.call(cmd, shell=True)
                if res != 0:
                    print('Error: {}'.format(res))
                    exit(1)

            cmd = 'mkdir -p {}'.format(bug_version_dir)
            res  = sp.call(cmd, shell=True)
            if res != 0:
                print('Error: {}'.format(res))
                exit(1)
            
            command = 'scp -r {}:/home/yangheechan/{}/{}/mbfl_data {} & \n'.format(
                machine, experiment_name, core, bug_version_dir
            )
            bash_file.write(command)
            
            if cnt % 5 == 0:
                bash_file.write("sleep 1s\n")
                # bash_file.write("wait\n")
            cnt += 1
    print('total bug version data: ', cnt)
    
    bash_file.write('echo scp done, waiting...\n')
    bash_file.write('date\n')
    bash_file.write('wait\n')
    bash_file.write('date\n')

    cmd = ['chmod', '+x', bash_name]
    res = sp.call(cmd, cwd=bin_dir)

if __name__ == "__main__":
    datset_dir_name = sys.argv[1]
    experiment_name = sys.argv[2]
    target_machines = sys.argv[3].split(' ')
    machinecore2bug = get_machinecore2bug()
    retreive_data('9_retreive_data.sh', machinecore2bug, datset_dir_name, experiment_name, target_machines)
