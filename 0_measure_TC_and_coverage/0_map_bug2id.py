#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import pandas as pd

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent
past_data_dir = main_dir / 'past_data'


def get_buggy_line_csv(spectrum_dir, bug):
    file_name = '{}.csv'.format(bug)
    spectrum_file = spectrum_dir / file_name

    out = pd.read_csv(spectrum_file)

    # get the line where column 'bug' is 1
    buggy_line = out[out['bug'] == 1]

    # validate that buggy_line has only one row
    if len(buggy_line) != 1:
        print('Error: {} has more than one buggy line'.format(bug))
        return None
    key = buggy_line['lineNo'].values[0]
    return key

def get_buggy_line_db(bug):
    db_dict = {
        'json_reader': main_dir / 'past_data/mutant_db/json_reader_mut_db.csv',
        'json_value': main_dir / 'past_data/mutant_db/json_value_mut_db.csv'
    }

    info = bug.split('.')[0]
    mutant_db = db_dict[info]

    mutant_fp = open(mutant_db, 'r')
    mutant_lines = mutant_fp.readlines()

    cnt = 0
    for line in mutant_lines:
        if cnt < 2:
            cnt += 1
            continue

        data = line.split(',')
        # print(line)
        mutant_id = data[0]
        operator = data[1]
        og_start_line = int(data[2])
        og_end_line = int(data[4])
        og_token = data[6]
        mut_start_line = int(data[7])
        mut_end_line = int(data[9])
        mut_token = data[11]
        assert og_start_line == mut_start_line
        assert mut_start_line == mut_end_line

        if mutant_id == bug:
            buggy_line = '{}#src/lib_json/{}.cpp#{}'.format(bug, info, mut_start_line)
            return buggy_line
    



def map_bug2id():
    spectrum_dir = past_data_dir / 'spectrum_feature_data_excluding_coincidentally_correct_tc_per_bug'

    bug_versions_dir = past_data_dir / 'bug_versions_jsoncpp'
    data_in_need_dir = main_dir / 'data_in_need'
    new_bug_versions_dir = main_dir / 'new_bug_versions_jsoncpp'
    
    if not data_in_need_dir.exists():
        data_in_need_dir.mkdir()
    if not new_bug_versions_dir.exists():
        new_bug_versions_dir.mkdir()
    else:
        cmd = ['rm', '-r', str(new_bug_versions_dir)]
        res = sp.run(cmd)
        if res.returncode != 0:
            print('Error: {}'.format(res))
            return
        new_bug_versions_dir.mkdir()
    
    bug2id = data_in_need_dir / 'bug2id.csv'
    bug2id_fp = open(bug2id, 'w')
    bug2id_fp.write('bug_id,original bug name,buggy jsoncpp file,buggyline\n')

    for_4bugs = {
        'bug1': ['json_value.cpp'],
        'bug2': ['json_reader.cpp'],
        'bug3': ['json_reader.cpp'],
        'bug4': ['json_reader.cpp']
    }

    bug_cnt = 1
    for version in sorted(bug_versions_dir.iterdir()):
        bug = version.name
        if bug == 'original_version':
            cmd = ['cp', '-r', str(version), new_bug_versions_dir / 'original_version']
            res = sp.run(cmd)
            if res.returncode != 0:
                print('Error: {}'.format(res))
                return
            continue

        bug_id = 'bug{}'.format(bug_cnt)

        real_bug = False
        json_file = None
        if 'bug' in bug:
            json_file = for_4bugs[bug][0]
            real_bug = True
        else:
            name_info = bug.split('.')
            json_file = '.'.join([name_info[0], name_info[2]])
        

        buggy_line = get_buggy_line_csv(spectrum_dir, bug)
        if not buggy_line:
            buggy_line_from_db = get_buggy_line_db(bug)
            lineNo_from_db = buggy_line_from_db.split('#')[2]
            lineNo_from_csv = buggy_line.split('#')[2]

            assert int(lineNo_from_db) == int(lineNo_from_csv)
        
        bug2id_fp.write('{},{},{},\"{}\"\n'.format(bug_id, bug, json_file, buggy_line))

        cmd = ['cp', '-r', str(version), new_bug_versions_dir / bug_id]
        res = sp.run(cmd)
        if res.returncode != 0:
            print('Error: {}'.format(res))
            return

        print('Moved {} to {}'.format(version, bug_id))
        bug_cnt += 1

        

if __name__ == '__main__':
    map_bug2id()