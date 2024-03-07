#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os
import csv

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent

def custom_sort(tc):
    return int(tc.name[3:])

def get_lines_executed_by_failing_tc(prerequisite_bug_dir):
    lines_exec_failing_txt = prerequisite_bug_dir / 'prerequisite_data/coverage_data/lines_executed_by_failing_TC.txt'
    assert lines_exec_failing_txt.exists()

    with open(lines_exec_failing_txt, 'r') as f:
        lines = f.readlines()
        return len(lines)
    
def get_mutated_lines(mbfl_data_bug_dir, buggy_line_key):
    buggy_target_file = buggy_line_key.split('#')[0].split('/')[-1]
    buggy_line_num = int(buggy_line_key.split('#')[-1])

    mutants_db_csv = mbfl_data_bug_dir / 'mbfl_data/selected_mutants/mutants_db.csv'
    assert mutants_db_csv.exists()

    line2mutants = {}

    mutated_line_cnt = 0
    mutant_on_buggy_line = 0

    with open(mutants_db_csv, 'r') as f:
        reader = csv.reader(f)
        # skip first header line
        next(reader)
        # do read row by row
        for row in reader:
            line_no = int(row[1])
            line_key = 'line_{}'.format(line_no)
            mutant_id = row[2]
            target_file = row[0]

            if target_file == buggy_target_file and line_no == buggy_line_num:
                mutant_on_buggy_line += 1
            
            if line_key not in line2mutants:
                mutated_line_cnt += 1
                line2mutants[line_key] = []
            line2mutants[line_key].append(mutant_id)

    mutant_per_line_cnt = 0
    for line_key in line2mutants:
        mutant_per_line_cnt += len(line2mutants[line_key])
    
    average_mutants_per_line = mutant_per_line_cnt / mutated_line_cnt

    return mutated_line_cnt, average_mutants_per_line, line2mutants, mutant_on_buggy_line

def get_uncompilable_mutants(mbfl_data_bug_dir, line2mutants):
    mutants_db_csv = mbfl_data_bug_dir / 'mbfl_data/per_mutant_data'
    assert mutants_db_csv.exists()

    line_cnt = 0
    total_build_failed_cnt = 0

    number_of_lines_all_uncompilable = 0

    for line_key in line2mutants:
        line_cnt += 1
        build_failed_cnt = 0

        for mutant_id in line2mutants[line_key]:
            mutant_dir = mutants_db_csv / mutant_id
            assert mutant_dir.exists()
            
            build_result_txt = mutant_dir / 'build_result.txt'
            assert build_result_txt.exists()


            with open(build_result_txt, 'r') as f:
                lines = f.readlines()
                line = lines[0].strip()
                if line == 'build-failed':
                    build_failed_cnt += 1

        if build_failed_cnt == len(line2mutants[line_key]):
            number_of_lines_all_uncompilable += 1

        total_build_failed_cnt += build_failed_cnt
    
    average_uncompilable_mutants_per_line = total_build_failed_cnt / line_cnt

    return average_uncompilable_mutants_per_line, number_of_lines_all_uncompilable

def get_buggy_line(bug_version):
    # get buggy_line_key
    buggy_line_key = ''
    bug2id_csv = main_dir / 'data_in_need/bug2id.csv'
    assert bug2id_csv.exists(), f'{bug2id_csv} does not exist'

    bug2id_fp = open(bug2id_csv, 'r')
    csv_reader = csv.reader(bug2id_fp)
    next(csv_reader)

    for row in csv_reader:
        bug_id = row[0]

        if bug_id == bug_version:
            buggy_line_key = '#'.join(row[3].split('#')[1:])
            break
    
    assert buggy_line_key != ''

    return buggy_line_key

if __name__ == "__main__":
    data_list = []

    mbfl_dataset_dir = main_dir / 'mbfl_dataset_per_bug-v1-240307'
    assert mbfl_dataset_dir.exists()

    prerequisite_data_dir = main_dir / 'prerequisite_data_per_bug'
    assert prerequisite_data_dir.exists()

    bug_lists = []
    bug_dirs = [bug_dir for bug_dir in mbfl_dataset_dir.iterdir() if bug_dir.exists() and bug_dir.is_dir()]
    bug_dirs = sorted(bug_dirs, key=custom_sort)

    cnt = 0
    for bug_dir in bug_dirs:
        prerequisite_bug_dir = prerequisite_data_dir / bug_dir.name
        assert prerequisite_bug_dir.exists()
        mbfl_data_bug_dir = mbfl_dataset_dir / bug_dir.name
        assert mbfl_data_bug_dir.exists()

        print('Bug Version:', bug_dir.name)

        buggy_line_key = get_buggy_line(bug_dir.name)

        lines_exec_failing = get_lines_executed_by_failing_tc(prerequisite_bug_dir)
        mutated_line_cnt, average_mutants_per_line, line2mutants, mutant_on_buggy_line = get_mutated_lines(mbfl_data_bug_dir, buggy_line_key)
        average_uncompilable_mutants_per_line, number_of_lines_all_uncompilable = get_uncompilable_mutants(mbfl_data_bug_dir, line2mutants)
        
        bug_lists.append({
            'bug_version': bug_dir.name,
            '# of lines executed by failing TCs': lines_exec_failing,
            '# of mutated lines (from lines executed by failing TCs)': mutated_line_cnt,
            '# of mutated lines / # of lines executed by failing TCs': mutated_line_cnt / lines_exec_failing,
            'average # of mutants per mutated line': average_mutants_per_line,
            '# of mutants on the buggy line': mutant_on_buggy_line,
            'average # of uncompilable mutants per mutated line': average_uncompilable_mutants_per_line,
            '# of lines with all mutants as uncompilable': number_of_lines_all_uncompilable
        })
    
    with open('mbfl_dataset_summary.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=bug_lists[0].keys())
        writer.writeheader()
        writer.writerows(bug_lists)