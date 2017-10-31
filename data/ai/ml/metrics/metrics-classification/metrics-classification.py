###Accuracy Score
knn.score(X_test,y_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

###Classification Report
from sklearn.metrics import classificton report
print(classification_report(y_test,y_pred))

###Confusion Matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))