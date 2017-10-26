#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import datetime
from tgrocery import Grocery
import sys
import numpy as np
import jieba

from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
from sklearn import metrics
from sklearn.naive_bayes import BernoulliNB

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

reload(sys)
from sklearn.metrics import classification_report

sys.setdefaultencoding('utf8')

if __name__ == "__main__":

    new_grocery = Grocery('title-model')
    new_grocery.load()

    path = '../data/title_test_data2.xlsx'
    test_data = pd.read_excel(path, converters={'utf-8': str})
    x_test, y_test = test_data['title'], test_data['label']

    pred = []
    for left in x_test:
        test_src = [('unknow', str(left).lower())]
        res = new_grocery.test(test_src)
        pred.append(int(res.predicted_y[0]))

    df = pd.DataFrame(pred, x_test)
    df.to_excel('title_test_result2.xlsx')
