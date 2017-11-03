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


###观察数据分布
def figure_dataset(data):
    # 子同一图表中观察所有数据的分布情况
    plt.plot(data["TV"], "ro", label="TV")
    plt.plot(data["Radio"], "g^", label="Radio")
    plt.plot(data["Newspaper"], "b*", label="Newspaper")
    plt.legend(loc="lower right")
    plt.grid()
    plt.show()

    # 通过各子图观察各数据分布的情况
    plt.figure(figsize=(9, 12))
    plt.subplot(311)
    plt.plot(data["TV"], "ro")
    plt.title("TV")
    plt.grid()

    plt.subplot(312)
    plt.plot(data["Radio"], "g^")
    plt.title("Radio")
    plt.grid()

    plt.subplot(313)
    plt.plot(data["Newspaper"], "b*")
    plt.title("Newspaper")
    plt.grid()

    plt.tight_layout()
    plt.show()


###构建特征和标签
def get_features(data):
    feature_cols = ["TV", "Radio", "Newspaper"]

    # use the list to select a subset of original DataFrame
    x = data[feature_cols]

    # check the type and shape of X
    print(type(x))
    print(x.shape)

    # select a series from the DataFrame
    y = data["Sales"]

    return x, y


###构建训练和测试集合
def get_train_dataset(x, y):
    # 默认切分是75%的训练集和25%的验证集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    # print(x_train.shape)
    # print(y_train.shape)
    # print(x_test.shape)
    # print(y_test.shape)

    return x_train, x_test, y_train, y_test


###sklearn的线性回归
def fit(x_train, y_train, x_test, y_test):
    linreg = LinearRegression()
    model = linreg.fit(x_train, y_train)
    # print(model)
    # print(linreg.intercept_)
    # print(linreg.coef_)

    y_pred = linreg.predict(x_test)
    # print(y_pred)
    # print(type(y_pred),type(y_test))
    # print(len(y_pred),len(y_test))
    # print(y_pred.shape,y_test.shape)

    return y_pred, y_test


###回归问题的评测
# 平均绝对误差(Mean Absolute Error,MAE)
# 均方误差(Mean Squared Error,MSE)
# 均方根误差(Root Mean Squared Error,RMSE)
def evaluation(y_pred, y_test):
    sum_mean = 0
    for i in range(len(y_pred)):
        sum_mean += (y_pred[i] - y_test.values[i]) ** 2
        print("RMSE by hand", np.sqrt(sum_mean / len(y_pred)))

    # 画图直观感受
    plt.figure()
    plt.plot(range(len(y_pred)), y_pred, "b", label="predict")
    plt.plot(range(len(y_test)), y_test, "r", label="test")
    plt.legend(loc="upper right")  # 显示图中的标签
    plt.xlabel("the number of sales")
    plt.ylabel("value of sales")
    plt.show()


###结果分析
###基于公式和结果,看是否有必要

if __name__ == "__main__":
    csv_file = r"D:\Advertising.csv"
    data = get_dataset(csv_file)
    # figure_dataset(data)
    x, y = get_features(data)
    x_train, x_test, y_train, y_test = get_train_dataset(x, y)

    y_pred, y_test = fit(x_train, y_train, x_test, y_test)
    print("============================================")

    print(y_pred)

    print("============================================")
    print(y_test)

    evaluation(y_pred, y_test)
