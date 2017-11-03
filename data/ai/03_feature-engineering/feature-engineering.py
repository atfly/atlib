#数据和特征决定了机器学习的上限，而模型和算法只是逼近这个上限而已
#StandardScaler	无量纲化	标准化，基于特征矩阵的列，将特征值转换至服从标准正态分布
#MinMaxScaler	无量纲化	区间缩放，基于最大最小值，将特征值转换到[0, 1]区间上
#Normalizer	归一化	基于特征矩阵的行，将样本向量转换为“单位向量”
#Binarizer	二值化	基于给定阈值，将定量特征按阈值划分
#OneHotEncoder	哑编码	将定性数据编码为定量数据
#Imputer	缺失值计算	计算缺失值，缺失值可填充为均值等
#PolynomialFeatures	多项式数据转换	多项式数据转换
#FunctionTransformer	自定义单元数据转换	使用单变元的函数来转换数据

###Standardization
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler().fix(X_train)
standardized_X=scaler.transform(X_train)
standardized_X_test=scaler.transform(X_test)

###Normalization
from sklearn.preprocessing import Normalizer
scaler=Normalizer().fix(X_train)
normalized_X=scaler.transform(X_train)
normalized_X_test=scaler.transform(X_test)

###Binarization
from sklearn.preprocessing import Binarizer
binarizer=Binarizer(threshold=0.0).fit(X)
binary_X=binarizer.transform(X)

###Encoding Categorical Features
from sklearn.preprocessing import LabelEncoder
enc=LabelEncoder()
y=enc.fit_transform(y)

###Imputing Missing Values
from sklearn.preprocessing import Imputer
imp=Imputer(missing_values=0,strategy='mean',axis=0)
imp.fit_transform(X_train)

###Generating Polynomial Features
from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(5)
poly.fit_transform(X)

