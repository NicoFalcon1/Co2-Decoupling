import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, root_mean_squared_error


def TrainModel(model, poly, X, y, threshold=0.01):
    r2 = 0.00
    while r2 < threshold:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        X_poly_feat = poly.fit_transform(X_train)
        X_poly_test = poly.transform(X_test)

        model.fit(X_poly_feat, y_train)
        y_pred = model.predict(X_poly_test)

        r2 = r2_score(y_test, y_pred)

    rms = root_mean_squared_error(y_test, y_pred)

    tests = [r2, rms]
    test_data = [X_test['year'], y_test, y_pred]

    refs = list(X.columns)
    target = [y.name]

    return [model, poly, refs, target, tests, test_data]


def TrainSVR(model, X, y, threshold=0.01):
    r2 = 0.00
    while r2 < threshold:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        r2 = r2_score(y_test, y_pred)

    rms = root_mean_squared_error(y_test, y_pred)

    tests = [r2, rms]
    test_data = [X_test['year'], y_test, y_pred]

    refs = list(X.columns)
    target = [y.name]

    return [model, refs, target, tests, test_data]