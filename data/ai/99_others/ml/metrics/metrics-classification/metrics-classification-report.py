from sklearn.metrics import classification_report
y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
target_names = ['class 0', 'class 1', 'class 2']
print(classification_report(y_true, y_pred, target_names=target_names))
print(classification_report(y_true, y_pred))

=============================================================================

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