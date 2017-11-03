# -*- coding: utf-8 -*-

"""
    作者:     梁斌
    版本:     1.0
    日期:     2017/10
    实战案例：员工离职原因分析及预测

    该案例有配套的讲解版本，在jupyter演示版中可找到

    声明：小象学院拥有完全知识产权的权利；只限于善意学习者在本课程使用，
         不得在课程范围外向任何第三方散播。任何其他人或机构不得盗版、复制、仿造其中的创意，
         我们将保留一切通过法律手段追究违反者的权利
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import os
from imblearn.over_sampling import SMOTE
from sklearn import metrics

# 指定数据集路径
dataset_path = '../dataset'
datafile_path = os.path.join(dataset_path, 'train.csv')

DO_OVERSAMPLE = False


def visualize_data(sample_data):
    """
        变量关系可视化
    """
    plt.figure()
    sns.countplot(x='Attrition', data=sample_data, hue='Education')
    plt.show()

    # ==== 单变量关系 ====
    plt.figure()

    # 离职与年龄的关系
    plt.subplot(2, 2, 1)
    sns.boxplot(x='Attrition', y='Age', data=sample_data)

    # 离职与家庭和公司距离的关系
    plt.subplot(2, 2, 2)
    sns.boxplot(x='Attrition', y='DistanceFromHome', data=sample_data)

    # 离职与月收入的关系
    plt.subplot(2, 2, 3)
    sns.boxplot(x='Attrition', y='MonthlyIncome', data=sample_data)

    # 离职与曾经工作公司数的关系
    plt.subplot(2, 2, 4)
    sns.boxplot(x='Attrition', y='NumCompaniesWorked', data=sample_data)

    plt.show()

    plt.figure()
    # 离职与婚姻状况的关系
    plt.subplot(2, 1, 1)
    sns.countplot(x='Attrition', hue='MaritalStatus', data=sample_data)

    # 离职与性别的关系
    plt.subplot(2, 1, 2)
    sns.countplot(x='Attrition', hue='Gender', data=sample_data)

    # ==== 多变量关系 ====
    plt.figure()
    sns.pairplot(sample_data, hue='Attrition', vars=['Age', 'MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike',
                                                     'TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany',
                                                     'YearsInCurrentRole',
                                                     'YearsSinceLastPromotion', 'YearsWithCurrManager'])
    plt.show()


def main():
    """
        主函数
    """
    # 加载数据
    sample_data = pd.read_csv(datafile_path)
    # ==== 预览数据 ====
    print('数据预览：')
    print(sample_data.head())
    print(sample_data.info())
    print(sample_data.describe())

    # 正负样本的比例
    pos_data = sample_data[sample_data['Attrition'] == 1]
    neg_data = sample_data[sample_data['Attrition'] == 0]
    print('正样本记录数：{}，所占比例：{}'.format(len(pos_data), len(pos_data) / len(sample_data)))
    print('负样本记录数：{}，所占比例：{}'.format(len(neg_data), len(neg_data) / len(sample_data)))

    # ==== 变量关系可视化 ====
    visualize_data(sample_data)

    # ==== 离职预测 ====
    # 数值型数据
    num_cols = ['Age', 'MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears',
                'TrainingTimesLastYear',
                'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']
    # 类别型数据
    # 所有类别型数据
    # cat_cols = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus',
    #             'Over18', 'OverTime']
    # 本案例只选取3个作为例子
    cat_cols = ['Gender', 'MaritalStatus', 'OverTime']
    # 有序类别数据
    ord_cols = ['DistanceFromHome', 'Education', 'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel',
                'JobSatisfaction',
                'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel', 'WorkLifeBalance']

    # 目标列
    target_col = ['Attrition']

    # 所有特征列
    total_cols = num_cols + cat_cols + ord_cols

    used_data = sample_data[total_cols + target_col]

    print('使用{}列数据作为特征'.format(len(total_cols)))

    # 分割训练集，测试集，80%作为训练集，20%作为测试集
    # 保证训练集和测试集中的正负样本的比例一样
    # 正负样本的比例

    pos_data = used_data[used_data['Attrition'] == 1].reindex()
    train_pos_data = pos_data.iloc[:int(len(pos_data) * 0.8)].copy()
    test_pos_data = pos_data.iloc[int(len(pos_data) * 0.8):].copy()

    neg_data = used_data[used_data['Attrition'] == 0].reindex()
    train_neg_data = neg_data.iloc[:int(len(neg_data) * 0.8)].copy()
    test_neg_data = neg_data.iloc[int(len(neg_data) * 0.8):].copy()

    train_data = pd.concat([train_pos_data, train_neg_data])
    test_data = pd.concat([test_pos_data, test_neg_data])

    print('训练集数据个数', len(train_data))
    print('正负样本比例', len(train_pos_data) / len(train_neg_data))
    train_data.head()

    print('测试集数据个数', len(test_data))
    print('正负样本比例', len(test_pos_data) / len(test_neg_data))
    test_data.head()

    # ==== 特征工程 ====
    # 对类别型数据进行“独热编码” One-Hot Encoding

    # 先进行Label Encoding
    # Gender数据
    gender_label_enc = preprocessing.LabelEncoder()
    train_data['Gender_Label'] = gender_label_enc.fit_transform(train_data['Gender'])

    # MaritalStatus数据
    marital_label_enc = preprocessing.LabelEncoder()
    train_data['Marital_Label'] = marital_label_enc.fit_transform(train_data['MaritalStatus'])

    # OverTime数据
    ot_label_enc = preprocessing.LabelEncoder()
    train_data['OT_Label'] = ot_label_enc.fit_transform(train_data['OverTime'])

    print('Gender数据:')
    print(train_data.groupby('Gender_Label').size())

    print()
    print('MaritalStatus数据:')
    print(train_data.groupby('Marital_Label').size())

    print()
    print('OverTime数据:')
    print(train_data.groupby('OT_Label').size())

    # 再进行One-Hot Encoding
    one_hot_enc = preprocessing.OneHotEncoder()
    train_cat_feats = one_hot_enc.fit_transform(train_data[['Gender_Label', 'Marital_Label', 'OT_Label']]).toarray()
    # print(train_cat_feats[:5, :])

    # 对测试集数据进行相应的编码操作
    # 注意要使用从训练集中得出的encoder

    # 标签编码
    # Gender数据
    test_data['Gender_Label'] = gender_label_enc.transform(test_data['Gender'])

    # MaritalStatus数据
    test_data['Marital_Label'] = marital_label_enc.transform(test_data['MaritalStatus'])

    # OverTime数据
    test_data['OT_Label'] = ot_label_enc.transform(test_data['OverTime'])

    # 独热编码
    test_cat_feats = one_hot_enc.transform(test_data[['Gender_Label', 'Marital_Label', 'OT_Label']]).toarray()

    # 整合所有特征
    train_num_feats = train_data[num_cols].values
    train_ord_feats = train_data[ord_cols].values
    train_feats = np.hstack((train_num_feats, train_ord_feats, train_cat_feats))
    train_targets = train_data[target_col].values

    # 整合所有特征
    test_num_feats = test_data[num_cols].values
    test_ord_feats = test_data[ord_cols].values
    test_feats = np.hstack((test_num_feats, test_ord_feats, test_cat_feats))
    test_targets = test_data[target_col].values

    print('训练数据：', train_feats.shape)
    print('测试数据：', test_feats.shape)

    if DO_OVERSAMPLE:
        # 处理不平衡数据
        # 过采样“少”的样本

        print('重采样前：')
        print('正样本个数：', len(train_targets[train_targets == 1]))
        print('负样本个数：', len(train_targets[train_targets == 0]))

        sm = SMOTE(random_state=0)
        train_resampled_feats, train_resampled_targets = sm.fit_sample(train_feats, train_targets)
        print('重采样后：')
        print('正样本个数：', len(train_resampled_targets[train_resampled_targets == 1]))
        print('负样本个数：', len(train_resampled_targets[train_resampled_targets == 0]))

    # ==== 数据建模 ====
    if DO_OVERSAMPLE:
        # 如果选择“重采样”请取消以下的注释
        # 随机森林
        rf_clf = RandomForestClassifier(random_state=0)
        rf_clf.fit(train_resampled_feats, train_resampled_targets)

        # 逻辑回归
        lr_clf = LogisticRegression()
        lr_clf.fit(train_resampled_feats, train_resampled_targets)
    else:
        # 随机森林
        rf_clf = RandomForestClassifier(random_state=0)
        rf_clf.fit(train_feats, train_targets)

        # 逻辑回归
        lr_clf = LogisticRegression()
        lr_clf.fit(train_feats, train_targets)

    # ==== 模型验证 ====
    # 随机森林
    if DO_OVERSAMPLE:
        print('重采样后：')

    print('测试集中正样本数', len(test_pos_data))
    print('测试集中负样本数', len(test_neg_data))
    print('随机森林：')
    test_pred = rf_clf.predict(test_feats)
    print(metrics.confusion_matrix(test_targets, test_pred, labels=[1, 0]))
    print('准确率：', metrics.accuracy_score(test_targets, test_pred))

    # 逻辑回归
    print('逻辑回归：')
    test_pred = lr_clf.predict(test_feats)
    print(metrics.confusion_matrix(test_targets, test_pred, labels=[1, 0]))
    print('准确率：', metrics.accuracy_score(test_targets, test_pred))


if __name__ == '__main__':
    main()
