
# coding: utf-8

# In[11]:


import jieba

#設定繁體中文詞庫(放在C槽使用者資料夾，自行建立的DICTIONARY裡)
jieba.set_dictionary('dictionary/dict.txt.big.txt')


sentence = "我到台中教育大學就讀碩士"

breakword = jieba.cut(sentence, cut_all=False)
print("預設模式:"+'|'.join(breakword))

breakword = jieba.cut(sentence, cut_all=True)
print("全文模式:"+'|'.join(breakword))

breakword = jieba.cut_for_search(sentence)
print("搜尋引勤:"+'|'.join(breakword))


# In[18]:


from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from collections import Counter


text = open('news.txt',"r",encoding="utf-8").read() #讀文字資料

jieba.set_dictionary('dictionary/dict.txt.big.txt')
with open('dictionary/stopword_cloud.txt','r',encoding='utf-8-sig') as f:
    stops = f.read().split('\n')
terms = []
for t in jieba.cut(text, cut_all=False):
    if t not in stops:
        terms.append(t)
diction = Counter(terms)

#可列印統計輛
#print(diction)

font = "C:\\windows\Fonts\\simsun.ttc"

mask = np.array(Image.open("heart.png"))

wordcloud = WordCloud(background_color="white",mask=mask, font_path=font)
wordcloud.generate_from_frequencies(diction) #產生文字雲

#產生圖片
plt.figure(figsize=(6,6))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#wordcloud.to file("mews Wordcloud.png") #存檔

