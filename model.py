from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm

import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, classification_report

# confusion_ matrix
def confusion_m(y_test, y_predict):
    matrix = confusion_matrix(y_test, y_predict)
    print('confusion_matrix:\n', matrix)
    print('report:\n', classification_report(y_test, y_predict))


def decision_tree(x_train, x_test, y_train, y_test, attr):
    clf_dt = DecisionTreeClassifier()
    clf_dt.fit(x_train, y_train)
    y_predict = clf_dt.predict(x_test)
    score = accuracy_score(y_test, y_predict)
    # accuracy
    print(f'Decision Tree Accuracy: {score * 100} %')
    confusion_m(y_test, y_predict)

    # visual
    # plt.figure(figsize = (10, 8))
    # plot_tree(clf_dt, feature_names = attr, 
    #           class_names = ['notWind_Archer', 'isWind_Archer'],
    #           filled = True,
    #           fontsize = 8)
    # plt.show()

def logistic_regression(x_train, x_test, y_train, y_test):
    clf_lr = LogisticRegression(max_iter = 10000)
    clf_lr.fit(x_train, y_train)
    y_predict = clf_lr.predict(x_test)
    score = accuracy_score(y_test, y_predict)
    print(f'Logistic Regression Accuracy: {score * 100} %')
    confusion_m(y_test, y_predict)

def random_forest(x_train, x_test, y_train, y_test):
    clf_rf = RandomForestClassifier(n_estimators = 400)
    clf_rf.fit(x_train, y_train)
    y_predict = clf_rf.predict(x_test)
    score = accuracy_score(y_test, y_predict)
    print(f'Random Forest Accuracy: {score * 100} %')
    confusion_m(y_test, y_predict)

def gaussianNB(x_train, x_test, y_train, y_test):
    clf_nb = GaussianNB()
    clf_nb.fit(x_train, y_train)
    y_predict = clf_nb.predict(x_test)
    score = accuracy_score(y_test, y_predict)
    print(f'Gaussian_NB Accuracy: {score * 100} %')
    confusion_m(y_test, y_predict)


