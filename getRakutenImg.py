#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/06/06 13:00
# @Author  : ziji
# @Site    : 
# @File    : getRakutenImg.py
# @Software: PyCharm
# @license : Copyright(C), TIHTIH CO., Ltd
# @Contact : chinss@tihtih.co.jp
# @Desc    : 楽天ショップからIMGを取得する。

import requests
from bs4 import BeautifulSoup
import re
import urllib
import os

root = "D:/python/pj/img/ydbs/"
url = "https://item.rakuten.co.jp/teddyshop/c/0000000279/"

try:
    if not os.path.exists(root):
        os.mkdir(root)
except:
    print("NG")

def getImg(url, root ):
    headers = {"User-Agent": "Mozilla/5.0"}
    req = requests.get(url, headers)
    req.raise_for_status()
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text, "html.parser")
    imgList = soup.find_all('img')
    lenth = len(imgList)
    imgCount = 0
    for s in range(lenth):
        u = imgList[s].attrs['src']
        imgre = re.compile(r'^http:*.*\d$')
        imgArray = imgre.findall(u)

        for i in imgArray:
            if i is not None:
                print(i)
                f = open(root + str(imgCount) + ".jpg", 'wb')
                f.write((urllib.request.urlopen(i)).read())
                f.close()
                imgCount += 1
    print("IMGを取得しました。")

getImg(url, root)