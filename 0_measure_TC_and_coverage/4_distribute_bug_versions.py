#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import pandas as pd

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent
past_data_dir = main_dir / 'past_data'

def get_available_machines():
    machine_txt = Path('/home/yangheechan/machines.txt')
    machine_fp = open(machine_txt, 'r')
    machines = machine_fp.readlines()
    machines = [machine.strip() for machine in machines]
    machine_fp.close()
    return machines

def get_assigned_machines(machine_list):
    # machine: core#: bug_version_path
    assigned_machines = {}

    bug_versions_dir = main_dir / 'new_bug_versions_jsoncpp'
    bug_versions_list = []
    for versions in sorted(bug_versions_dir.iterdir()):
        version_name = versions.name
        if version_name == 'original_version':
            continue

        reader_file = versions / 'json_reader.cpp'
        value_file = versions / 'json_value.cpp'

        file_path = None
        if reader_file.exists():
            file_path = reader_file
        elif value_file.exists():
            file_path = value_file
        if file_path is None:
            print('Error: {} does not exist'.format(versions))
            exit(1)

        bug_versions_list.append([file_path, version_name])
    
    print('bug_versions_list: ', len(bug_versions_list))
    
    machinecore2bug_file = main_dir / 'data_in_need/machinecore2bug.csv'
    machinecore2bug_fp = open(machinecore2bug_file, 'w')
    machinecore2bug_fp.write('machine,core,bug_version\n')

    bug_version_cnt = 0
    cores = 8
    for machine in machine_list:
        assigned_machines[machine] = {}
        for i in range(cores):
            if bug_version_cnt == len(bug_versions_list):
                break
            
            # ONE FOR SINGLE CORE!!!
            assigned_machines[machine][i] = bug_versions_list[bug_version_cnt][0]
            
            machinecore2bug_fp.write('{},core{},{}\n'.format(machine, i, bug_versions_list[bug_version_cnt][1]))
            bug_version_cnt += 1
        if bug_version_cnt == len(bug_versions_list):
            break
    
    return assigned_machines

def sent_mutants(bash_name):
    machines = get_available_machines()
    print("Resetting MBFL on {} machines".format(len(machines)))

    bash_file = open(bash_name, 'w')
    bash_file.write('date\n')

    assigned_machines = get_assigned_machines(machines)

    cnt = 0
    for machine in assigned_machines:
        print('machine {}'.format(machine))

        for core_num in assigned_machines[machine]:
            print('\tcore{}: '.format(core_num))

            # for file in assigned_machines[assigned_machines][core].iterdir():
            file = assigned_machines[machine][core_num]
            file_name = file.name
            print('\t\t{}'.format(file))
            bash_file.write('scp {} {}:/home/yangheechan/mbfl/core{}/jsoncpp_template/src/lib_json/{} & \n'.format(
                file, machine, core_num, file_name
            ))
            cnt += 1
            if cnt%5 == 0:
                bash_file.write('wait\n')
                bash_file.write('sleep 1s\n')
    
    bash_file.write('echo ssh done, waiting...\n')
    bash_file.write('date\n')
    bash_file.write('wait\n')
    bash_file.write('date\n')

    cmd = ['chmod', '+x', bash_name]
    res = sp.run(cmd)
            

if __name__ == '__main__':
    sent_mutants('4_distribute_bug_versions.sh')