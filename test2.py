# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import os

source = open("data.txt","r",encoding='utf-8')
line = source.readlines()
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

result = [i-0.5 for i in sentimentslist]

import matplotlib.pyplot as plt
import numpy as np
# plt.plot(sentimentslist, 'k-')
plt.plot(result, 'k-')
plt.xlabel('Number')
plt.ylabel('Sentiment')
plt.title('Analysis of Sentiments')
plt.show()
