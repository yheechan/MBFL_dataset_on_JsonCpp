date
ssh faster19 "mkdir -p mbfl_dataset_12mts_music-240311/core0" &
ssh faster19 "mkdir -p mbfl_dataset_12mts_music-240311/core1" &
ssh faster19 "mkdir -p mbfl_dataset_12mts_music-240311/core2" &
ssh faster19 "mkdir -p mbfl_dataset_12mts_music-240311/core3" &
ssh faster19 "mkdir -p mbfl_dataset_12mts_music-240311/core4" &
sleep 1s
wait
ssh faster19 "mkdir -p mbfl_dataset_12mts_music-240311/core5" &
ssh faster19 "mkdir -p mbfl_dataset_12mts_music-240311/core6" &
ssh faster19 "mkdir -p mbfl_dataset_12mts_music-240311/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster19:/home/yangheechan/mbfl_dataset_12mts_music-240311/ &
sleep 1s
wait
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset_12mts_music-240311/original_jsoncpp /home/yangheechan/mbfl_dataset_12mts_music-240311/core0/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset_12mts_music-240311/original_jsoncpp /home/yangheechan/mbfl_dataset_12mts_music-240311/core1/jsoncpp_template" &
sleep 1s
wait
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset_12mts_music-240311/original_jsoncpp /home/yangheechan/mbfl_dataset_12mts_music-240311/core2/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset_12mts_music-240311/original_jsoncpp /home/yangheechan/mbfl_dataset_12mts_music-240311/core3/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset_12mts_music-240311/original_jsoncpp /home/yangheechan/mbfl_dataset_12mts_music-240311/core4/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset_12mts_music-240311/original_jsoncpp /home/yangheechan/mbfl_dataset_12mts_music-240311/core5/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset_12mts_music-240311/original_jsoncpp /home/yangheechan/mbfl_dataset_12mts_music-240311/core6/jsoncpp_template" &
sleep 1s
wait
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset_12mts_music-240311/original_jsoncpp /home/yangheechan/mbfl_dataset_12mts_music-240311/core7/jsoncpp_template" &
echo ssh done, waiting...
date
wait
date
