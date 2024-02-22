#!/usr/bin/python3

import subprocess as sp
from pathlib import Path
import os
import sys
import json

script_path = Path(os.path.realpath(__file__))
bin_dir = script_path.parent
main_dir = bin_dir.parent


def get_tc_from_results(core_dir, tc_type):
    testcase_info_dir = core_dir / 'data/testcase_info'
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
    line2function_dir = core_dir / 'data/line2function_data'
    
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
    cov_data, cov_json, line2func_data, tc_id,
    failing_tc_dict, passing_tc_dict,
    lines_executed_by_failing_tc, lines_executed_by_passing_tc, lines_executed_by_tc,
    coverage_summary
):
    cov_data['col_data'].append(tc_id)
    
    tc_type = False if tc_id in failing_tc_dict else True
    if tc_type:
        assert tc_id in passing_tc_dict
    
    cnt = 0
    for file in cov_json['files']:
        filename = file['file']
        
        for i in range(len(file['lines'])):
            line = file['lines'][i]
            line_number = line['line_number']
            function_name = return_fuction(filename, line_number, line2func_data)
            
            row_name = filename+'#'+function_name+"#"+str(line_number)
            
            assert row_name == cov_data['row_data'][cnt][0], '{} != {}'.format(row_name, cov_data['row_data'][cnt][0])
            if row_name == cov_data['row_data'][cnt][0]:
                cov_result = 1 if line['count'] > 0 else 0
                cov_data['row_data'][cnt].append(cov_result)
                
                if cov_result == 1:
                    if row_name not in lines_executed_by_tc:
                        lines_executed_by_tc[row_name] = []
                    lines_executed_by_tc[row_name].append(tc_id)
                    if tc_type:
                        if row_name not in lines_executed_by_passing_tc:
                            lines_executed_by_passing_tc[row_name] = []
                        lines_executed_by_passing_tc[row_name].append(tc_id)
                    else:
                        if row_name not in lines_executed_by_failing_tc:
                            lines_executed_by_failing_tc[row_name] = []
                        lines_executed_by_failing_tc[row_name].append(tc_id)                    
            cnt += 1
    return

def write_postprocessed_data(core_dir, cov_data):
    data_dir = core_dir / 'data'
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
    coverage_dir = core_dir / 'data/coverage_data/'
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
    data_dir = core_dir / 'data'
    
    version_summary_dir = data_dir / 'version_summary.csv'
    version_summary_fp = open(version_summary_dir, 'w')
    version_summary_fp.write('# of failing_tc,# of passing_tc,# of total_tc,# of lines executed by failing TC,# of lines executed by passing tc,total # of lines executed,total # of lines, total coverage\n')
    version_summary_fp.write('{},{},{},{},{},{},{},{:.2f}\n'.format(
        coverage_summary['failing_tc'],
        coverage_summary['passing_tc'],
        coverage_summary['total_tc'],
        coverage_summary['lines_executed_by_failing_tc'],
        coverage_summary['lines_executed_by_passing_tc'],
        coverage_summary['total_lines_executed'],
        coverage_summary['total_lines'],
        (coverage_summary['total_lines_executed']/coverage_summary['total_lines'])*100
    ))
    


def postprocess_cov(
    core_dir, jsoncpp_dir,
    failing_tc_dict, passing_tc_dict,
    line2func_dict,
    lines_executed_by_failing_tc, lines_executed_by_passing_tc, lines_executed_by_tc,
    coverage_summary
):
    # get coverage data
    coverage_dir = core_dir / 'data/coverage_data'
    cov_per_tc_dir = coverage_dir / 'coverage_per_tc'
    cov_summary_dir = coverage_dir / 'coverage_summary_per_tc'
    
    # get list of total tc_id in sorted order
    tc_list = list(failing_tc_dict.keys()) + list(passing_tc_dict.keys())
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
            cov_data, cov_json, line2func_dict, tc_id,
            failing_tc_dict, passing_tc_dict,
            lines_executed_by_failing_tc, lines_executed_by_passing_tc, lines_executed_by_tc,
            coverage_summary
        )

    # json.dump(cov_data, open('cov_data.json', 'w'), ensure_ascii=False, indent=4)
    coverage_summary['failing_tc'] = len(failing_tc_dict)
    coverage_summary['passing_tc'] = len(passing_tc_dict)
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
    core_dir = main_dir / core_id
    jsoncpp_dir = core_dir / 'jsoncpp_template'
    build_dir = jsoncpp_dir / 'build'

    # get tc lists to postprocess
    failing_tc_dict = get_tc_from_results(core_dir, 'failing_testcases')
    passing_tc_dict = get_tc_from_results(core_dir, 'passing_testcases')
    
    lines_executed_by_failing_tc = {}
    lines_executed_by_passing_tc = {}
    lines_executed_by_tc = {}
    coverage_summary = {
        'failing_tc': 0,
        'passing_tc': 0,
        'total_tc': 0,
        'lines_executed_by_failing_tc': 0,
        'lines_executed_by_passing_tc': 0,
        'total_lines_executed': 0,
        'total_lines': 0,
    }

    assert (len(failing_tc_dict) + len(passing_tc_dict)) == 127
    
    # get line2function data
    line2func_dict = get_line2function_json(core_dir)
    
    postprocess_cov(
        core_dir, jsoncpp_dir,
        failing_tc_dict, passing_tc_dict,
        line2func_dict,
        lines_executed_by_failing_tc, lines_executed_by_passing_tc, lines_executed_by_tc,
        coverage_summary
    )

    # failing_tc_dict, passing_tc_list = run_tc(
    #     core_dir, jsoncpp_test, tc_dict, jsoncpp_dir, gen_cov=gen_cov)

    # print('{} fails + {} pass = {} total'.format(
    #     len(failing_tc_dict), len(passing_tc_list),
    #     len(failing_tc_dict)+len(passing_tc_list))
    # )

    # write_tc_info(core_dir, failing_tc_dict, 'failing_testcases')
    # write_tc_info(core_dir, passing_tc_list, 'passing_testcases')
    