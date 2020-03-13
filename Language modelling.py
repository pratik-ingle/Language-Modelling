
# coding: utf-8

# Reading file in python

# In[160]:

with open('mothergoosecorpus.txt','r') as f:
	corpus = f.read() 
	print(corpus)


# In[161]:

words = corpus.split()        # split function converting whole corpus in to list of words so it will be eassy to handle
print(words[:])


# In[162]:

# vocabulary of corpus
def vocabulary(words):
    vocabulary = []
    for i in words:
        if i not in vocabulary:
            vocabulary.append(i)
    print(vocabulary)


# In[163]:

v = vocabulary(words)


# In[164]:

N = len(words)
print(N)


# In[165]:

#counting frequency of each type in corpus

from collections import Counter
a = dict(Counter(words))
print(a)


# In[166]:

# probability of unigrams
import collections
types =  collections.Counter(words)
#print(types)

# converting dictionary into two dimentional array
a = []
for value in types.items() :
    a.append(value)
print(a)

#finding probability and printing 
pro_uni = [[] for i in range(14)]
for i in range(14):
    probability = a[i][1]/N
    pro_uni[i].append(a[i][0])   # storing word in first columb of pro_uni list
    pro_uni[i].append(probability)  # storing word in second columb on pro_uni list
    #print( a[i][0] ,"=", probability)
    
# sorting probabilities of unigrames 
sorted(pro_uni,key=lambda l:l[1], reverse = True)


# In[167]:

# bigram probability method 
# most frequent bigram in model

# forming bigram model as list
bigram = [[] for i in range(N)]
for i in range(N):
    if i+1 < N:   
        bigram[i].append( words[i] )   # storing word in first columb of pro_uni list
        bigram[i].append( words[i+1] )
    
#print (bigram)

print(bigram)


# counting frequency of each bigram
bigram_fre = []
for i in bigram:
    temp = [i, bigram.count(i)]
    if temp not in bigram_fre:
        bigram_fre.append(temp)

b1 = sorted(bigram_fre,key=lambda l:l[1], reverse = True)

print(b1)


# In[168]:

#finding probability of bigram

for i in range(len(b1)-1):
    num = b1[i][1]
    den = words.count(b1[i][0][0])
    
    bigram_pro = num/den
    
    print(b1[i], '=', bigram_pro)


# In[169]:

# probability matrix of bigram using laplace smoothing

# vocabilary of words 
vocabulary = []
for i in words:
    if i not in vocabulary:
        vocabulary.append(i)
v = (len(vocabulary)-1)

# bigram probability with laplace smoothing 
seen_bigram_lap = []
for i in range(len(b1)-1):
    num = b1[i][1]
    den = words.count(b1[i][0][0])
    
    bigram_pro_lap = (num+1)/(den +v)
    tem = [b1[i], bigram_pro_lap]
    seen_bigram_lap.append(tem)

for i in seen_bigram_lap:
    print(i)



# In[170]:

# vocabulary of words
vocabulary = []
for i in words:
    if i not in vocabulary:
        vocabulary.append(i)
print(vocabulary)


# In[171]:

len(vocabulary)


# In[172]:

# all possible bigrams
 
all_bigram = []
n = len(vocabulary)
for i in vocabulary:
    for j in range(n):
        temp =[i , vocabulary[j]] 
        if temp not in all_bigram:
            all_bigram.append(temp)
    
#for i in all_bigram:
 #      print(i)

bigram_count =[]
for i in range(len(bigram)):   
        x = bigram[i]
        #x1= bigram[1][0]
        temp = [bigram[i], bigram.count(x)] #bigram.count(x)/words.count(x1)]
        if temp not in bigram_count:
            bigram_count.append(temp)
   
        else:
           {}
#print(bigram_count)


# In[173]:

# frequency of all bigrams
bigram_fre_all = []
for i in all_bigram:
    temp = [i, all_bigram.count(i)]
    if temp not in bigram_fre:
        bigram_fre_all.append(temp)

b_all = sorted(bigram_fre_all,key=lambda l:l[1], reverse = True)

#laplace smoothing of unseen bigrams
unseen_bigram_lap = []
for i in range(len(b_all)-1):
        num = b_all[i][1]
        den = words.count(b_all[i][0][0])
        bigram_pro_lap = 1/(den +v)
        temp =[b_all[i], bigram_pro_lap]
        if temp not in unseen_bigram_lap:
            unseen_bigram_lap.append(temp)


for i in unseen_bigram_lap:
    print(i)


# In[174]:

import numpy as np


# In[175]:

import pprint


# In[176]:

# MLE probability of bigram model of sentence
sen = ['<s>', 'peter', 'piper', 'picked', 'a', 'pickled', 'peppers', '</s>']
bigram1 = [[] for i in range(N)]
for i in range(N):
    if i+1 < N:   
        bigram1[i].append( sen[i] )   # storing word in first columb of pro_uni list
        bigram1[i].append( sen[i+1] )
    
#print (bigram)
nb = len(bigram1)

for i in bigram1:
       print(i)

# counting frequency of each bigram
sen_bigram_fre = []
for i in bigram1:
    temp = [i, bigram.count(i)]
    if temp not in sen_bigram_fre:
        sen_bigram_fre.append(temp)

print(sen_bigram_fre)

z = len(sen_bigram_fre)
#finding probability of bigram
sen_bi_pro = []
for i in range(z-1):
    num = sen_bigram_fre[i][1]
    den = words.count(sen_bigram_fre[i][0][0])
    
    sen_pro = num/den
    
    tem=[sen_bigram_fre[i],sen_pro]
    sen_bi_pro.append(tem)

pprint.pprint(sen_bi_pro)

multi_pro=[]
for i in range(z-1):
    temp=sen_bi_pro[i][1]
    multi_pro.append(temp)

print(multi_pro)

from functools import reduce
reduce(lambda x, y: x*y, multi_pro)


# In[177]:

# laplace smoothed probability of bigram model sentence
sen = ['<s>', 'peter', 'piper', 'picked', 'a', 'pickled', 'peppers', '</s>']
bigram1 = [[] for i in range(N)]
for i in range(N):
    if i+1 < N:   
        bigram1[i].append( sen[i] )   # storing word in first columb of pro_uni list
        bigram1[i].append( sen[i+1] )
    
#print (bigram)
nb = len(bigram1)

for i in bigram1:
       print(i)

# counting frequency of each bigram
sen_bigram_fre = []
for i in bigram1:
    temp = [i, bigram.count(i)]
    if temp not in sen_bigram_fre:
        sen_bigram_fre.append(temp)

print(sen_bigram_fre)


z = len(sen_bigram_fre)
#finding laplace smoothed probability of bigram
v = (len(vocabulary)-1)

sen_bi_pro = []
for i in range(z-1):
    num = sen_bigram_fre[i][1]
    den = words.count(sen_bigram_fre[i][0][0])
    
    sen_pro = (num+1)/(den+v)
    
    tem=[sen_bigram_fre[i],sen_pro]
    sen_bi_pro.append(tem)

pprint.pprint(sen_bi_pro)

multi_pro=[]
for i in range(z-1):
    temp=sen_bi_pro[i][1]
    multi_pro.append(temp)

print(multi_pro)

from functools import reduce
reduce(lambda x, y: x*y, multi_pro)


# In[178]:

# count of count table
count_table=[]
count_count = []
for i in all_bigram: 
        count_table.append(bigram.count(i))
        
bigram_count= []
for i in range(len(all_bigram)):
    temp = [all_bigram[i],count_table[i]]
    bigram_count.append(temp)
print(bigram_count)    

j=0
for i in range(0,(len(all_bigram)+1)):
    m = [j, count_table.count(j)]
    count_count.append(m)
    j=j+1
print(count_count)

