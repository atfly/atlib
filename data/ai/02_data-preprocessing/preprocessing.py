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

