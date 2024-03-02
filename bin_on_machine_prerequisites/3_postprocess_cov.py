#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import sys
import json
import time
import csv

script_path = Path(os.path.realpath(__file__))
bin_dir = script_path.parent
main_dir = bin_dir.parent

remove_cct = bin_dir / '3_remove_CCTs.py'

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

def add_key_data(cov_data, cov_json, line2func_data, coverage_summary):
    cov_data['col_data'].append('key')
    
    cnt = 0
    for file in cov_json['files']:
        filename = file['file']
        
        for line in file['lines']:
            line_number = line['line_number']
            function_name = return_fuction(filename, line_number, line2func_data)
            
            row_name = filename+'#'+function_name+"#"+str(line_number)
            
            assert [row_name] not in cov_data['row_data']
            if [row_name] not in cov_data['row_data']:
                cov_data['row_data'].append([row_name])
                coverage_summary['total_lines'] += 1
            
            cnt += 1
    return

def add_cov_data(
    cov_data, cov_json, tc_id,
    failing_tc_dict, passing_tc_dict, cct_dict,
    line2func_dict, buggy_line_key,
    lines_executed_by_failing_tc, lines_executed_by_passing_tc,
    lines_executed_by_tc,
    coverage_summary
):
    # dont postprocess the coverage of CCT
    if tc_id in cct_dict:
        return
    
    cov_data['col_data'].append(tc_id)
    
    pass_or_fail = False if tc_id in failing_tc_dict else True
    check_bug_line_executed = False

    if pass_or_fail == True:
        assert tc_id in passing_tc_dict
        check_bug_line_executed = True
    
    
    
    cnt = 0
    for file in cov_json['files']:
        filename = file['file']
        
        for i in range(len(file['lines'])):
            line = file['lines'][i]
            line_number = line['line_number']
            function_name = return_fuction(filename, line_number, line2func_dict)
            
            row_name = filename+'#'+function_name+"#"+str(line_number)
            assert row_name == cov_data['row_data'][cnt][0], '{} != {}'.format(row_name, cov_data['row_data'][cnt][0])

            covered = 1 if line['count'] > 0 else 0
            cov_data['row_data'][cnt].append(covered)
            
            # check if line is covered
            if covered == 1:
                # add to lines executed dict
                if row_name not in lines_executed_by_tc:
                    lines_executed_by_tc[row_name] = []
                lines_executed_by_tc[row_name].append(tc_id)

                if pass_or_fail == True:
                    # add to line executed by passing tc
                    if row_name not in lines_executed_by_passing_tc:
                        lines_executed_by_passing_tc[row_name] = []
                    lines_executed_by_passing_tc[row_name].append(tc_id)
                else:
                    # add to line executed by failing tc
                    if row_name not in lines_executed_by_failing_tc:
                        lines_executed_by_failing_tc[row_name] = []
                    lines_executed_by_failing_tc[row_name].append(tc_id)

                    # check if it is the buggy line is executed for failing TC
                    if row_name == buggy_line_key:
                        check_bug_line_executed = True
            cnt += 1
    
    # assert that all fail test case executes buggy line
    assert check_bug_line_executed == True, 'buggy line {}\nnot executed by {}'.format(buggy_line_key, tc_id)
    return

def write_postprocessed_data(core_dir, cov_data):
    data_dir = core_dir / 'prerequisite_data'
    if not data_dir.exists():
        data_dir.mkdir()
    coverage_dir = data_dir / 'postprocessed_coverage_data'
    if not coverage_dir.exists():
        coverage_dir.mkdir()
    
    
    file_name = 'cov_data.csv'
    file_path = coverage_dir / file_name
    with open(file_path, 'w') as cov_fp:
        for col in cov_data['col_data']:
            cov_fp.write(col+',')

        cov_fp.write('\n')
        for row in cov_data['row_data']:
            cnt = 0
            for cell in row:
                if cnt == 0:
                    cov_fp.write('\"{}\",'.format(cell))
                else:
                    cov_fp.write(str(cell)+',')
            cov_fp.write('\n')
    return

def write_execution_data(core_dir, lines_executed_by_tc, type):
    coverage_dir = core_dir / 'prerequisite_data/coverage_data/'
    execution_file_name = 'lines_executed_by_{}_TC.txt'.format(type)
    file_path = coverage_dir / execution_file_name
    with open(file_path, 'w') as cov_fp:
        for line, tc_list in lines_executed_by_tc.items():
            cov_fp.write('{}$$'.format(line))
            for tc in tc_list:
                cov_fp.write(',{}'.format(tc))
            cov_fp.write('\n')
    return

def write_version_summary(core_dir, coverage_summary):
    data_dir = core_dir / 'prerequisite_data'

    col_data = [
        '# of failing TCs',
        '# of passing TCs',
        '# of CCTCs',
        'total # of TCs',
        '# of lines executed by failing TCs',
        '# of lines executed by passing TCs',
        'total # of lines executed',
        'total # of lines',
        'total coverage'
    ]

    col_string = ','.join(col_data)
    
    version_summary_dir = data_dir / 'version_summary.csv'
    version_summary_fp = open(version_summary_dir, 'w')
    version_summary_fp.write(col_string+'\n')
    version_summary_fp.write('{},{},{},{},{},{},{},{},{:.2f}\n'.format(
        coverage_summary['failing_tc'],
        coverage_summary['passing_tc'],
        coverage_summary['cc_tc'],
        coverage_summary['total_tc'],
        coverage_summary['lines_executed_by_failing_tc'],
        coverage_summary['lines_executed_by_passing_tc'],
        coverage_summary['total_lines_executed'],
        coverage_summary['total_lines'],
        (coverage_summary['total_lines_executed']/coverage_summary['total_lines'])*100
    ))
    


def postprocess_cov(
    core_dir, jsoncpp_dir,
    failing_tc_dict, passing_tc_dict, cct_dict,
    line2func_dict, buggy_line_key,
    lines_executed_by_failing_tc, lines_executed_by_passing_tc,
    lines_executed_by_tc,
    coverage_summary
):
    # get coverage data
    coverage_dir = core_dir / 'prerequisite_data/coverage_data'
    cov_per_tc_dir = coverage_dir / 'coverage_per_tc'
    cov_summary_dir = coverage_dir / 'coverage_summary_per_tc'
    
    # get list of total tc_id in sorted order
    tc_list = list(failing_tc_dict.keys()) + list(passing_tc_dict.keys()) + list(cct_dict.keys())
    tc_list = sorted(tc_list, key=custom_sort)
    
    first = True
    cov_data = {
        'col_data': [],
        'row_data': []
    }
    for tc_id in tc_list:
        cov_file_name = '{}.cov.json'.format(tc_id)
        cov_file_path = cov_per_tc_dir / cov_file_name
        cov_json = json.load(open(cov_file_path, 'r'))
        
        if first:
            add_key_data(cov_data, cov_json, line2func_dict, coverage_summary)
            first = False
        
        add_cov_data(
            cov_data, cov_json, tc_id,
            failing_tc_dict, passing_tc_dict, cct_dict,
            line2func_dict, buggy_line_key,
            lines_executed_by_failing_tc, lines_executed_by_passing_tc,
            lines_executed_by_tc,
            coverage_summary
        )

    # json.dump(cov_data, open('cov_data.json', 'w'), ensure_ascii=False, indent=4)
    coverage_summary['failing_tc'] = len(failing_tc_dict)
    coverage_summary['passing_tc'] = len(passing_tc_dict)
    coverage_summary['cc_tc'] = len(cct_dict)
    coverage_summary['total_tc'] = len(failing_tc_dict) + len(passing_tc_dict)
    coverage_summary['lines_executed_by_failing_tc'] = len(lines_executed_by_failing_tc)
    coverage_summary['lines_executed_by_passing_tc'] = len(lines_executed_by_passing_tc)
    coverage_summary['total_lines_executed'] = len(lines_executed_by_tc)
    
    # write coverage data as csv
    write_postprocessed_data(core_dir, cov_data)
    write_execution_data(core_dir, lines_executed_by_failing_tc, 'failing')
    write_execution_data(core_dir, lines_executed_by_passing_tc, 'passing')
    
    write_version_summary(core_dir, coverage_summary)

if __name__ == "__main__":
    core_id = sys.argv[1]
    exclude_CCT = True if sys.argv[2] == 'exclude_CCT' else False

    core_dir = main_dir / core_id
    jsoncpp_dir = core_dir / 'jsoncpp_template'
    build_dir = jsoncpp_dir / 'build'

    # if command to exclude CCT
    if exclude_CCT:
        cmd = [remove_cct, core_id]
        begin_time = time.time()
        res = sp.call(cmd)
        if res != 0:
            print('remove_cct failed: {}'.format(res))
            exit(1)
        curr_time = time.time()
        print('[{} {:.2f} secs] - Success remove_cct: {}'.format(core_id, curr_time - begin_time, res))

    # get tc lists to postprocess
    failing_tc_dict = get_tc_from_results(core_dir, 'failing_testcases')
    passing_tc_dict = get_tc_from_results(core_dir, 'passing_testcases')
    cct_dict = {}
    if exclude_CCT:
        cct_dict = get_tc_from_results(core_dir, 'cc_testcases')
    
    lines_executed_by_failing_tc = {}
    lines_executed_by_passing_tc = {}
    lines_executed_by_tc = {}
    coverage_summary = {
        'failing_tc': 0,
        'passing_tc': 0,
        'cc_tc': 0,
        'total_tc': 0,
        'lines_executed_by_failing_tc': 0,
        'lines_executed_by_passing_tc': 0,
        'total_lines_executed': 0,
        'total_lines': 0,
    }
    
    fail_cnt = len(failing_tc_dict)
    pass_cnt = len(passing_tc_dict)
    cct_cnt = len(cct_dict)
    assert fail_cnt + pass_cnt + cct_cnt == 127

    # get buggy line
    buggy_version, buggy_line_key = get_buggy_line_key(core_dir)
    buggy_line_key = '#'.join(buggy_line_key.split('#')[1:])
    
    # get line2function data
    line2func_dict = get_line2function_json(core_dir)
    
    postprocess_cov(
        core_dir, jsoncpp_dir,
        failing_tc_dict, passing_tc_dict, cct_dict,
        line2func_dict, buggy_line_key,
        lines_executed_by_failing_tc, lines_executed_by_passing_tc,
        lines_executed_by_tc,
        coverage_summary
    )
