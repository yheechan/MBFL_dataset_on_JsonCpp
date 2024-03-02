#!/usr/bin/python3
import subprocess as sp
from pathlib import Path
import os

script_path = Path(os.path.realpath(__file__))
my_tool_dir = script_path.parent
main_dir = my_tool_dir.parent

def custom_sort(tc):
    return int(tc[3:])

if __name__ == "__main__":
    data_per_bug_dir = main_dir / 'prerequisite_data_per_bug'
    data_per_bug_dir = main_dir / 'data_per_bug'
    
    # get directory names in list of data_per_bug
    bug_dirs_list = [d.name for d in data_per_bug_dir.iterdir()]
    assert len(bug_dirs_list) == 153

    bug_dirs_list = sorted(bug_dirs_list, key=custom_sort)

    data = main_dir / '_prerequisite_data_240301'
    data = main_dir / '_prerequisite_data_past'
    if not data.exists():
        data.mkdir()

    column_line = ''
    rows = []
    average_summary = {
        'failing_tc': 0,
        'passing_tc': 0,
        'total_tc': 0,
        'lines_executed_by_failing_tc': 0,
        'lines_executed_by_passing_tc': 0,
        'total_lines_executed': 0,
        'total_lines': 0,
        'total_coverage': 0
    }

    total_cnt = 0
    for bug_version in bug_dirs_list:
        version_sum = data_per_bug_dir / bug_version / 'prerequisite_data/version_summary.csv'
        version_sum = data_per_bug_dir / bug_version / 'data/version_summary.csv'

        version_sum_fp = open(version_sum, 'r')
        lines = version_sum_fp.readlines()
        version_sum_fp.close()
        if column_line == '':
            column_line = 'bug_version,'+lines[0].strip()
        
        for line in lines[1:]:
            line = line.strip()
            line = '{},{}'.format(bug_version, line)
            rows.append(line)

            info = line.split(',')
            average_summary['failing_tc'] += int(info[1])
            average_summary['passing_tc'] += int(info[2])
            average_summary['total_tc'] += int(info[3])
            average_summary['lines_executed_by_failing_tc'] += int(info[4])
            average_summary['lines_executed_by_passing_tc'] += int(info[5])
            average_summary['total_lines_executed'] += int(info[6])
            average_summary['total_lines'] += int(info[7])
            average_summary['total_coverage'] += float(info[8])
            total_cnt += 1

    for key in average_summary:
        average_summary[key] = average_summary[key] / total_cnt
    
    version_sum_fp = open(data / 'coverage_summary_per_bug_version.csv', 'w')
    version_sum_fp.write(column_line+'\n')
    for row in rows:
        version_sum_fp.write(row+'\n')
    
    version_sum_fp.write('average,')
    for key in average_summary:
        version_sum_fp.write('{:.2f}'.format(average_summary[key]))
        if key != 'total_coverage':
            version_sum_fp.write(',')
    version_sum_fp.write('\n')
    version_sum_fp.close()
    print('Done')