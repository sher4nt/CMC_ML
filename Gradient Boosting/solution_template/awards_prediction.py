from sklearn.preprocessing import MultiLabelBinarizer
from catboost import CatBoostRegressor
import pandas as pd
import numpy as np

from numpy import ndarray

"""
 Внимание!
 В проверяющей системе имеется проблема с catboost.
 При использовании этой библиотеки, в скрипте с решением необходимо инициализировать метод с использованием `train_dir` как показано тут:
 CatBoostRegressor(train_dir='/tmp/catboost_info')
"""


def unknown_director(x):
    if x == 'unknown':
        return ['unknown']
    return x


def train_model_and_predict(train_file: str, test_file: str) -> ndarray:
    """
    This function reads dataset stored in the folder, trains predictor and returns predictions.
    :param train_file: the path to the training dataset
    :param test_file: the path to the testing dataset
    :return: predictions for the test file in the order of the file lines (ndarray of shape (n_samples,))
    """

    df_train = pd.read_json(train_file, lines=True)
    df_test = pd.read_json(test_file, lines=True)

    y_train = df_train["awards"]
    del df_train["awards"]

    categorial_features = np.array(['actor_0_gender', 'actor_1_gender', 'actor_2_gender'])

    df_train[categorial_features] = df_train[categorial_features].astype('category')
    df_test[categorial_features] = df_test[categorial_features].astype('category')

    df_train['directors'] = df_train['directors'].apply(unknown_director)
    df_test['directors'] = df_test['directors'].apply(unknown_director)

    for feature in ['genres', 'directors', 'filming_locations', 'keywords']:
        mlb = MultiLabelBinarizer()

        temp = mlb.fit_transform(df_train[feature])
        feat_names = np.apply_along_axis(lambda x: feature + '_' + x, arr=mlb.classes_, axis=0)
        df_temp = pd.DataFrame(temp, columns=feat_names)
        df_train = df_train.drop(feature, axis=1)
        df_train = pd.concat([df_train, df_temp], axis=1)

        temp = mlb.transform(df_test[feature])
        df_temp = pd.DataFrame(temp, columns=feat_names)
        df_test = df_test.drop(feature, axis=1)
        df_test = pd.concat([df_test, df_temp], axis=1)

        categorial_features = np.append(categorial_features, feat_names)

    regressor = CatBoostRegressor(
        train_dir='/tmp/catboost_info', n_estimators=1000, depth=9,
        learning_rate=1e-1, cat_features=categorial_features)
    regressor.fit(df_train, y_train)
    return regressor.predict(df_test)
