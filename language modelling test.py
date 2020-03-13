words = []
vocab = []
uni_prob = {}
uni_prob_list = []
bi_list = []
bi_prob = []
temp_bi = []
bi_prob_lap = []
count_table = []
count_count = []
temp_count = []
with open("mothergoosecorpus.txt","r") as f:
    i=0
    j=0
    lines = f.readlines()
    for line in lines:
        tokens = line.split()
        words.extend(tokens)
    len_uni = len(words) - words.count('<s>') - words.count('</s>')
    for word in words:
        if word not in vocab and word != '<s>' and word != '</s>':
            vocab.append(word)
        if word == '<s>' or word == '</s>':
            {}
        else:
            uni_prob[word] = words.count(word) / len_uni
        if i != len(words)-1:
            if words[i] =='</s>':
                    i=i+1
            else:
                bi = [words[i],words[i+1]]
                bi_list.append(bi)
                i=i+1
    #print("VOCABULARY :", vocab,"\n")
    for key , value in uni_prob.items():
        temp = [key, value]
        uni_prob_list.append(temp)
    uni_prob_list.sort(key = lambda x :x[1], reverse= True)
    #print(uni_prob_list[0:2])
    for i in bi_list:
        if i not in temp_bi:
            temp_bi.append(i)
            temp1 = [i,bi_list.count(i)/ words.count(i[0])]
            bi_prob.append(temp1)
    #print(bi_prob)
    bi_prob.sort(key =lambda x :x[:][1], reverse = True)
    #print(bi_prob[0])
    for i in temp_bi:
        temp2 = [i , (bi_list.count(i)+1) / (words.count(i[0]) + len(vocab))]
        bi_prob_lap.append(temp2)
    #print(bi_prob_lap)
    for i in temp_bi: 
        count_table.append(bi_list.count(i))
    j=0
    for i in range(0,(len(temp_bi)+1)):
        m = [j, count_table.count(j)]
        count_count.append(m)
        j=j+1
    #print(count_count)
    # when a zero count of count is encountered, it causes the probability of the previous event to be zero even if it had some probability to start with. Seen events could be counted as unseen, hence smoothing of count of counts table is necessary.
     
