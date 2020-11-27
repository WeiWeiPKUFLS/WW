#! python3
# encoding: utf-8
import bs4
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("/Users/weiwei/Documents/pilotstudy29.html"))
import sys
non_bmp_map = dict.fromkeys(range(0x10000,sys.maxunicode + 1),0xfffd)
titles = []
lenstitle = []
maintexts = []
keywords = []
lenstext = []

#标题关键词和描述
title = soup.title.string
titles.append(title)
lenstitle.append(len(title))

keyword = soup.find(attrs={"name":"keywords"})['content']
keywords.append(keyword)
maintext = soup.find_all("p", class_="text")
for m in maintext:
    main = m.text.strip()
    print(main)
    print(len(main))
    lenstext.append(len(main))
    maintexts.append(main)
    
#遍历提取评论者名称和评论
usernames = []
remarks = []
numberofwords = []
identities = []

a = soup.find_all('span', class_="username")
for i in a:
    name = i.text
    nam = name.translate(non_bmp_map)
    print (nam)
    usernames.append(nam)
'''————————————————————————————————————————————————————'''
'''获取职业称号'''
bests=soup.select('p.user')
for best in bests:
    getbest = best.select('span.best')
    getb = str(getbest)
    print(getb)
    identities.append(getb)
    
'''————————————————————————————————————————————————————'''
b = soup.find_all('div',class_="text")
for j in b:
    remark = j.text
    rem = remark.translate(non_bmp_map)
    print(rem)
    print(len(rem))
    remarks.append(rem)
    numberofword = len(rem)
    numberofwords.append(numberofword)

print(usernames)
print(remarks)
print(numberofwords)
print(identities)

import pandas as pd
test = pd.DataFrame({'用户名':usernames,'用户身份':identities,'评论':remarks, '评论字数':numberofwords})
test2 = pd.DataFrame({'标题':titles,'标题长度':lenstitle,'正文':maintexts, '关键词':keywords,'正文长度':lenstext})
test.to_csv('pilotstudy29.csv',index=False,encoding='utf_8_sig')
test2.to_csv('pilotstudy29maintext.csv',index=False,encoding='utf_8_sig')

    
