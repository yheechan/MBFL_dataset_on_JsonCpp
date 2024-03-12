#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os
import sys

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent

def custom_sort(tc):
    return int(tc.name[3:])

def validate_generation(bug_dirs):
    cnt = 0
    error_bug = []
    for bug_dir in bug_dirs:
        assert bug_dir.exists()

        # print('Bug Version:', bug_dir)
        mbfl_features_csv = bug_dir / 'mbfl_data/mbfl_features.csv'
        if not mbfl_features_csv.exists():
            error_bug.append(bug_dir.name)
    
    if len(error_bug) > 0:
        print('[Invalid] {} bug without mbfl_features.csv file generated.', len(error_bug))
        for bug in error_bug:
            print(bug)
    else:
        print('[Valid] {} bug versions has mbfl_features.csv'.format(len(bug_dirs)))

def validate_mutant_runs_against_selected(bug_dirs):
    for bug_dir in bug_dirs:
        # print('Bug Version:', bug_dir)
        assert bug_dir.exists()

        selected_db_csv = bug_dir / 'mbfl_data/selected_mutants/mutants_db.csv'
        assert selected_db_csv.exists()

        selcted_mutants_fp = open(selected_db_csv, 'r')
        lines = selcted_mutants_fp.readlines()
        selcted_mutants_fp.close()
        selected_mutants = [mutant.strip() for mutant in lines[1:]]

        selected_mutant_id = []        
        # cnt = 0
        for mutant in selected_mutants:
            mutant_id = mutant.split(',')[2]
            selected_mutant_id.append(mutant_id)

            # cnt += 1
            # print('\t{} Mutant ID: {}'.format(cnt, mutant_id))
        
        per_mutant_data_dir = bug_dir / 'mbfl_data/per_mutant_data'
        assert per_mutant_data_dir.exists()

        ran_mutant_id = []
        for mutant_dir in per_mutant_data_dir.iterdir():
            assert mutant_dir.exists()
            mutant_id = mutant_dir.name
            ran_mutant_id.append(mutant_id)

        # VALIDATE HERE
        assert len(selected_mutant_id) == len(ran_mutant_id)

        for mutant_id in selected_mutant_id:
            assert mutant_id in ran_mutant_id
        for mutant_id in ran_mutant_id:
            assert mutant_id in selected_mutant_id
    
    print('[Valid] selected mutants for {} bug versions have been ran successfully.'.format(len(bug_dirs)))


if __name__ == "__main__":
    dataset_dir_name = sys.argv[1]

    mbfl_dataset_dir = main_dir / dataset_dir_name
    assert mbfl_dataset_dir.exists()

    bug_lists = []
    bug_dirs = [bug_dir for bug_dir in mbfl_dataset_dir.iterdir() if bug_dir.exists() and bug_dir.is_dir()]
    assert len(bug_dirs) == 153
    bug_dirs = sorted(bug_dirs, key=custom_sort)

    validate_generation(bug_dirs)
    # validate_mutant_runs_against_selected(bug_dirs)