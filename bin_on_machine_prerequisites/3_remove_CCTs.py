#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import sys
import json
import csv

script_path = Path(os.path.realpath(__file__))
bin_dir = script_path.parent
main_dir = bin_dir.parent


def get_tc_from_results(core_dir, tc_type):
    testcase_info_dir = core_dir / 'prerequisite_data/testcase_info'
    file_name = '{}.csv'.format(tc_type)
    tc_csv = testcase_info_dir / file_name

    tc_dict = {}
    failing_tc_fp = open(tc_csv, 'r')
    failing_tc_lines = failing_tc_fp.readlines()
    for line in failing_tc_lines:
        line = line.strip()
        if line == 'tc_id,tc_name':
            continue
        tc_id, tc_name = line.split(',')
        tc_dict[tc_id] = tc_name
    failing_tc_fp.close()
    return tc_dict

def get_line2function_json(core_dir):
    line2function_dir = core_dir / 'prerequisite_data/line2function_data'
    
    line2func_file_name = 'line2function.json'
    line2func_file_path = line2function_dir / line2func_file_name
    
    json_data = {}
    with open(line2func_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    return json_data

def custom_sort(tc):
    return int(tc[2:])

def return_fuction(fname, lnum, line2function_dict):
    endName = fname.split('/')[-1]
    useName = endName if endName == 'CMakeCXXCompilerId.cpp' else fname

    if useName in line2function_dict.keys():
        for funcData in line2function_dict[useName]:
            funcName = funcData[0]
            funcStart = funcData[1]
            funcEnd = funcData[2]

            if lnum >= funcStart and lnum <= funcEnd:
                return funcName
    return 'FUNCTIONNOTFOUND'


def get_bug_version(core_dir):
    bug_version_txt = core_dir / 'prerequisite_data/bug_version.txt'
    bug_version_txt = bug_version_txt.open('r')
    bug_version = bug_version_txt.readline().strip()
    bug_version_txt.close()
    bug_version = bug_version.split('-')[-1]
    return bug_version

def get_buggy_line_key(core_dir):
    
    # get bug_id
    bug_version = get_bug_version(core_dir)

    # get buggy_line_key
    buggy_line_key = ''
    bug2id_csv = main_dir / 'data_in_need/bug2id.csv'
    bug2id_fp = open(bug2id_csv, 'r')
    csv_reader = csv.reader(bug2id_fp)
    next(csv_reader)
    for row in csv_reader:
        bug_id = row[0]

        if bug_id == bug_version:
            buggy_line_key = row[3]
            break
    
    assert buggy_line_key != ''

    return bug_version, buggy_line_key


def check_cct(cov_json, cct_dict, tc_id, failing_tc_dict, passing_tc_dict,
              line2func_dict, buggy_line_key):
    pass_or_fail = False if tc_id in failing_tc_dict else True
    if pass_or_fail:
        assert tc_id in passing_tc_dict
    
    for file in cov_json['files']:
        filename = file['file']
        
        for line in file['lines']:
            line_number = line['line_number']
            function_name = return_fuction(filename, line_number, line2func_dict)
            
            row_name = filename+'#'+function_name+"#"+str(line_number)
            
            # check the buggy row
            if row_name == buggy_line_key:
                # check if it is executed by this tc
                covered = True if line['count'] > 0 else False
                if covered == True:
                    # check if the tc is passing
                    if pass_or_fail == True:
                        assert tc_id not in failing_tc_dict
                        assert tc_id in passing_tc_dict
                        assert tc_id not in cct_dict

                        cct_dict[tc_id] = passing_tc_dict[tc_id]
                        del passing_tc_dict[tc_id]


def get_cct(core_dir, failing_tc_dict, passing_tc_dict,
            line2func_dict, buggy_line_key):
    # get coverage data
    coverage_dir = core_dir / 'prerequisite_data/coverage_data'
    cov_per_tc_dir = coverage_dir / 'coverage_per_tc'
    cov_summary_dir = coverage_dir / 'coverage_summary_per_tc'

    # get list of total tc_id in sorted order
    tc_list = list(failing_tc_dict.keys()) + list(passing_tc_dict.keys())
    tc_list = sorted(tc_list, key=custom_sort)
    
    cct_dict = {}
    # check whether single tc is a cct
    for tc_id in tc_list:
        cov_file_name = '{}.cov.json'.format(tc_id)
        cov_file_path = cov_per_tc_dir / cov_file_name
        cov_json = json.load(open(cov_file_path, 'r'))
        
        check_cct(cov_json, cct_dict, tc_id,
                  failing_tc_dict, passing_tc_dict,
                  line2func_dict, buggy_line_key
        )
    
    return cct_dict

def write_tc_info(core_dir, tc_dict, tc_type):
    data_dir = core_dir / 'prerequisite_data'
    if not data_dir.exists():
        data_dir.mkdir()
    tc_dir = data_dir / 'testcase_info'
    if not tc_dir.exists():
        tc_dir.mkdir()
    
    tc_file_name = '{}.csv'.format(tc_type)
    tc_file_path = tc_dir / tc_file_name
    tc_file_fp = open(tc_file_path, 'w')
    tc_file_fp.write('tc_id,tc_name\n')
    for tc_id, tc_name in tc_dict.items():
        tc_file_fp.write('{},{}\n'.format(tc_id, tc_name))
    tc_file_fp.close()
    return

if __name__ == "__main__":
    core_id = sys.argv[1]
    core_dir = main_dir / core_id
    jsoncpp_dir = core_dir / 'jsoncpp_template'
    build_dir = jsoncpp_dir / 'build'

    # get tc lists to postprocess
    failing_tc_dict = get_tc_from_results(core_dir, 'failing_testcases')
    passing_tc_dict = get_tc_from_results(core_dir, 'passing_testcases')
    assert (len(failing_tc_dict) + len(passing_tc_dict)) == 127

    # get line2function data
    line2func_dict = get_line2function_json(core_dir)

    # get buggy line
    buggy_version, buggy_line_key = get_buggy_line_key(core_dir)
    buggy_line_key = '#'.join(buggy_line_key.split('#')[1:])

    cct_dict = get_cct(core_dir, failing_tc_dict, passing_tc_dict,
                       line2func_dict, buggy_line_key)
    
    write_tc_info(core_dir, failing_tc_dict, 'failing_testcases')
    write_tc_info(core_dir, passing_tc_dict, 'passing_testcases')
    write_tc_info(core_dir, cct_dict, 'cc_testcases')

    
    fail_cnt = len(failing_tc_dict)
    pass_cnt = len(passing_tc_dict)
    cct_cnt = len(cct_dict)

    assert fail_cnt + pass_cnt + cct_cnt == 127

    print('fail_cnt:', fail_cnt)
    print('pass_cnt:', pass_cnt)
    print('cct_cnt:', cct_cnt)
    print('total:', fail_cnt + pass_cnt + cct_cnt)