#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import sys

script_path = Path(os.path.realpath(__file__))
bin_gen_mbfl_dir = script_path.parent
main_dir = bin_gen_mbfl_dir.parent

def get_available_machines():
    machine_txt = Path('/home/yangheechan/.hosts/mbfl_servers')
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

        # format: file_path, version_name
        bug_versions_list.append([file_path, version_name])
    
    print('bug_versions_list: ', len(bug_versions_list))
    
    machinecore2bug_file = main_dir / 'data_in_need_dataset/machinecore2bug.csv'
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
            assigned_machines[machine][i] = bug_versions_list[bug_version_cnt]
            
            machinecore2bug_fp.write('{},core{},{}\n'.format(machine, i, bug_versions_list[bug_version_cnt][1]))
            bug_version_cnt += 1
        if bug_version_cnt == len(bug_versions_list):
            break
    
    return assigned_machines

def send_bug_version(bash_name, experiment_name, target_machines):
    machines = get_available_machines()
    print("Resetting MBFL on {} machines".format(len(machines)))

    bash_file = open(bash_name, 'w')
    bash_file.write('date\n')

    assigned_machines = get_assigned_machines(machines)

    designated_machines = []
    if target_machines[0] == '' and len(target_machines) == 1:
        designated_machines = machines
    else:
        designated_machines = target_machines

    cnt = 0
    for machine in assigned_machines:
        if machine not in designated_machines:
            continue
        
        print('machine {}'.format(machine))

        for core_num in assigned_machines[machine]:
            print('\tcore{}: '.format(core_num))

            # for file in assigned_machines[assigned_machines][core].iterdir():
            file = assigned_machines[machine][core_num][0]
            version_name = assigned_machines[machine][core_num][1]
            file_name = file.name
            print('\t\t{}'.format(file))
            bash_file.write('scp {} {}:/home/yangheechan/{}/core{}/jsoncpp_template/src/lib_json/{} & \n'.format(
                file, machine, experiment_name, core_num, file_name
            ))
            bash_file.write('ssh {} \"mkdir -p /home/yangheechan/{}/core{}/mbfl_data/bug_version_code\"\n'.format(
                machine, experiment_name, core_num
            ))
            bash_file.write('scp {} {}:/home/yangheechan/{}/core{}/mbfl_data/bug_version_code/{} & \n'.format(
                file, machine, experiment_name, core_num, file_name
            ))
            bash_file.write('ssh {} \"mkdir -p /home/yangheechan/{}/core{}/mbfl_data && echo {}-core{}-{} > /home/yangheechan/{}/core{}/mbfl_data/bug_version.txt\" & \n'.format(
                machine, experiment_name, core_num, machine, core_num, version_name, experiment_name, core_num
            ))
            # make directory for prepared data
            bash_file.write('ssh {} \"mkdir -p /home/yangheechan/{}/core{}/prerequisite_data/coverage_data\" & \n'.format(
                machine, experiment_name, core_num,
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
    experiment_name = sys.argv[1]
    target_machines = sys.argv[2].split(' ')
    send_bug_version('4_distribute_bug_versions.sh', experiment_name, target_machines)