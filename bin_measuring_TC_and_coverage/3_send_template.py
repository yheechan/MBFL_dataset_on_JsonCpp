#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import pandas as pd

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent

def get_available_machines():
    machine_txt = Path('/home/yangheechan/machines.txt')
    machine_fp = open(machine_txt, 'r')
    machines = machine_fp.readlines()
    machines = [machine.strip() for machine in machines]
    machine_fp.close()
    return machines

def reset_mfbl(bash_name, template_name):
    machines = get_available_machines()
    print("Resetting MBFL on {} machines".format(len(machines)))

    bash_file = open(bash_name, 'w')
    bash_file.write('date\n')

    template_dir = main_dir / template_name
    number_of_cores = 8
    cnt = 0
    for machine in machines:
        # send template to a machine
        for i in range(number_of_cores):
            bash_file.write('ssh {} \"mkdir -p mbfl/core{}" &\n'.format(machine, i))
            cnt += 1
            if cnt%5 == 0:
                bash_file.write("sleep 1s\n")
                bash_file.write('wait\n')
        bash_file.write('scp -r {} {}:/home/yangheechan/mbfl/ &\n'.format(
            template_dir, machine
        ))
    
    for machine in machines:
        # copy template
        for i in range(number_of_cores):
            bash_file.write('ssh {} \"cp -r /home/yangheechan/mbfl/{} /home/yangheechan/mbfl/core{}/\" &\n'.format(
                machine, template_name, i
            ))
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
    reset_mfbl('3_send_template.sh', 'jsoncpp_template')