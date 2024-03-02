date
ssh faster4 "mkdir -p mbfl_dataset/core0" &
ssh faster4 "mkdir -p mbfl_dataset/core1" &
ssh faster4 "mkdir -p mbfl_dataset/core2" &
ssh faster4 "mkdir -p mbfl_dataset/core3" &
ssh faster4 "mkdir -p mbfl_dataset/core4" &
sleep 1s
wait
ssh faster4 "mkdir -p mbfl_dataset/core5" &
ssh faster4 "mkdir -p mbfl_dataset/core6" &
ssh faster4 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster4:/home/yangheechan/mbfl_dataset/ &
ssh faster5 "mkdir -p mbfl_dataset/core0" &
ssh faster5 "mkdir -p mbfl_dataset/core1" &
sleep 1s
wait
ssh faster5 "mkdir -p mbfl_dataset/core2" &
ssh faster5 "mkdir -p mbfl_dataset/core3" &
ssh faster5 "mkdir -p mbfl_dataset/core4" &
ssh faster5 "mkdir -p mbfl_dataset/core5" &
ssh faster5 "mkdir -p mbfl_dataset/core6" &
sleep 1s
wait
ssh faster5 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster5:/home/yangheechan/mbfl_dataset/ &
ssh faster7 "mkdir -p mbfl_dataset/core0" &
ssh faster7 "mkdir -p mbfl_dataset/core1" &
ssh faster7 "mkdir -p mbfl_dataset/core2" &
ssh faster7 "mkdir -p mbfl_dataset/core3" &
sleep 1s
wait
ssh faster7 "mkdir -p mbfl_dataset/core4" &
ssh faster7 "mkdir -p mbfl_dataset/core5" &
ssh faster7 "mkdir -p mbfl_dataset/core6" &
ssh faster7 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster7:/home/yangheechan/mbfl_dataset/ &
ssh faster8 "mkdir -p mbfl_dataset/core0" &
sleep 1s
wait
ssh faster8 "mkdir -p mbfl_dataset/core1" &
ssh faster8 "mkdir -p mbfl_dataset/core2" &
ssh faster8 "mkdir -p mbfl_dataset/core3" &
ssh faster8 "mkdir -p mbfl_dataset/core4" &
ssh faster8 "mkdir -p mbfl_dataset/core5" &
sleep 1s
wait
ssh faster8 "mkdir -p mbfl_dataset/core6" &
ssh faster8 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster8:/home/yangheechan/mbfl_dataset/ &
ssh faster9 "mkdir -p mbfl_dataset/core0" &
ssh faster9 "mkdir -p mbfl_dataset/core1" &
ssh faster9 "mkdir -p mbfl_dataset/core2" &
sleep 1s
wait
ssh faster9 "mkdir -p mbfl_dataset/core3" &
ssh faster9 "mkdir -p mbfl_dataset/core4" &
ssh faster9 "mkdir -p mbfl_dataset/core5" &
ssh faster9 "mkdir -p mbfl_dataset/core6" &
ssh faster9 "mkdir -p mbfl_dataset/core7" &
sleep 1s
wait
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster9:/home/yangheechan/mbfl_dataset/ &
ssh faster14 "mkdir -p mbfl_dataset/core0" &
ssh faster14 "mkdir -p mbfl_dataset/core1" &
ssh faster14 "mkdir -p mbfl_dataset/core2" &
ssh faster14 "mkdir -p mbfl_dataset/core3" &
ssh faster14 "mkdir -p mbfl_dataset/core4" &
sleep 1s
wait
ssh faster14 "mkdir -p mbfl_dataset/core5" &
ssh faster14 "mkdir -p mbfl_dataset/core6" &
ssh faster14 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster14:/home/yangheechan/mbfl_dataset/ &
ssh faster15 "mkdir -p mbfl_dataset/core0" &
ssh faster15 "mkdir -p mbfl_dataset/core1" &
sleep 1s
wait
ssh faster15 "mkdir -p mbfl_dataset/core2" &
ssh faster15 "mkdir -p mbfl_dataset/core3" &
ssh faster15 "mkdir -p mbfl_dataset/core4" &
ssh faster15 "mkdir -p mbfl_dataset/core5" &
ssh faster15 "mkdir -p mbfl_dataset/core6" &
sleep 1s
wait
ssh faster15 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster15:/home/yangheechan/mbfl_dataset/ &
ssh faster16 "mkdir -p mbfl_dataset/core0" &
ssh faster16 "mkdir -p mbfl_dataset/core1" &
ssh faster16 "mkdir -p mbfl_dataset/core2" &
ssh faster16 "mkdir -p mbfl_dataset/core3" &
sleep 1s
wait
ssh faster16 "mkdir -p mbfl_dataset/core4" &
ssh faster16 "mkdir -p mbfl_dataset/core5" &
ssh faster16 "mkdir -p mbfl_dataset/core6" &
ssh faster16 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster16:/home/yangheechan/mbfl_dataset/ &
ssh faster17 "mkdir -p mbfl_dataset/core0" &
sleep 1s
wait
ssh faster17 "mkdir -p mbfl_dataset/core1" &
ssh faster17 "mkdir -p mbfl_dataset/core2" &
ssh faster17 "mkdir -p mbfl_dataset/core3" &
ssh faster17 "mkdir -p mbfl_dataset/core4" &
ssh faster17 "mkdir -p mbfl_dataset/core5" &
sleep 1s
wait
ssh faster17 "mkdir -p mbfl_dataset/core6" &
ssh faster17 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster17:/home/yangheechan/mbfl_dataset/ &
ssh faster18 "mkdir -p mbfl_dataset/core0" &
ssh faster18 "mkdir -p mbfl_dataset/core1" &
ssh faster18 "mkdir -p mbfl_dataset/core2" &
sleep 1s
wait
ssh faster18 "mkdir -p mbfl_dataset/core3" &
ssh faster18 "mkdir -p mbfl_dataset/core4" &
ssh faster18 "mkdir -p mbfl_dataset/core5" &
ssh faster18 "mkdir -p mbfl_dataset/core6" &
ssh faster18 "mkdir -p mbfl_dataset/core7" &
sleep 1s
wait
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster18:/home/yangheechan/mbfl_dataset/ &
ssh faster19 "mkdir -p mbfl_dataset/core0" &
ssh faster19 "mkdir -p mbfl_dataset/core1" &
ssh faster19 "mkdir -p mbfl_dataset/core2" &
ssh faster19 "mkdir -p mbfl_dataset/core3" &
ssh faster19 "mkdir -p mbfl_dataset/core4" &
sleep 1s
wait
ssh faster19 "mkdir -p mbfl_dataset/core5" &
ssh faster19 "mkdir -p mbfl_dataset/core6" &
ssh faster19 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster19:/home/yangheechan/mbfl_dataset/ &
ssh faster20 "mkdir -p mbfl_dataset/core0" &
ssh faster20 "mkdir -p mbfl_dataset/core1" &
sleep 1s
wait
ssh faster20 "mkdir -p mbfl_dataset/core2" &
ssh faster20 "mkdir -p mbfl_dataset/core3" &
ssh faster20 "mkdir -p mbfl_dataset/core4" &
ssh faster20 "mkdir -p mbfl_dataset/core5" &
ssh faster20 "mkdir -p mbfl_dataset/core6" &
sleep 1s
wait
ssh faster20 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster20:/home/yangheechan/mbfl_dataset/ &
ssh faster21 "mkdir -p mbfl_dataset/core0" &
ssh faster21 "mkdir -p mbfl_dataset/core1" &
ssh faster21 "mkdir -p mbfl_dataset/core2" &
ssh faster21 "mkdir -p mbfl_dataset/core3" &
sleep 1s
wait
ssh faster21 "mkdir -p mbfl_dataset/core4" &
ssh faster21 "mkdir -p mbfl_dataset/core5" &
ssh faster21 "mkdir -p mbfl_dataset/core6" &
ssh faster21 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster21:/home/yangheechan/mbfl_dataset/ &
ssh faster23 "mkdir -p mbfl_dataset/core0" &
sleep 1s
wait
ssh faster23 "mkdir -p mbfl_dataset/core1" &
ssh faster23 "mkdir -p mbfl_dataset/core2" &
ssh faster23 "mkdir -p mbfl_dataset/core3" &
ssh faster23 "mkdir -p mbfl_dataset/core4" &
ssh faster23 "mkdir -p mbfl_dataset/core5" &
sleep 1s
wait
ssh faster23 "mkdir -p mbfl_dataset/core6" &
ssh faster23 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster23:/home/yangheechan/mbfl_dataset/ &
ssh faster24 "mkdir -p mbfl_dataset/core0" &
ssh faster24 "mkdir -p mbfl_dataset/core1" &
ssh faster24 "mkdir -p mbfl_dataset/core2" &
sleep 1s
wait
ssh faster24 "mkdir -p mbfl_dataset/core3" &
ssh faster24 "mkdir -p mbfl_dataset/core4" &
ssh faster24 "mkdir -p mbfl_dataset/core5" &
ssh faster24 "mkdir -p mbfl_dataset/core6" &
ssh faster24 "mkdir -p mbfl_dataset/core7" &
sleep 1s
wait
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster24:/home/yangheechan/mbfl_dataset/ &
ssh faster25 "mkdir -p mbfl_dataset/core0" &
ssh faster25 "mkdir -p mbfl_dataset/core1" &
ssh faster25 "mkdir -p mbfl_dataset/core2" &
ssh faster25 "mkdir -p mbfl_dataset/core3" &
ssh faster25 "mkdir -p mbfl_dataset/core4" &
sleep 1s
wait
ssh faster25 "mkdir -p mbfl_dataset/core5" &
ssh faster25 "mkdir -p mbfl_dataset/core6" &
ssh faster25 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster25:/home/yangheechan/mbfl_dataset/ &
ssh faster26 "mkdir -p mbfl_dataset/core0" &
ssh faster26 "mkdir -p mbfl_dataset/core1" &
sleep 1s
wait
ssh faster26 "mkdir -p mbfl_dataset/core2" &
ssh faster26 "mkdir -p mbfl_dataset/core3" &
ssh faster26 "mkdir -p mbfl_dataset/core4" &
ssh faster26 "mkdir -p mbfl_dataset/core5" &
ssh faster26 "mkdir -p mbfl_dataset/core6" &
sleep 1s
wait
ssh faster26 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster26:/home/yangheechan/mbfl_dataset/ &
ssh faster27 "mkdir -p mbfl_dataset/core0" &
ssh faster27 "mkdir -p mbfl_dataset/core1" &
ssh faster27 "mkdir -p mbfl_dataset/core2" &
ssh faster27 "mkdir -p mbfl_dataset/core3" &
sleep 1s
wait
ssh faster27 "mkdir -p mbfl_dataset/core4" &
ssh faster27 "mkdir -p mbfl_dataset/core5" &
ssh faster27 "mkdir -p mbfl_dataset/core6" &
ssh faster27 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster27:/home/yangheechan/mbfl_dataset/ &
ssh faster29 "mkdir -p mbfl_dataset/core0" &
sleep 1s
wait
ssh faster29 "mkdir -p mbfl_dataset/core1" &
ssh faster29 "mkdir -p mbfl_dataset/core2" &
ssh faster29 "mkdir -p mbfl_dataset/core3" &
ssh faster29 "mkdir -p mbfl_dataset/core4" &
ssh faster29 "mkdir -p mbfl_dataset/core5" &
sleep 1s
wait
ssh faster29 "mkdir -p mbfl_dataset/core6" &
ssh faster29 "mkdir -p mbfl_dataset/core7" &
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster29:/home/yangheechan/mbfl_dataset/ &
ssh faster30 "mkdir -p mbfl_dataset/core0" &
ssh faster30 "mkdir -p mbfl_dataset/core1" &
ssh faster30 "mkdir -p mbfl_dataset/core2" &
sleep 1s
wait
ssh faster30 "mkdir -p mbfl_dataset/core3" &
ssh faster30 "mkdir -p mbfl_dataset/core4" &
ssh faster30 "mkdir -p mbfl_dataset/core5" &
ssh faster30 "mkdir -p mbfl_dataset/core6" &
ssh faster30 "mkdir -p mbfl_dataset/core7" &
sleep 1s
wait
scp -r /home/yangheechan/mbfl-dataset-gen/MBFL_dataset_on_JsonCpp/original_jsoncpp faster30:/home/yangheechan/mbfl_dataset/ &
ssh faster4 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster4 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster4 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster4 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster4 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
sleep 1s
wait
ssh faster4 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster4 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster4 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster5 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster5 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
sleep 1s
wait
ssh faster5 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster5 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster5 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster5 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster5 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
sleep 1s
wait
ssh faster5 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster7 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster7 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster7 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster7 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
sleep 1s
wait
ssh faster7 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster7 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster7 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster7 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster8 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
sleep 1s
wait
ssh faster8 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster8 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster8 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster8 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster8 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
sleep 1s
wait
ssh faster8 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster8 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster9 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster9 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster9 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
sleep 1s
wait
ssh faster9 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster9 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster9 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster9 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster9 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
sleep 1s
wait
ssh faster14 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster14 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster14 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster14 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster14 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
sleep 1s
wait
ssh faster14 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster14 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster14 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster15 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster15 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
sleep 1s
wait
ssh faster15 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster15 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster15 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster15 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster15 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
sleep 1s
wait
ssh faster15 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster16 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster16 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster16 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster16 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
sleep 1s
wait
ssh faster16 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster16 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster16 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster16 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster17 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
sleep 1s
wait
ssh faster17 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster17 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster17 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster17 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster17 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
sleep 1s
wait
ssh faster17 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster17 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster18 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster18 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster18 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
sleep 1s
wait
ssh faster18 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster18 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster18 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster18 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster18 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
sleep 1s
wait
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
sleep 1s
wait
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster19 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster20 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster20 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
sleep 1s
wait
ssh faster20 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster20 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster20 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster20 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster20 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
sleep 1s
wait
ssh faster20 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster21 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster21 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster21 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster21 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
sleep 1s
wait
ssh faster21 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster21 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster21 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster21 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster23 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
sleep 1s
wait
ssh faster23 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster23 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster23 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster23 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster23 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
sleep 1s
wait
ssh faster23 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster23 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster24 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster24 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster24 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
sleep 1s
wait
ssh faster24 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster24 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster24 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster24 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster24 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
sleep 1s
wait
ssh faster25 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster25 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster25 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster25 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster25 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
sleep 1s
wait
ssh faster25 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster25 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster25 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster26 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster26 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
sleep 1s
wait
ssh faster26 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster26 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster26 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster26 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster26 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
sleep 1s
wait
ssh faster26 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster27 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster27 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster27 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster27 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
sleep 1s
wait
ssh faster27 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster27 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster27 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster27 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster29 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
sleep 1s
wait
ssh faster29 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster29 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
ssh faster29 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster29 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster29 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
sleep 1s
wait
ssh faster29 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster29 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
ssh faster30 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core0/jsoncpp_template" &
ssh faster30 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core1/jsoncpp_template" &
ssh faster30 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core2/jsoncpp_template" &
sleep 1s
wait
ssh faster30 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core3/jsoncpp_template" &
ssh faster30 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core4/jsoncpp_template" &
ssh faster30 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core5/jsoncpp_template" &
ssh faster30 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core6/jsoncpp_template" &
ssh faster30 "cp -r /home/yangheechan/mbfl_dataset/original_jsoncpp /home/yangheechan/mbfl_dataset/core7/jsoncpp_template" &
sleep 1s
wait
echo ssh done, waiting...
date
wait
date
