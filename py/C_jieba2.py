
# coding: utf-8

# # jieba分词《二》

# ## Part 1. 词频统计、降序排序
# 

# In[1]:

import jieba


# In[2]:

article = open("C_jieba_demo.txt", "r").read()
words = jieba.cut(article, cut_all = False)
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key = lambda x: x[1], reverse = True)

max_number = int(raw_input(u"需要前多少位高频词？ "))

for word, freq in freq_word[: max_number]:
    print word, freq


# %^&**( argly停用词

# ## Part 2. 人工去停用词
# 
# 标点符号、虚词、连词不在统计范围内。

# In[3]:

stopwords = []
for word in open("D:\\python_workspace\\toolkits\\stopword1.txt","r"):
    stopwords.append(word.strip())


# In[4]:

article = open("C_jieba_demo.txt", "r").read()
words = jieba.cut(article, cut_all = False)


# In[5]:

stayed_line = ""
for word in words:
    if word.encode("utf-8") not in stopwords:
        stayed_line += word + " "
print stayed_line


# ## Part 3. 合并同义词

# * 将同义词列举出来，按下Tab键分隔，把第一个词作为需要显示的词语，后面的词语作为要替代的同义词，一系列同义词放在一行。
# * 这里，“北京”、“首都”、“京城”、“北平城”、“故都”为同义词。

# In[6]:

combine_dict = {}

for line in open("C_jieba_tongyici.txt", "r"):
    seperate_word = line.strip().split("\t")
    num = len(seperate_word)
    for i in range(1, num):
        combine_dict[seperate_word[i]] = seperate_word[0]


# In[7]:

combine_dict


# In[8]:

jieba.suggest_freq("北平城", tune = True)
seg_list = jieba.cut("北京是中国的首都，京城的景色非常优美，就像当年的北平城，我爱这故都的一草一木。", cut_all = False)
f = ",".join(seg_list)
result = open("output.txt", "w")
result.write(f.encode("utf-8"))
result.close()

for line in open("output.txt", "r"):
    line_1 = line.split(",")

final_sentence = ""
for word in line_1:
    if word in combine_dict:
        word = combine_dict[word]
        final_sentence += word
    else:
        final_sentence += word
print final_sentence


# In[ ]:




# ## Part 4. 词语提及率

# 主要步骤：分词——过滤停用词（略）——替代同义词——计算词语在文本中出现的概率。

# ## Part 5. 按词性提取
# 

# In[9]:

import jieba.posseg as pseg
word = pseg.cut("李晨好帅，又能力超强，是“大黑牛”，也是一个能力者，还是队里贴心的晨妈妈。")
for w in word:
    if w.flag in ["n", "v", "x"]:
        print w.word, w.flag


# In[ ]:



