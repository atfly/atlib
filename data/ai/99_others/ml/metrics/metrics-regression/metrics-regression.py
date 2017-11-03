###Mean Absolute Error
from sklearn.metrics import mean_absolute_error
y_true=[3,-0.5,2]
mean_absolute_error(y_true,y_pred)

###Mean Squared Error
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test,y_pred)

###R2 Score
from sklearn.metrics import r2_score
r2_score(y_true,y_pred)

