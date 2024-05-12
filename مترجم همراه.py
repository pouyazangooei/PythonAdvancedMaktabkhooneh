numb = int(input())
full_dic = dict()
for i in range(0,numb):
    translations = str(input())
    trans_list = translations.split()
    for j in range(1,4):
        full_dic[trans_list[j]] = trans_list[0]
sentence = str(input())
divided_sentence = sentence.split()
tranlated_sentence = []
for k in range(0,len(divided_sentence)):
    temp = divided_sentence[k]
    if temp in full_dic:
        temp = full_dic[temp]
        tranlated_sentence.append(temp)
    else:
        tranlated_sentence.append(temp)
print(' '.join(tranlated_sentence))
