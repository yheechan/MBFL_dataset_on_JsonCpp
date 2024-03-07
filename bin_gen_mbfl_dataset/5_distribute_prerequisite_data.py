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
    
    machinecore2bug_file = main_dir / 'data_in_need_dataset/machinecore2bug.csv'
    machinecore2bug_fp = open(machinecore2bug_file, 'r')
    # machinecore2bug_fp.write('machine,core,bug_version\n')
    lines = machinecore2bug_fp.readlines()
    machinecore2bug_fp.close()
    # skip the first line
    for line in lines[1:]:
        machine, core, bug_version = line.strip().split(',')
        if machine not in assigned_machines:
            assigned_machines[machine] = {}
        assigned_machines[machine][core] = bug_version
    
    return assigned_machines

def send_prerequisite_data(bash_name, experiment_name):
    machines = get_available_machines()
    print("Resetting MBFL on {} machines".format(len(machines)))


    assigned_machines = get_assigned_machines(machines)

    cnt = 0
    for machines in assigned_machines:
        print('machine {}'.format(machines))
        for core in assigned_machines[machines]:
            print('\t{}: '.format(core))
            print('\t\t{}'.format(assigned_machines[machines][core]))
            cnt += 1
    print('total: ', cnt)
    
    bash_file = open(bash_name, 'w')
    bash_file.write('date\n')

    cnt = 0
    data_per_bug_dir = main_dir / 'prerequisite_data_per_bug'
    assert data_per_bug_dir.exists()

    tc_line_cov_list = [
        'lines_executed_by_failing_TC.txt',
        'lines_executed_by_passing_TC.txt',
    ]

    for machine in assigned_machines:
        print('machine {}'.format(machine))

        for core_id in assigned_machines[machine]:
            bug_id = assigned_machines[machine][core_id]
            bug_dir = data_per_bug_dir / bug_id / 'prerequisite_data'
            assert bug_dir.exists(), bug_dir

            print('\t{}: '.format(core_id))
            print('\t\t{}'.format(bug_id))

            # send per test case line coverage
            for tc_line_cov in tc_line_cov_list:
                file = bug_dir / 'coverage_data' / tc_line_cov
                assert file.exists()
                file_name = file.name
                bash_file.write('scp -r {} {}:/home/yangheechan/{}/{}/prerequisite_data/coverage_data/{} & \n'.format(
                    file, machine, experiment_name, core_id, file_name
                ))
            
            # send post processed coverage data
            pp_dir = bug_dir / 'postprocessed_coverage_data'
            assert pp_dir.exists()
            bash_file.write('scp -r {} {}:/home/yangheechan/{}/{}/prerequisite_data/ & \n'.format(
                pp_dir, machine, experiment_name, core_id
            ))

            # send testcase info
            tc_info_dir = bug_dir / 'testcase_info'
            assert tc_info_dir.exists()
            bash_file.write('scp -r {} {}:/home/yangheechan/{}/{}/prerequisite_data/ & \n'.format(
                tc_info_dir, machine, experiment_name, core_id
            ))

            # send version summary
            version_summary = bug_dir / 'version_summary.csv'
            assert version_summary.exists()
            bash_file.write('scp -r {} {}:/home/yangheechan/{}/{}/prerequisite_data/ & \n'.format(
                version_summary, machine, experiment_name, core_id
            ))

            # send bug version txt
            bug_version_txt = bug_dir / 'bug_version.txt'
            assert bug_version_txt.exists()
            bash_file.write('scp -r {} {}:/home/yangheechan/{}/{}/prerequisite_data/ & \n'.format(
                bug_version_txt, machine, experiment_name, core_id
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
    send_prerequisite_data('5_distribute_prerequisite_data.sh', experiment_name)