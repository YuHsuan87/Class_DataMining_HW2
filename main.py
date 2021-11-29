import pandas as pd
from sklearn.model_selection import train_test_split
from model import *

if __name__ == '__main__':

    # read csv
    df = pd.read_csv('data1.csv')
    y = df['isWind_Archer']
    x = df.drop(['isWind_Archer'], axis = 1)
    attr = list(df)

    # train & test dataset
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)
    print('----------------------------------------------')

    # decision_tree
    decision_tree(x_train, x_test, y_train, y_test, attr)
    print('----------------------------------------------')

    # logistic_regression
    logistic_regression(x_train, x_test, y_train, y_test)
    print('----------------------------------------------')

    # random_forest
    random_forest(x_train, x_test, y_train, y_test)
    print('----------------------------------------------')

    # gaussianNB
    gaussianNB(x_train, x_test, y_train, y_test)
    print('----------------------------------------------')


