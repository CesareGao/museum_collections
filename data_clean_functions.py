## this file contain several functions for data cleaning of the dataset

## import modules
import pandas as pd
import numpy as np
import re
import nltk
from collections import Counter

## data cleaning functions

def credit_year(row):
    if pd.notna(row):
        ## find the year in string type document
        year_str = re.compile('\d{4}').findall(row.split(',')[-1])
        if year_str:
            year_int = int(year_str[0])
            ## filter wrong years according to the found year of the museum
            if 1870 <= year_int <= 2019:
                return pd.Timestamp(str(year_int))
    return np.nan

def check_name(row):
    if pd.isna(row.Artist_Alpha_Sort):
        return True
    else:
        r1 = re.findall(r'\w+',row.Artist_Display_Name.lower())
        r2 = re.findall(r'\w+',row.Artist_Alpha_Sort.lower())
        count = 0
        for word in r1:
            if word in r2:
                count += 1
        if count/len(r1) > 0.6:
            return True
        count = 0
        for word in r2:
            if word in r1:
                count += 1
        if count/len(r2) > 0.6:
            return True
        else:
            return False

class contraction_replacer(object):
    def __init__(self, contraction_patterns):
        # store compiled regex object
        self._contraction_regexes = [(re.compile(p), replaced_text) for p, replaced_text in contraction_patterns]

    def do_contraction_normalization(self, text):
        for contraction_regex, replaced_text in self._contraction_regexes:
            text = contraction_regex.sub(replaced_text,text)
        return text

def get_noun(row):
    sample_contraction_replacer = contraction_replacer(contraction_patterns)
    ## word tokenize
    if pd.isna(row):
        return row
    else:
        text = re.sub('\|',' ',row)
    words = nltk.tokenize.word_tokenize(sample_contraction_replacer.do_contraction_normalization(text))
    words = set(words)

    ## stop words removal
    stopwords = nltk.corpus.stopwords.words('english')
    words = [w for w in words if w not in stopwords]

    ## lemmatization
    wnetl = WordNetLemmatizer()

    for i in range(len(words)):
        if not wordnet.synsets(words[i]):
            nword = wnetl.lemmatize(words[i], 'n')
            if wordnet.synsets(nword):
                words[i] = nword
    return '|'.join(words)

def select_top_ten_roles(df):
    roles = defaultdict(int)
    for i in df[df.Artist_Role.notna()].index:
        for role in df.Artist_Role.loc[i].split('|'):
            roles[role] += 1
    x, y = [], []
    upper_bound = inf
    for _ in range(10):
        lar = -inf
        for key,val in roles.items():
            if lar < val < upper_bound:
                lar = val
                temp = key
        upper_bound = lar
        x.append(lar)
        y.append(temp)
    return x, y, roles
