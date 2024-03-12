date
ssh faster19 "cd mbfl_dataset_12mts_music-240311/bin_on_machine_mbfl_dataset && ./command.py core0 12 5 > output.core0 2>&1" & 
sleep 1s
ssh faster19 "cd mbfl_dataset_12mts_music-240311/bin_on_machine_mbfl_dataset && ./command.py core1 12 5 > output.core1 2>&1" & 
ssh faster19 "cd mbfl_dataset_12mts_music-240311/bin_on_machine_mbfl_dataset && ./command.py core2 12 5 > output.core2 2>&1" & 
ssh faster19 "cd mbfl_dataset_12mts_music-240311/bin_on_machine_mbfl_dataset && ./command.py core3 12 5 > output.core3 2>&1" & 
ssh faster19 "cd mbfl_dataset_12mts_music-240311/bin_on_machine_mbfl_dataset && ./command.py core4 12 5 > output.core4 2>&1" & 
ssh faster19 "cd mbfl_dataset_12mts_music-240311/bin_on_machine_mbfl_dataset && ./command.py core5 12 5 > output.core5 2>&1" & 
sleep 1s
ssh faster19 "cd mbfl_dataset_12mts_music-240311/bin_on_machine_mbfl_dataset && ./command.py core6 12 5 > output.core6 2>&1" & 
ssh faster19 "cd mbfl_dataset_12mts_music-240311/bin_on_machine_mbfl_dataset && ./command.py core7 12 5 > output.core7 2>&1" & 
echo ssh done, waiting...
date
wait
date
