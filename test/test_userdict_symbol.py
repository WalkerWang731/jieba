# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")
import jieba
jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg
test_sent = "l+navtion+cf1 l-navtion-cf1 l-navtion-co1 l+navtion+cn2 l.navtion.cn2 l#navtion#cn2 l:navtion:cn2 l:navtion|cn2 l-navtion.co1 Edu Trust认证 Edu Trust认"
words = pseg.cut(test_sent)
for k,v in words:
    print(k,v)
w = jieba.cut(test_sent)
print(",".join(w))