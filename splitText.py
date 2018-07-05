#-*- coding:utf-8 -*-
import jieba
import sys
import codecs
import ipdb


def cut_and_write(input_file, output):
    with open(output,'w+') as fo:
        with open(input_file, 'r') as fi:
            for line in fi:
                stripped_line = line.strip().decode("utf-8", 'ignore').split('\t')
                linenum, sentence0, sentence1, label = stripped_line 
                #ipdb.set_trace()
                seg0, seg1 = jieba.cut(sentence0), jieba.cut(sentence1)
                cut_sentence = linenum + "\t" + ' '.join(seg0) + '\t' + ' '.join(seg1) + "\t" + label + "\n"

                fo.write(cut_sentence.encode('utf-8'))
                print cut_sentence

if __name__ == "__main__":
    #input = "atec_nlp_sim_train.csv"
    #output = "atec_nlp_sim_train_split.csv"
    input_file = sys.argv[1] 
    output = sys.argv[2]
    #ipdb.set_trace()
    cut_and_write(input_file, output)
