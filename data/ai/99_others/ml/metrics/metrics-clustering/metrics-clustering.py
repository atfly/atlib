###Adjusted Rand Index
from sklearn.metrics import adjusted_rand_score
adjusted_rand_score(y_true,y_pred)

###Homogeneity
from sklearn.metrics import homogeneity_score
homogeneity_score(y_true,y_pred)

###V-measure
from sklearn.metrics import v_measure_score
metrics.v_measure_score(y_test,y_pred)