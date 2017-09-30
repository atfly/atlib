import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

###收集准备数据
def get_dataset(csv_file):
    data = pd.read_csv(csv_file)
    # print(data.head()) #显示前5行数据
    return data

###构建特征和标签
def get_features(data):
    feature_cols = ["f1", "f2"]

    # use the list to select a subset of original DataFrame
    x = data[feature_cols]

    # check the type and shape of X
    print(type(x))
    print(x.shape)

    # select a series from the DataFrame
    y = data["l"]

    return x, y

def fit(x_train, y_train):
    linreg = LinearRegression()
    model = linreg.fit(x_train, y_train)
    print(model)
    print(linreg.intercept_)
    print(linreg.coef_)

if __name__ == "__main__":
    csv_file = r"D:\Advertising.csv"
    data = get_dataset(csv_file)
    # figure_dataset(data)
    x, y = get_features(data)
    fit(x,y)




