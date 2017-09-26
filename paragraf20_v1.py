# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:46:20 2017

@author: ntyss
"""

#%% Import af pakker
import requests
from bs4 import BeautifulSoup
import time
import re

data = []
for i in [100]:
    time.sleep(2)
    d = {}
    Url = 'http://ft.dk/samling/20151/spoergsmaal/S' + str(i) + '/index.htm'
    text = requests.get(Url).text
    soup = BeautifulSoup(text, "lxml")
    response = soup.findAll("div", {'class':'tingdok-normal'})
    d['ID'] = soup.select('div.tingdok__breadcrumb-b__container span.tingdok__breadcrumb-b__item')[0].text
    d['parti_spoerger'] = response[0].get_text().strip().split()[-1]
    d['fornavne_spørger'] = response[0].get_text().strip().split()[1]
    d['efternavne_spørger'] = response[0].get_text().strip().split()[2:-1]
    d['minister_titel'] = response[1].get_text().split()[1]
    d['minister_fornavn'] = response[1].get_text().split()[2]
    d['minister_efternavne'] = response[1].get_text().split()[3:]
    d['dato'] = response[2].get_text().split()[1]
    d['status'] = response[4].get_text().split(":")[1].strip()
    d['samling'] = response[3].get_text().split()[1]
    d['anmeldelse'] = response[5].get_text().split()[1]
    d['endeligBesvarelse'] = response[6].get_text().split()[-1]
    d['spoergsmaal'] = response[8].get_text().strip() 
    d['begrundelse'] = response[10].get_text().strip()
	data.append(d)