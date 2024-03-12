#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os
import csv
import sys
import pandas as pd

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
    selected_mutants_on_buggy_line = 0
    buggy_mutants = []
    total_mutants = 0

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
                selected_mutants_on_buggy_line += 1
                buggy_mutants.append(mutant_id)
            
            if line_key not in line2mutants:
                mutated_line_cnt += 1
                line2mutants[line_key] = []
            line2mutants[line_key].append(mutant_id)
            total_mutants += 1

    mutant_per_line_cnt = 0
    for line_key in line2mutants:
        mutant_per_line_cnt += len(line2mutants[line_key])
    
    average_mutants_per_line = mutant_per_line_cnt / mutated_line_cnt

    return mutated_line_cnt, average_mutants_per_line, line2mutants, selected_mutants_on_buggy_line, total_mutants, buggy_mutants

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

def get_susp_score_0(buggy_line_key, line2mutants):
    buggy_target_file = buggy_line_key.split('#')[0].split('/')[-1]
    buggy_line_num = int(buggy_line_key.split('#')[-1])

    mbfl_features_csv = mbfl_data_bug_dir / 'mbfl_data/mbfl_features.csv'
    assert mbfl_features_csv.exists()


    with open(mbfl_features_csv, 'r') as f:
        reader = csv.reader(f)
        # skip first header line
        next(reader)
        # do read row by row
        for row in reader:
            muse_score_0 = 0
            met_score_0 = 0

            key = row[0]
            line_no = int(key.split('#')[-1])
            target_file = key.split('#')[0].split('/')[-1]

            if target_file == buggy_target_file and line_no == buggy_line_num:
                muse_score = float(row[10])
                if muse_score == 0.0:
                    muse_score_0 = 1
                met_score = float(row[4])
                if met_score == 0.0:
                    met_score_0 = 1
                break
            else:
                continue

    return met_score_0, muse_score_0

def compile_status(mbfl_data_bug_dir, buggy_mutants):
    uncompilable_mutants_on_buggy_line = 0
    utilized_mutants_on_buggy_line = 0

    per_mutant_data_dir = mbfl_data_bug_dir / 'mbfl_data/per_mutant_data'
    assert per_mutant_data_dir.exists()

    for mutant_id in buggy_mutants:
        mutant_dir = per_mutant_data_dir / mutant_id
        assert mutant_dir.exists()

        build_result_txt = mutant_dir / 'build_result.txt'
        assert build_result_txt.exists()

        with open(build_result_txt, 'r') as f:
            lines = f.readlines()
            line = lines[0].strip()
            if line == 'build-failed':
                uncompilable_mutants_on_buggy_line += 1
            else:
                utilized_mutants_on_buggy_line += 1
    
    assert uncompilable_mutants_on_buggy_line + utilized_mutants_on_buggy_line == len(buggy_mutants)
    return uncompilable_mutants_on_buggy_line, utilized_mutants_on_buggy_line

def get_rank(mbfl_data_bug_dir, buggy_line_key):
    mbfl_features_csv = mbfl_data_bug_dir / 'mbfl_data/mbfl_features.csv'
    assert mbfl_features_csv.exists()

    # include/json/reader.h#CharReader::~CharReader()#247
    buggy_target_file = buggy_line_key.split('#')[0].split('/')[-1]
    buggy_function_name = buggy_line_key.split('#')[1]
    buggy_line_num = int(buggy_line_key.split('#')[-1])
    print('Buggy Line:', buggy_target_file, buggy_function_name, buggy_line_num)

    mbfl_features_df = pd.read_csv(mbfl_features_csv)
    # iterate through the rows of df
    for index, row in mbfl_features_df.iterrows():
        # split the 'key' column by '#'
        key = row['key']
        target_file = key.split('#')[0].split('/')[-1]
        function_name = key.split('#')[1]
        line_num = int(key.split('#')[-1])

        # drop 'key' column and add target_file, function_name, line_num as columns
        mbfl_features_df.at[index, 'target_file'] = target_file
        mbfl_features_df.at[index, 'function_name'] = function_name
        mbfl_features_df.at[index, 'line_num'] = line_num


        # check if the row is the buggy line
        if target_file == buggy_target_file and function_name == buggy_function_name:
            # print('Buggy Line found:', target_file, function_name, line_num)
            # set the 'bug' column as 1
            mbfl_features_df.at[index, 'bug'] = 1
        else:
            # set the 'bug' column as 0
            mbfl_features_df.at[index, 'bug'] = 0
    
    # drop key column of df
    mbfl_features_df = mbfl_features_df.drop(columns=['key'])
    # move 'target_file', 'function_name', 'line_num' columns to the front of the df
    mbfl_features_df = mbfl_features_df[[
        'target_file', 'function_name', 'line_num',
        'met_1', 'met_2', 'met_3', 'met_4',
        'muse_1', 'muse_2', 'muse_3', 'muse_4', 'muse_5', 'muse_6',
        'bug'
    ]]

    # merge rows with the same 'function_name' in standard of row that has the highest 'muse_6' value
    mbfl_features_df = mbfl_features_df.groupby(['target_file', 'function_name']).apply(lambda x: x.nlargest(1, 'muse_6')).reset_index(drop=True)

    # sort mbfl_features_df by 'muse_6' column
    mbfl_features_df = mbfl_features_df.sort_values(by='muse_6', ascending=False).reset_index(drop=True)
    
    # add a rank column to the df
    # the rank is in the standard of muse_6 column
    # if the rank is a tie, the rank is the upper bound of the tie
    mbfl_features_df['rank'] = mbfl_features_df['muse_6'].rank(ascending=False, method='max').astype(int)

    rank = mbfl_features_df[mbfl_features_df['bug'] == 1].index[0] + 1
    # write csv
    # mbfl_features_df.to_csv('tmp.csv', index=False)

    print('Rank:', rank)

    return rank


    

if __name__ == "__main__":
    dataset_dir_name = sys.argv[1]
    data_list = []

    mbfl_dataset_dir = main_dir / dataset_dir_name
    assert mbfl_dataset_dir.exists()

    prerequisite_data_dir = main_dir / 'prerequisite_data_per_bug'
    assert prerequisite_data_dir.exists()

    bug_lists = []
    bug_dirs = [bug_dir for bug_dir in mbfl_dataset_dir.iterdir() if bug_dir.exists() and bug_dir.is_dir()]
    bug_dirs = sorted(bug_dirs, key=custom_sort)

    cnt = 0
    rank_dict = {
        'crit1': [],
        'crit2': [],
        'crit3': [],
        'crit4': [],
    }
    for bug_dir in bug_dirs:
        prerequisite_bug_dir = prerequisite_data_dir / bug_dir.name
        assert prerequisite_bug_dir.exists()
        mbfl_data_bug_dir = mbfl_dataset_dir / bug_dir.name
        assert mbfl_data_bug_dir.exists()

        # if bug_dir.name != 'bug82': continue

        print('Bug Version:', bug_dir.name)

        buggy_line_key = get_buggy_line(bug_dir.name)

        lines_exec_failing = get_lines_executed_by_failing_tc(prerequisite_bug_dir)

        mutated_line_cnt, average_mutants_per_line, line2mutants, selected_mutants_on_buggy_line, \
        total_mutants, buggy_mutants \
            = get_mutated_lines(mbfl_data_bug_dir, buggy_line_key)
        
        average_uncompilable_mutants_per_line, number_of_lines_all_uncompilable = get_uncompilable_mutants(mbfl_data_bug_dir, line2mutants)

        metallaxis_score_0, muse_score_0 = get_susp_score_0(buggy_line_key, line2mutants)
        uncompilable_mutants_on_buggy_line, utilized_mutants_on_buggy_line = compile_status(mbfl_data_bug_dir, buggy_mutants)


        muse_rank = get_rank(mbfl_data_bug_dir, buggy_line_key)
        if muse_rank <= 10:
            rank_dict['crit1'].append(bug_dir.name)
        elif muse_rank > 10 and muse_rank <= 20:
            rank_dict['crit2'].append(bug_dir.name)
        elif muse_rank > 20 and muse_rank <= 30:
            rank_dict['crit3'].append(bug_dir.name)
        else:
            assert muse_rank > 30
            rank_dict['crit4'].append(bug_dir.name)

        
        bug_lists.append({
            'bug_version': bug_dir.name,

            '# of lines executed by failing TCs': lines_exec_failing,
            '# of mutated lines (from lines executed by failing TCs)': mutated_line_cnt,
            'ratio: # of mutated lines / # of lines executed by failing TCs': mutated_line_cnt / lines_exec_failing,
            '# of total mutants on bug version': total_mutants,

            '# of selected mutants on buggy line': selected_mutants_on_buggy_line,
            '# of uncompilable mutants on buggy line': uncompilable_mutants_on_buggy_line,
            '# of utilized mutants on buggy line': utilized_mutants_on_buggy_line,

            # 'average # of mutants per mutated line': average_mutants_per_line,
            # '# of mutants on the buggy line': mutant_on_buggy_line,
            # 'average # of uncompilable mutants per mutated line': average_uncompilable_mutants_per_line,
            # '# of lines with all mutants as uncompilable': number_of_lines_all_uncompilable,
            'Metallaxis score of buggy line is 0': metallaxis_score_0,
            'MUSE score of buggy line is 0': muse_score_0,
            'Rank of buggy line at method level (based on MUSE score)': muse_rank
        })
    
    for crit in rank_dict:
        print(f'Rank {crit}: {len(rank_dict[crit])}')
    with open(dataset_dir_name+'.summary.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=bug_lists[0].keys())
        writer.writeheader()
        writer.writerows(bug_lists)
