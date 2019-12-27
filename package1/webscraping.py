import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import requests
from lxml import html
import lxml.html as lh
from bs4 import BeautifulSoup
from acquisition import reading_csv

df = pd.read_csv('cleaned')

def education_list(df):
    a = list(df.loc[:, 'education'] == 'None')
    count = -1
    none_education_list = []
    for i in a:
        count += 1
        if i == True:
            none_education_list.append(count)
    return none_education_list

def web_scraping_education(df_col):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    page_url = 'https://en.wikipedia.org/wiki/'
    edu_url = []
    for i in education_list(df):
        req = requests.get(page_url + df_col[i], headers=header)
        soup = BeautifulSoup(req.text, 'lxml')

        edu_find = soup.find('table', attrs={'class': 'infobox biography vcard'})
        edu_url.append(str(edu_find))

    edu_l = []
    for j in edu_url:
        edu_l.append(re.findall('Alma', j) or re.findall('Education', j))

    edu = []
    for x in edu_l:
        if len(x) != 0:
            edu.append('Yes')
        else:
            edu.append('No')
    return edu

def webscraping(df, file):
    df['education'] = web_scraping_education(df.name)

    df.drop('name', axis=1, inplace=True)

    return df.to_csv(file,  index=False)

webscraping(df, 'web')
