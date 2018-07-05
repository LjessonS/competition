- 分词

```shell
#使用splitText.py对atec_nlp_sim_train_add.csv、atec_nlp_sim_train.csv两个训练集（competion目录下）进行分词
$ mkdir split #将分词后的文件放入split文件夹
$ python splitText.py atec_nlp_sim_train.csv split/atec_nlp_sim_train_split.csv
$ python splitText.py atec_nlp_sim_train_add.csv split/atec_nlp_sim_train_add.csv
```

- 转换为词向量

```shell
#从本地load vectors.bin文件(competion目录下)，用word_vector_cnn.py脚本从该文件中输出分词后的文本的词向量,将
#用法：python 分词后的文本训练集 分词后的文本向量 question格式的文件名(输出文件) word_embed格式的文件名（输出文件）
$ cd split
$ python word_vector_cnn.py ../atec_nlp_sim_train_split.csv train_split.csv question_split.csv word_embed_split.csv
$ python word_vector_cnn.py ../atec_nlp_sim_train_add.csv train_add_split.csv question_add_split.csv word_embed_add_split.csv
```

- 或者一键执行上述步骤

```shell
#将atec_nlp_sim_train_add.csv、atec_nlp_sim_train.csv、vectors.bin文件放在competion目录下
#执行下面的脚本
$ git clone 
$ cd competion
$ cat oneKey.sh
mkdir split #将分词后的文件放入split文件夹
python splitText.py atec_nlp_sim_train.csv split/atec_nlp_sim_train_split.csv
python splitText.py atec_nlp_sim_train_add.csv split/atec_nlp_sim_train_add_split.csv
cd split
python ../word_vector_cnn.py atec_nlp_sim_train_split.csv train_split.csv question_split.csv word_embed_split.csv
python ../word_vector_cnn.py atec_nlp_sim_train_add_split.csv train_add_split.csv question_add_split.csv word_embed_add_split.csv
$ sh oneKey.sh
```

