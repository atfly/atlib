# !/usr/bin/python
# -*- coding:utf-8 -*-

# 1.1 数据挖掘的步骤
# http://www.cnblogs.com/jasonfreak/p/5448462.html
# 数据挖掘通常包括数据采集，数据分析，特征工程，训练模型，模型评估等步骤。使用sklearn工具可以方便地进行特征工程和模型训练工作，
# 在《使用sklearn做单机特征工程》中，我们最后留下了一些疑问：特征处理类都有三个方法fit、transform和fit_transform，fit方法居然和模型训练方法fit同名（不光同名，参数列表都一样），这难道都是巧合？
# 显然，这不是巧合，这正是sklearn的设计风格。我们能够更加优雅地使用sklearn进行特征工程和模型训练工作

# 我们使用sklearn进行虚线框内的工作（sklearn也可以进行文本特征提取）。通过分析sklearn源码，我们可以看到除训练，预测和评估以外，处理其他工作的类都实现了3个方法：fit、transform和fit_transform。从命名中可以看到，
# fit_transform方法是先调用fit然后调用transform，我们只需要关注fit方法和transform方法即可。
# transform方法主要用来对特征进行转换。从可利用信息的角度来说，转换分为无信息转换和有信息转换。无信息转换是指不利用任何其他信息进行转换，比如指数、对数函数转换等。
# 有信息转换从是否利用目标值向量又可分为无监督转换和有监督转换。无监督转换指只利用特征的统计信息的转换，统计信息包括均值、标准差、边界等等，比如标准化、PCA法降维等。有监督转换指既利用了特征信息又利用了目标值信息的转换，比如通过模型选择特征、LDA法降维等。通过总结常用的转换类，我们得到下表：


# 包	类	参数列表	类别	fit方法有用	说明
# sklearn.preprocessing	StandardScaler	特征	无监督	Y	标准化
# sklearn.preprocessing	MinMaxScaler	特征	无监督	Y	区间缩放
# sklearn.preprocessing	Normalizer	特征	无信息	N	归一化
# sklearn.preprocessing	Binarizer	特征	无信息	N	定量特征二值化
# sklearn.preprocessing	OneHotEncoder	特征	无监督	Y	定性特征编码
# sklearn.preprocessing	Imputer	特征	无监督	Y	缺失值计算
# sklearn.preprocessing	PolynomialFeatures	特征	无信息	N	多项式变换（fit方法仅仅生成了多项式的表达式）
# sklearn.preprocessing	FunctionTransformer	特征	无信息	N	自定义函数变换（自定义函数在transform方法中调用）
# sklearn.feature_selection	VarianceThreshold	特征	无监督	Y	方差选择法
# sklearn.feature_selection	SelectKBest	特征/特征+目标值	无监督/有监督	Y	自定义特征评分选择法
# sklearn.feature_selection	SelectKBest+chi2	特征+目标值	有监督	Y	卡方检验选择法
# sklearn.feature_selection	RFE	特征+目标值	有监督	Y	递归特征消除法
# sklearn.feature_selection	SelectFromModel	特征+目标值	有监督	Y	自定义模型训练选择法
# sklearn.decomposition	PCA	特征	无监督	Y	PCA降维
# sklearn.lda	LDA	特征+目标值	有监督	Y	LDA降维


# 1.2 数据初貌
# 在此，我们仍然使用IRIS数据集来进行说明。为了适应提出的场景，对原数据集需要稍微加工：

from numpy import hstack, vstack, array, median, nan
from numpy.random import choice
from sklearn.datasets import load_iris
from sklearn.pipeline import FeatureUnion, _fit_one_transformer, _fit_transform_one, _transform_one

iris = load_iris()
# 特征矩阵加工
# 使用vstack增加一行含缺失值的样本(nan, nan, nan, nan)
# 使用hstack增加一列表示花的颜色（0-白、1-黄、2-红），花的颜色是随机的，意味着颜色并不影响花的分类
iris.data = hstack((choice([0, 1, 2], size=iris.data.shape[0] + 1).reshape(-1, 1),
                    vstack((iris.data, array([nan, nan, nan, nan]).reshape(1, -1)))))
# 目标值向量加工
# 增加一个目标值，对应含缺失值的样本，值为众数
iris.target = hstack((iris.target, array([median(iris.target)])))

# 1.3 关键技术
# 并行处理，流水线处理，自动化调参，持久化是使用sklearn优雅地进行数据挖掘的核心。并行处理和流水线处理将多个特征处理工作，甚至包括模型训练工作组合成一个工作（从代码的角度来说，即将多个对象组合成了一个对象）。
# 在组合的前提下，自动化调参技术帮我们省去了人工调参的反锁。训练好的模型是贮存在内存中的数据，持久化能够将这些数据保存在文件系统中，之后使用时无需再进行训练，直接从文件系统中加载即可。


# 2 并行处理
# 并行处理使得多个特征处理工作能够并行地进行。根据对特征矩阵的读取方式不同，可分为整体并行处理和部分并行处理。
# 整体并行处理，即并行处理的每个工作的输入都是特征矩阵的整体；部分并行处理，即可定义每个工作需要输入的特征矩阵的列。
#
# 2.1 整体并行处理
# pipeline包提供了FeatureUnion类来进行整体并行处理：

from numpy import log1p
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import Binarizer
from sklearn.pipeline import FeatureUnion
from sklearn.preprocessing import OneHotEncoder

step2_1 = ('OneHotEncoder', OneHotEncoder(sparse=False))
# 新建将部分特征矩阵进行对数函数转换的对象
step2_2 = ('ToLog', FunctionTransformer(log1p))
# 新建将部分特征矩阵进行二值化类的对象
step2_3 = ('ToBinary', Binarizer())

# 新建整体并行处理对象
# 该对象也有fit和transform方法，fit和transform方法均是并行地调用需要并行处理的对象的fit和transform方法
# 参数transformer_list为需要并行处理的对象列表，该列表为二元组列表，第一元为对象的名称，第二元为对象
step2 = ('FeatureUnion', FeatureUnion(transformer_list=[step2_1, step2_2, step2_3]))

# 3 流水线处理
# pipeline包提供了Pipeline类来进行流水线处理。流水线上除最后一个工作以外，其他都要执行fit_transform方法，且上一个工作输出作为下一个工作的输入。最后一个工作必须实现fit方法，输入为上一个工作的输出；
# 但是不限定一定有transform方法，因为流水线的最后一个工作可能是训练！根据本文提出的场景，结合并行处理，构建完整的流水线的代码如下：

from numpy import log1p
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 新建计算缺失值的对象
step1 = ('Imputer', Imputer())
# 新建将部分特征矩阵进行定性特征编码的对象
step2_1 = ('OneHotEncoder', OneHotEncoder(sparse=False))
# 新建将部分特征矩阵进行对数函数转换的对象
step2_2 = ('ToLog', FunctionTransformer(log1p))
# 新建将部分特征矩阵进行二值化类的对象
step2_3 = ('ToBinary', Binarizer())
# 新建部分并行处理对象，返回值为每个并行工作的输出的合并
step2 = ('FeatureUnion', FeatureUnion(transformer_list=[step2_1, step2_2, step2_3]))
# 新建无量纲化对象
step3 = ('MinMaxScaler', MinMaxScaler())
# 新建卡方校验选择特征的对象
step4 = ('SelectKBest', SelectKBest(chi2, k=3))
# 新建PCA降维的对象
step5 = ('PCA', PCA(n_components=2))
# 新建逻辑回归的对象，其为待训练的模型作为流水线的最后一步
step6 = ('LogisticRegression', LogisticRegression(penalty='l2'))
# 新建流水线处理对象
# 参数steps为需要流水线处理的对象列表，该列表为二元组列表，第一元为对象的名称，第二元为对象
pipeline = Pipeline(steps=[step1, step2, step3, step4, step5, step6])

# 4 自动化调参
# 网格搜索为自动化调参的常见技术之一，grid_search包提供了自动化调参的工具，包括GridSearchCV类。对组合好的对象进行训练以及调参的代码如下


from sklearn.model_selection import GridSearchCV

# 新建网格搜索对象
# 第一参数为待训练的模型
# param_grid为待调参数组成的网格，字典格式，键为参数名称（格式“对象名称__子对象名称__参数名称”），值为可取的参数值列表
grid_search = GridSearchCV(pipeline, param_grid={'FeatureUnion__ToBinary__threshold': [1.0, 2.0, 3.0, 4.0],
                                                 'LogisticRegression__C': [0.1, 0.2, 0.4, 0.8]})
# 训练以及调参
grid_search.fit(iris.data, iris.target)

# 5 持久化
# 　　externals.joblib包提供了dump和load方法来持久化和加载内存数据：

from sklearn.externals import joblib

# 持久化数据
# 第一个参数为内存中的对象
# 第二个参数为保存在文件系统中的名称
# 第三个参数为压缩级别，0为不压缩，3为合适的压缩级别
joblib.dump(grid_search, 'grid_search.dmp', compress=3)
# 从文件系统中加载数据到内存中
grid_search = joblib.load('grid_search.dmp')



# 6 回顾
# 包	类或方法	说明
# sklearn.pipeline	Pipeline	流水线处理
# sklearn.pipeline	FeatureUnion	并行处理
# sklearn.grid_search	GridSearchCV	网格搜索调参
# externals.joblib	dump	数据持久化
# externals.joblib	load	从文件系统中加载数据至内存
#
# 注意：组合和持久化都会涉及pickle技术，在sklearn的技术文档中有说明，将lambda定义的函数作为FunctionTransformer的自定义转换函数将不能pickle化。
