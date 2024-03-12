date
ssh faster7 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core0 > 4_run_mutants.py.output.core0 2>&1" & 
sleep 1s
ssh faster7 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core1 > 4_run_mutants.py.output.core1 2>&1" & 
ssh faster7 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core2 > 4_run_mutants.py.output.core2 2>&1" & 
ssh faster7 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core3 > 4_run_mutants.py.output.core3 2>&1" & 
ssh faster7 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core4 > 4_run_mutants.py.output.core4 2>&1" & 
ssh faster7 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core5 > 4_run_mutants.py.output.core5 2>&1" & 
sleep 1s
ssh faster7 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core6 > 4_run_mutants.py.output.core6 2>&1" & 
ssh faster7 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core7 > 4_run_mutants.py.output.core7 2>&1" & 
ssh faster14 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core0 > 4_run_mutants.py.output.core0 2>&1" & 
ssh faster14 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core1 > 4_run_mutants.py.output.core1 2>&1" & 
ssh faster14 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core2 > 4_run_mutants.py.output.core2 2>&1" & 
sleep 1s
ssh faster14 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core3 > 4_run_mutants.py.output.core3 2>&1" & 
ssh faster14 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core4 > 4_run_mutants.py.output.core4 2>&1" & 
ssh faster14 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core5 > 4_run_mutants.py.output.core5 2>&1" & 
ssh faster14 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core6 > 4_run_mutants.py.output.core6 2>&1" & 
ssh faster14 "cd mbfl_dataset_6mts-240308/bin_on_machine_mbfl_dataset && ./4_run_mutants.py core7 > 4_run_mutants.py.output.core7 2>&1" & 
sleep 1s
echo ssh done, waiting...
date
wait
date
