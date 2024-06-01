import numpy as np
import typing
from collections import defaultdict


def kfold_split(num_objects: int,
                num_folds: int) -> list[tuple[np.ndarray, np.ndarray]]:
    step = num_objects // num_folds
    index = np.arange(num_objects)
    lst = []
    for i in range(num_folds - 1):
        test = np.arange(i*step, (i+1) * step)
        lst.append((np.delete(index, test), test))
    train = np.arange(step * (num_folds-1))
    test = np.delete(index, train)
    lst.append((train, test))
    return lst


def knn_cv_score(X: np.ndarray, y: np.ndarray, parameters: dict[str, list],
                 score_function: callable,
                 folds: list[tuple[np.ndarray, np.ndarray]],
                 knn_class: object) -> dict[str, float]:
    dict = {}
    for k in parameters['n_neighbors']:
        for metrics in parameters['metrics']:
            for weights in parameters['weights']:
                for normalizer in parameters['normalizers']:
                    score = []

                    for fold in folds:
                        X_train = X[fold[0]]
                        y_train = y[fold[0]]
                        X_test = X[fold[1]]
                        y_test = y[fold[1]]

                        if normalizer[0] is not None:
                            scaler = normalizer[0]
                            scaler.fit(X_train)
                            X_train = scaler.transform(X_train)
                            X_test = scaler.transform(X_test)

                        classify = knn_class(n_neighbors=k,
                                             weights=weights,
                                             metric=metrics)
                        classify.fit(X_train, y_train)

                        y_pred = classify.predict(X_test)

                        score.append(score_function(y_test, y_pred))

                    dict[(normalizer[1], k,
                          metrics, weights)] = np.mean(score, axis=0)
    return dict
