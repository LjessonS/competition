#coding:utf-8
import sys
reload(sys)
import ipdb
import gensim
sys.setdefaultencoding('utf8')

VECTOR_DIR = '../vectors.bin'
w2v_model = gensim.models.KeyedVectors.load_word2vec_format(VECTOR_DIR, binary=True)

input_file = sys.argv[1]
traincsvName = sys.argv[2]
questionName = sys.argv[3]
word_embed = sys.argv[4]

words = []
q = []
with open(input_file) as f:
    for line in f:
        _, Q0, Q1, label = line.strip().decode("utf-8", "ignore").split('\t')
        q.append(Q0)
        q.append(Q1)
        words += Q0.split(" ")
        words += Q1.split(" ")

q_uniq = [q_it for q_it in set(q)]
words_uniq = [words_it for words_it in set(words)]
q_uniq_len = len(q_uniq)
words_uniq_len = len(words_uniq)

word_prob_dict = {}
for word, i in zip(words_uniq, xrange(words_uniq_len)):
    if word in w2v_model:
        word_prob_dict[word] = w2v_model[word]

remained_words = word_prob_dict.keys()

word_posSt_dict = {}
with open(word_embed, 'w') as f:
   len_remained_words = len(remained_words) 
   len_total = len(str(len_remained_words))
   for i, word in zip(xrange(len_remained_words), remained_words):
       prob_arr = word_prob_dict[word]
       pos_str = "W" + "".join(['0']*(len_total-len(str(i)))) + str(i)
       word_posSt_dict[word] = pos_str
       word_prob_str = pos_str + " "  + " ".join(str(prob) for prob in prob_arr)
       f.write(word_prob_str.encode("utf-8") + "\n")
       

#-----------
q_it_remained_list = []
sentence_list = []
for q_it in q_uniq:
    words_in_q_it = q_it.split(" ")
    save = True
    tmp = []
    for w in words_in_q_it:
        if w in word_posSt_dict:
            tmp.append(word_posSt_dict[w]) 
        else:
            save = False
    if save:
        sentence_list.append(tmp)
        q_it_remained_list.append(q_it)

true_len_q_it = len(sentence_list)
q_posStr_dict = {}
with open(questionName, "w") as f:
    len_total = len(str(true_len_q_it))
    for i, sentence in zip(xrange(true_len_q_it), sentence_list):
        words_str = " ".join(sentence)
        q_pos_str = "Q" + "".join(['0']*(len_total-len(str(i)))) + str(i)
        q_posStr_dict[q_it_remained_list[i]] = q_pos_str
        f.write((q_pos_str + "," + words_str).encode("utf-8") + "\n")

with open(traincsvName, "w") as f:
    f.write("label,q1,q2\n".encode("utf-8"))
    with open(input_file) as fr:
        for line in fr:
            _, Q0, Q1, label = line.strip().decode("utf-8", "ignore").split('\t')
            if (Q0 in q_posStr_dict) and (Q1 in q_posStr_dict):
                f.write(label + "," + q_posStr_dict[Q0] + "," + q_posStr_dict[Q1] + "\n")



         
