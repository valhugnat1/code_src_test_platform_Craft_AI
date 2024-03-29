from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


def entryStepIris():

    iris_X, iris_y = datasets.load_iris(return_X_y=True)

    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))

    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]

    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train)

    result = knn.predict(iris_X_test)

    print(result)