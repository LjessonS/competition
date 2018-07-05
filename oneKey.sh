#!/bin/bash
plit #将分词后的文件放入split文件夹
python splitText.py atec_nlp_sim_train.csv split/atec_nlp_sim_train_split.csv
python splitText.py atec_nlp_sim_train_add.csv split/atec_nlp_sim_train_add_split.csv
cd split
python ../atec_nlp_sim_train_split.csv train_split.csv question_split.csv word_embed_split.csv
python ../atec_nlp_sim_train_add.csv train_add_split.csv question_add_split.csv word_embed_add_split.csv
