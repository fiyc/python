#-*- coding: UTF-8 -*-

import sys
import os
import re
sys.path.append(os.getcwd())

from library import http_help

def hander(html):
    if(html == '' or html == None):
        return None

    result = {}
    titles = re.findall('<a href="(.*?)" title="(.*?)" strategy="BlogCommendFromBaidu',html)

    fs = open('temp.html', 'a+')
    fs.write(html)
    fs.close()
    return html


param = {
    'url': "https://blog.csdn.net/u013858731/article/details/54971762",
    'retry': 3,
    'encode':'utf-8'
}

result = http_help.analysis(param, None, hander)
print(result)