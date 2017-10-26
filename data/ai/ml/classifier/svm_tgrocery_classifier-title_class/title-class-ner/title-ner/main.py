#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split
from tgrocery import Grocery
import sys
import numpy as np
from sklearn import metrics

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":

    path = '../data/title_class_data1.xlsx'  # 数据文件路径
    path2 = '../data/title_class_data2.xlsx'  # 数据文件路径

    data = pd.read_excel(path, converters={'utf-8': str})
    data2 = pd.read_excel(path2, converters={'utf-8': str})

    data = data.append(data2)

    x, y = data['title'], data['label']
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.7)

    train_src = zip(np.array(y_train, dtype=np.int32).tolist(), np.array(x_train, np.str).tolist())

    grocery = Grocery("title-class-ner")
    grocery.train(train_src)

    grocery.save()

    new_grocery = Grocery('title-class-ner')
    new_grocery.load()

    y_pred = []

    for left, right in zip(x_test, y_test):
        test_src = [('unknow', str(left).lower())]
        res = new_grocery.test(test_src)
        y_pred.append(res.predicted_y[0])

    y_true = np.array(y_test, dtype=int)
    y_pred = np.array(y_pred, dtype=int)

    classify_report = metrics.classification_report(y_true, y_pred)
    confusion_matrix = metrics.confusion_matrix(y_true, y_pred)
    overall_accuracy = metrics.accuracy_score(y_true, y_pred)
    acc_for_each_class = metrics.precision_score(y_true, y_pred, average=None)
    average_accuracy = np.mean(acc_for_each_class)
    score = metrics.accuracy_score(y_true, y_pred)

    print('** classify_report :\n')
    print(classify_report)

    print('** confusion_matrix :\n')
    print(confusion_matrix)

    print('** acc_for_each_class\n')
    print (acc_for_each_class)

    print('** average_accuracy:\n')
    print(average_accuracy)

    print('** overall_accuracy:\n')
    print(overall_accuracy)

    print('** score:\n')
    print(score)
