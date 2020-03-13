# Language-Modelling
maximum likelihood estimates (MLEs) of all possible bigrams in corpus


Code (python)

Results

Reading txt file in python

with open('mothergoosecorpus.txt','r') as f:
	corpus = f.read() 
	print(corpus)

<s> peter piper picked a peck of pickled peppers </s>
<s> a peck of pickled peppers peter piper picked </s>
<s> if peter piper picked a peck of pickled peppers </s>
<s> where s the peck of pickled peppers peter piper picked </s>


Converting corpus into list of strings
words = corpus.split()        # split function converting whole corpus in to list of words so it will be eassy to handle
print(words[:])

<s>', 'peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers', '</s>', '<s>', 'a', 'peck', 'of', 'pickled', 'peppers', 'peter', 'piper', 'picked', '</s>', '<s>', 'if', 'peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers', '</s>', '<s>', 'where', 's', 'the', 'peck', 'of', 'pickled', 'peppers', 'peter', 'piper', 'picked', '</s>'

Compute the vocabulary of training corpus and print? 
	
# vocabulary of corpus
def vocabulary(words):
    vocabulary = []
    for i in words:
        if i not in vocabulary:
            vocabulary.append(i)
    print(vocabulary)

v = vocabulary(words)

['<s>', 'peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers', '</s>', 'if', 'where', 's', ‘the’]

2.In the above training corpus, calculate the probability of each unigram and print the 2 unigrams with the highest probability. 

Counting total number of token in corpus

N = len(words)
print(N)
 
#counting frequency of each type in corpus
from collections import Counter
a = dict(Counter(words))
print(a)

Probability of unigrams

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
    print( a[i][0] ,"=", probability)

    
# sorting probabilities of unigrames 
sorted(pro_uni,key=lambda l:l[1], reverse = True)


[['picked', 0.09302325581395349],
 ['piper', 0.09302325581395349],
 ['peck', 0.09302325581395349],
 ['<s>', 0.09302325581395349],
 ['peter', 0.09302325581395349],
 ['peppers', 0.09302325581395349],
 ['of', 0.09302325581395349],
 ['pickled', 0.09302325581395349],
 ['</s>', 0.09302325581395349],
 ['a', 0.06976744186046512],
 ['where', 0.023255813953488372],
 ['the', 0.023255813953488372],
 ['if', 0.023255813953488372],
 ['s', 0.023255813953488372]]


3. Construct a probability matrix containing the maximum likelihood estimates (MLEs) of all possible bigrams and print it out 

# forming bigram model as list
bigram = [[] for i in range(N)]
for i in range(N):
    if i+1 < N:   
        bigram[i].append( words[i] )   # storing word in first columb of pro_uni list
        bigram[i].append( words[i+1] )
    
#print (bigram)

for i in bigram:
       print(i)

# counting frequency of each bigram
bigram_fre = []
for i in bigram:
    temp = [i, bigram.count(i)]
    if temp not in bigram_fre:
        bigram_fre.append(temp)

b1 = sorted(bigram_fre,key=lambda l:l[1], reverse = True)

print(b1)

[[['peter', 'piper'], 4], [['piper', 'picked'], 4], [['peck', 'of'], 4], [['of', 'pickled'], 4], [['pickled', 'peppers'], 4], [['a', 'peck'], 3], [['</s>', '<s>'], 3], [['picked', 'a'], 2], [['peppers', '</s>'], 2], [['peppers', 'peter'], 2], [['picked', '</s>'], 2], [['<s>', 'peter'], 1], [['<s>', 'a'], 1], [['<s>', 'if'], 1], [['if', 'peter'], 1], [['<s>', 'where'], 1], [['where', 's'], 1], [['s', 'the'], 1], [['the', 'peck'], 1], [[], 1]]


#finding probability of bigram

for i in range(len(b1)-1):
    num = b1[i][1]
    den = words.count(b1[i][0][0])
    
    bigram_pro = num/den
    
    print(b1[i], '=', bigram_pro)

[['peter', 'piper'], 4] = 1.0
[['piper', 'picked'], 4] = 1.0
[['peck', 'of'], 4] = 1.0
[['of', 'pickled'], 4] = 1.0
[['pickled', 'peppers'], 4] = 1.0
[['a', 'peck'], 3] = 1.0
[['</s>', '<s>'], 3] = 0.75
[['picked', 'a'], 2] = 0.5
[['peppers', '</s>'], 2] = 0.5
[['peppers', 'peter'], 2] = 0.5
[['picked', '</s>'], 2] = 0.5
[['<s>', 'peter'], 1] = 0.25
[['<s>', 'a'], 1] = 0.25
[['<s>', 'if'], 1] = 0.25
[['if', 'peter'], 1] = 1.0
[['<s>', 'where'], 1] = 0.25
[['where', 's'], 1] = 1.0
[['s', 'the'], 1] = 1.0
[['the', 'peck'], 1] = 1.0

4. What is the most frequent bigram in this corpus 

bigram_fre = []
for i in bigram:
    temp = [i, bigram.count(i)]
    if temp not in bigram_fre:
        bigram_fre.append(temp)

sorted(bigram_fre,key=lambda l:l[1], reverse = True)
    
[[['peter', 'piper'], 4],
 [['piper', 'picked'], 4],
 [['peck', 'of'], 4],
 [['of', 'pickled'], 4],
 [['pickled', 'peppers'], 4],
 [['a', 'peck'], 3],
 [['</s>', '<s>'], 3],
 [['picked', 'a'], 2],
 [['peppers', '</s>'], 2],
 [['peppers', 'peter'], 2],
 [['picked', '</s>'], 2],
 [['<s>', 'peter'], 1],
 [['<s>', 'a'], 1],
 [['<s>', 'if'], 1],
 [['if', 'peter'], 1],
 [['<s>', 'where'], 1],
 [['where', 's'], 1],
 [['s', 'the'], 1],
 [['the', 'peck'], 1],
 [[], 1]]


5.Construct a probability matrix containing the Laplace smoothed estimates of all possible bigrams and print it out. 
For only bigrams present in corpus
# vocabilary of words 
vocabulary = []
for i in words:
    if i not in vocabulary:
        vocabulary.append(i)
v = (len(vocabulary)-1)

# bigram probability with laplace smoothing 
for i in range(len(b1)-1):
    num = b1[i][1]
    den = words.count(b1[i][0][0])
    
    bigram_pro_lap = (num+1)/(den +v)
    
    print(b1[i], '=', bigram_pro_lap)
[['peter', 'piper'], 4] = 0.29411764705882354
[['piper', 'picked'], 4] = 0.29411764705882354
[['peck', 'of'], 4] = 0.29411764705882354
[['of', 'pickled'], 4] = 0.29411764705882354
[['pickled', 'peppers'], 4] = 0.29411764705882354
[['a', 'peck'], 3] = 0.25
[['</s>', '<s>'], 3] = 0.23529411764705882
[['picked', 'a'], 2] = 0.17647058823529413
[['peppers', '</s>'], 2] = 0.17647058823529413
[['peppers', 'peter'], 2] = 0.17647058823529413
[['picked', '</s>'], 2] = 0.17647058823529413
[['<s>', 'peter'], 1] = 0.11764705882352941
[['<s>', 'a'], 1] = 0.11764705882352941
[['<s>', 'if'], 1] = 0.11764705882352941
[['if', 'peter'], 1] = 0.14285714285714285
[['<s>', 'where'], 1] = 0.11764705882352941
[['where', 's'], 1] = 0.14285714285714285
[['s', 'the'], 1] = 0.14285714285714285
[['the', 'peck'], 1] = 0.14285714285714285

For all possible bigrams 
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


6. What is the probability of unseen bigrams?
# all possible bigrams
 
all_bigram = []
for i in words:
    for j in range(N):
        temp =[i , words[j]] 
        if temp not in all_bigram:
            all_bigram.append(temp)
    
for i in all_bigram:
       print(i)

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
    if b_all[i] not in seen_bigram_lap:
        num = b_all[i][1]
        den = words.count(b_all[i][0][0])
        bigram_pro_lap = 1/(den +v)
        temp =[b_all[i], bigram_pro_lap]
        unseen_bigram_lap.append(temp)

for i in unseen_bigram_lap:
    print(i)

Total= 177 unseen bigrams
[[['<s>', '<s>'], 1], 0.058823529411764705]
[[['<s>', 'piper'], 1], 0.058823529411764705]
[[['<s>', 'picked'], 1], 0.058823529411764705]
[[['<s>', 'peck'], 1], 0.058823529411764705]
[[['<s>', 'of'], 1], 0.058823529411764705]
[[['<s>', 'pickled'], 1], 0.058823529411764705]
[[['<s>', 'peppers'], 1], 0.058823529411764705]
[[['<s>', '</s>'], 1], 0.058823529411764705]
[[['<s>', 's'], 1], 0.058823529411764705]
[[['<s>', 'the'], 1], 0.058823529411764705]
[[['peter', '<s>'], 1], 0.058823529411764705]
[[['peter', 'peter'], 1], 0.058823529411764705]
[[['peter', 'piper'], 1], 0.058823529411764705]
[[['peter', 'picked'], 1], 0.058823529411764705]
[[['peter', 'a'], 1], 0.058823529411764705]
[[['peter', 'peck'], 1], 0.058823529411764705]
[[['peter', 'of'], 1], 0.058823529411764705]
[[['peter', 'pickled'], 1], 0.058823529411764705]
[[['peter', 'peppers'], 1], 0.058823529411764705]
[[['peter', '</s>'], 1], 0.058823529411764705]
[[['peter', 'if'], 1], 0.058823529411764705]
[[['peter', 'where'], 1], 0.058823529411764705]
	. . .  
	. . . 
	. . .
	. . . 
	. . .

7.count-of-count table for bigram 

count_table=[]
count_count = []
for i in all_bigram: 
        count_table.append(bigram.count(i))
        
bigram_count= []
for i in range(len(all_bigram)):
    temp = [all_bigram[i],count_table[i]]
    bigram_count.append(temp)
print(bigram_count)    

[[['<s>', '<s>'], 1], [['<s>', 'peter'], 1], [['<s>', 'piper'], 1], [['<s>', 'picked'], 1], [['<s>', 'a'], 1], [['<s>', 'peck'], 1], [['<s>', 'of'], 1], [['<s>', 'pickled'], 1], [['<s>', 'peppers'], 0], [['<s>', '</s>'], 0], [['<s>', 'if'], 1], [['<s>', 'where'], 1], [['<s>', 's'], 0], [['<s>', 'the'], 0], [['peter', '<s>'], 1], [['peter', 'peter'], 1], [['peter', 'piper'], 4], [['peter', 'picked'], 1], [['peter', 'a'], 1], [['peter', 'peck'], 1], [['peter', 'of'], 1], [['peter', 'pickled'], 1], [['peter', 'peppers'], 0], [['peter', '</s>'], 0], [['peter', 'if'], 0], [['peter', 'where'], 0], [['peter', 's'], 0], [['peter', 'the'], 0], [['piper', '<s>'], 1], [['piper', 'peter'], 1], [['piper', 'piper'], 1], [['piper', 'picked'], 4], [['piper', 'a'], 1], [['piper', 'peck'], 1], [['piper', 'of'], 1], [['piper', 'pickled'], 1], [['piper', 'peppers'], 0], [['piper', '</s>'], 0], [['piper', 'if'], 0], [['piper', 'where'], 0], [['piper', 's'], 0], [['piper', 'the'], 0], [['picked', '<s>'], 1], [['picked', 'peter'], 1], [['picked', 'piper'], 1], [['picked', 'picked'], 1], [['picked', 'a'], 2], [['picked', 'peck'], 1], [['picked', 'of'], 1], [['picked', 'pickled'], 1], [['picked', 'peppers'], 0], [['picked', '</s>'], 2], [['picked', 'if'], 0], [['picked', 'where'], 0], [['picked', 's'], 0], [['picked', 'the'], 0], [['a', '<s>'], 1], [['a', 'peter'], 1], [['a', 'piper'], 1], [['a', 'picked'], 1], [['a', 'a'], 1], [['a', 'peck'], 3], [['a', 'of'], 1], [['a', 'pickled'], 1], [['a', 'peppers'], 0], [['a', '</s>'], 0], [['a', 'if'], 0], [['a', 'where'], 0], [['a', 's'], 0], [['a', 'the'], 0], [['peck', '<s>'], 1], [['peck', 'peter'], 1], [['peck', 'piper'], 1], [['peck', 'picked'], 1], [['peck', 'a'], 1], [['peck', 'peck'], 1], [['peck', 'of'], 4], [['peck', 'pickled'], 1], [['peck', 'peppers'], 0], [['peck', '</s>'], 0], [['peck', 'if'], 0], [['peck', 'where'], 0], [['peck', 's'], 0], [['peck', 'the'], 0], [['of', '<s>'], 1], [['of', 'peter'], 1], [['of', 'piper'], 1], [['of', 'picked'], 1], [['of', 'a'], 1], [['of', 'peck'], 1], [['of', 'of'], 1], [['of', 'pickled'], 4], [['of', 'peppers'], 0], [['of', '</s>'], 0], [['of', 'if'], 0], [['of', 'where'], 0], [['of', 's'], 0], [['of', 'the'], 0], [['pickled', '<s>'], 1], [['pickled', 'peter'], 1], [['pickled', 'piper'], 1], [['pickled', 'picked'], 1], [['pickled', 'a'], 1], [['pickled', 'peck'], 1], [['pickled', 'of'], 1], [['pickled', 'pickled'], 1], [['pickled', 'peppers'], 4], [['pickled', '</s>'], 0], [['pickled', 'if'], 0], [['pickled', 'where'], 0], [['pickled', 's'], 0], [['pickled', 'the'], 0], [['peppers', '<s>'], 1], [['peppers', 'peter'], 2], [['peppers', 'piper'], 1], [['peppers', 'picked'], 1], [['peppers', 'a'], 1], [['peppers', 'peck'], 1], [['peppers', 'of'], 1], [['peppers', 'pickled'], 1], [['peppers', 'peppers'], 0], [['peppers', '</s>'], 2], [['peppers', 'if'], 0], [['peppers', 'where'], 0], [['peppers', 's'], 0], [['peppers', 'the'], 0], [['</s>', '<s>'], 3], [['</s>', 'peter'], 1], [['</s>', 'piper'], 1], [['</s>', 'picked'], 1], [['</s>', 'a'], 1], [['</s>', 'peck'], 1], [['</s>', 'of'], 1], [['</s>', 'pickled'], 1], [['</s>', 'peppers'], 0], [['</s>', '</s>'], 0], [['</s>', 'if'], 0], [['</s>', 'where'], 0], [['</s>', 's'], 0], [['</s>', 'the'], 0], [['if', '<s>'], 1], [['if', 'peter'], 1], [['if', 'piper'], 1], [['if', 'picked'], 1], [['if', 'a'], 1], [['if', 'peck'], 1], [['if', 'of'], 1], [['if', 'pickled'], 1], [['if', 'peppers'], 0], [['if', '</s>'], 0], [['if', 'if'], 0], [['if', 'where'], 0], [['if', 's'], 0], [['if', 'the'], 0], [['where', '<s>'], 1], [['where', 'peter'], 1], [['where', 'piper'], 1], [['where', 'picked'], 1], [['where', 'a'], 1], [['where', 'peck'], 1], [['where', 'of'], 1], [['where', 'pickled'], 1], [['where', 'peppers'], 0], [['where', '</s>'], 0], [['where', 'if'], 0], [['where', 'where'], 0], [['where', 's'], 1], [['where', 'the'], 0], [['s', '<s>'], 1], [['s', 'peter'], 1], [['s', 'piper'], 1], [['s', 'picked'], 1], [['s', 'a'], 1], [['s', 'peck'], 1], [['s', 'of'], 1], [['s', 'pickled'], 1], [['s', 'peppers'], 0], [['s', '</s>'], 0], [['s', 'if'], 0], [['s', 'where'], 0], [['s', 's'], 0], [['s', 'the'], 1], [['the', '<s>'], 1], [['the', 'peter'], 1], [['the', 'piper'], 1], [['the', 'picked'], 1], [['the', 'a'], 1], [['the', 'peck'], 1], [['the', 'of'], 1], [['the', 'pickled'], 1], [['the', 'peppers'], 0], [['the', '</s>'], 0], [['the', 'if'], 0], [['the', 'where'], 0], [['the', 's'], 0], [['the', 'the'], 0]]

j=0
for i in range(0,(len(all_bigram)+1)):
    m = [j, count_table.count(j)]
    count_count.append(m)
    j=j+1
print(count_count)

[[0, 77], [1, 108], [2, 4], [3, 2], [4, 5], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0], [22, 0], [23, 0], [24, 0], [25, 0], [26, 0], [27, 0], [28, 0], [29, 0], [30, 0], [31, 0], [32, 0], [33, 0], [34, 0], [35, 0], [36, 0], [37, 0], [38, 0], [39, 0], [40, 0], [41, 0], [42, 0], [43, 0], [44, 0], [45, 0], [46, 0], [47, 0], [48, 0], [49, 0], [50, 0], [51, 0], [52, 0], [53, 0], [54, 0], [55, 0], [56, 0], [57, 0], [58, 0], [59, 0], [60, 0], [61, 0], [62, 0], [63, 0], [64, 0], [65, 0], [66, 0], [67, 0], [68, 0], [69, 0], [70, 0], [71, 0], [72, 0], [73, 0], [74, 0], [75, 0], [76, 0], [77, 0], [78, 0], [79, 0], [80, 0], [81, 0], [82, 0], [83, 0], [84, 0], [85, 0], [86, 0], [87, 0], [88, 0], [89, 0], [90, 0], [91, 0], [92, 0], [93, 0], [94, 0], [95, 0], [96, 0], [97, 0], [98, 0], [99, 0], [100, 0], [101, 0], [102, 0], [103, 0], [104, 0], [105, 0], [106, 0], [107, 0], [108, 0], [109, 0], [110, 0], [111, 0], [112, 0], [113, 0], [114, 0], [115, 0], [116, 0], [117, 0], [118, 0], [119, 0], [120, 0], [121, 0], [122, 0], [123, 0], [124, 0], [125, 0], [126, 0], [127, 0], [128, 0], [129, 0], [130, 0], [131, 0], [132, 0], [133, 0], [134, 0], [135, 0], [136, 0], [137, 0], [138, 0], [139, 0], [140, 0], [141, 0], [142, 0], [143, 0], [144, 0], [145, 0], [146, 0], [147, 0], [148, 0], [149, 0], [150, 0], [151, 0], [152, 0], [153, 0], [154, 0], [155, 0], [156, 0], [157, 0], [158, 0], [159, 0], [160, 0], [161, 0], [162, 0], [163, 0], [164, 0], [165, 0], [166, 0], [167, 0], [168, 0], [169, 0], [170, 0], [171, 0], [172, 0], [173, 0], [174, 0], [175, 0], [176, 0], [177, 0], [178, 0], [179, 0], [180, 0], [181, 0], [182, 0], [183, 0], [184, 0], [185, 0], [186, 0], [187, 0], [188, 0], [189, 0], [190, 0], [191, 0], [192, 0], [193, 0], [194, 0], [195, 0], [196, 0]]


8.count-of-count table smoothing
In most of the cases most of the cell in original count table will be zeros, so most of the time our bigram model assigns probability zero and probability zero means event will never occur but in reality thats not the case, to overcome this problem we can convert these zeros into some value as we do in Laplace smoothing, this will help us to get some nonzero probability for zero count bigrams models pointing to the fact that the zero count bigrams will occur in nature.  


9.<s> peter piper picked a pickled pepper </s>
a. MLE bigram model

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

Probability of sentence using MLE = 0.0
['<s>', 'peter']
['peter', 'piper']
['piper', 'picked']
['picked', 'a']
['a', 'pickled']
['pickled', 'peppers']
['peppers', '</s>']
[]
[[['<s>', 'peter'], 1], [['peter', 'piper'], 4], [['piper', 'picked'], 4], [['picked', 'a'], 2], [['a', 'pickled'], 0], [['pickled', 'peppers'], 4], [['peppers', '</s>'], 2], [[], 1]]
[[[['<s>', 'peter'], 1], 0.25],
 [[['peter', 'piper'], 4], 1.0],
 [[['piper', 'picked'], 4], 1.0],
 [[['picked', 'a'], 2], 0.5],
 [[['a', 'pickled'], 0], 0.0],
 [[['pickled', 'peppers'], 4], 1.0],
 [[['peppers', '</s>'], 2], 0.5]]
[0.25, 1.0, 1.0, 0.5, 0.0, 1.0, 0.5]

Out[77]:
0.0


b. Laplace smoothed bigram model
# laplace smoothed probability of bigram model
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
Probability of sentence using laplace smoothed model = 5.825980238523608e-06


['<s>', 'peter']
['peter', 'piper']
['piper', 'picked']
['picked', 'a']
['a', 'pickled']
['pickled', 'peppers']
['peppers', '</s>']
[]
[[['<s>', 'peter'], 1], [['peter', 'piper'], 4], [['piper', 'picked'], 4], [['picked', 'a'], 2], [['a', 'pickled'], 0], [['pickled', 'peppers'], 4], [['peppers', '</s>'], 2], [[], 1]]
[[[['<s>', 'peter'], 1], 0.11764705882352941],
 [[['peter', 'piper'], 4], 0.29411764705882354],
 [[['piper', 'picked'], 4], 0.29411764705882354],
 [[['picked', 'a'], 2], 0.17647058823529413],
 [[['a', 'pickled'], 0], 0.0625],
 [[['pickled', 'peppers'], 4], 0.29411764705882354],
 [[['peppers', '</s>'], 2], 0.17647058823529413]]
[0.11764705882352941, 0.29411764705882354, 0.29411764705882354, 0.17647058823529413, 0.0625, 0.29411764705882354, 0.17647058823529413]
Out[78]:
5.825980238523608e-06

