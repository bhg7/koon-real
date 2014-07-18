# -*- coding:utf-8 -*-

import urllib
from bs4 import BeautifulSoup

basicurl = "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100#&date=2014-07-18 00:00:00&page=%(page)s"



for i in range(1,4):
    nowurl = basicurl + str(i)
    htmltext = urllib.urlopen(basicurl %{'page': i}).read()


    soup = BeautifulSoup(htmltext, from_encoding="utf-8")
    


    for each in soup.findAll('strong'):
        if each.findAll('strong',attrs={'class','n_ico n_pho_big'}):
            print " "
        else:
            print each.text
        











