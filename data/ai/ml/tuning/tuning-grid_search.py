###Grid Search
from sklearn.grid_search import GridSearchCV
params={"n_neighbors":np.arange(1,3),"metric":["euclidean","city_block"]}
gird=GridSearchCV(estimator=knn,param_grid=params)
grid.fit(X_train,y_train)
print(grid.best_score_)
print(grid.best_estimator_.n_neighbors)