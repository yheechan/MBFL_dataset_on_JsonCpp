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

def reset_mfbl(bash_name, experiment_name, target_machines):
    machines = []
    if target_machines[0] == '' and len(target_machines) == 1:
        machines = get_available_machines()
    else:
        machines = target_machines
    print("Resetting MBFL on {} machines".format(len(machines)))

    bash_file = open(bash_name, 'w')
    bash_file.write('date\n')

    cnt = 0
    for machine in machines:
        bash_file.write('ssh {} "rm -rf {}/" &\n'.format(machine, experiment_name))
        cnt += 1
        if cnt%5 == 0:
            bash_file.write("sleep 1s\n")
            bash_file.write('wait\n')
    
    bash_file.write('echo ssh done, waiting...\n')
    bash_file.write('date\n')
    bash_file.write('wait\n')
    bash_file.write('date\n')

    cmd = ['chmod', '+x', bash_name]
    res = sp.run(cmd)
            

if __name__ == '__main__':
    experiment_name = sys.argv[1]
    target_machines = sys.argv[2].split(' ')
    reset_mfbl('2_reset_mbfl_dataset.sh', experiment_name, target_machines)