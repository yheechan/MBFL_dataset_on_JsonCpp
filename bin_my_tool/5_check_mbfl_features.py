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


if __name__ == "__main__":
    data_list = []

    mbfl_dataset_dir = main_dir / 'mbfl_dataset_per_bug'
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
        print('bug_dir:', bug_dir)
        mbfl_features_csv = bug_dir / 'mbfl_data/mbfl_features.csv'
        assert mbfl_features_csv.exists()
