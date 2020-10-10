# -*-coding:utf-8-*-
# @auth ivan
# @time 2019-08-24 18:05:00
# @goal test the model
from sklearn.datasets.california_housing import fetch_california_housing
from sklearn.model_selection import train_test_split
import joblib

housing = fetch_california_housing()
x, y = housing.data, housing.target
x, y = x[:100], y[:100]
y = [1 if i > 2 else 0 for i in y]
data_train, data_test, target_train, target_test = train_test_split(
    x, y, test_size=0.1, random_state=42)


def gradient_boosting_classifier_good(train_x, train_y):
    a, b = [], []
    for i in range(1, 250):
        if i < 250:
            a.append(i)
        if i < 10:
            b.append(i)

    from sklearn.grid_search import GridSearchCV
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier()
    param_grid = {
        'n_estimators': a,
        'max_depth': b,
    }
    grid_search = GridSearchCV(model, param_grid, n_jobs=1, verbose=1)
    """
    D:\Python35\lib\site-packages\sklearn\grid_search.py:553:
    UserWarning: Multiprocessing backed parallel loops cannot be nested below threads,
    setting n_jobs=1 for parameters in parameter_iterable
    """
    grid_search.fit(train_x, train_y)
    best_parameters = grid_search.best_estimator_.get_params()
    for para, val in best_parameters.items():
        print(para, val)

    model = GradientBoostingClassifier(
        n_estimators=best_parameters['n_estimators'],
        max_depth=best_parameters['max_depth'])
    model.fit(train_x, train_y)
    return model


f_model = gradient_boosting_classifier_good
model = f_model(data_train, target_train)
print(
    model.score(data_train, target_train), model.score(data_test, target_test))
joblib.dump(model, "run.model")
