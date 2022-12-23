from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import tarfile


def entryStepIris (dataSetPath) :

    my_tar = tarfile.open(dataSetPath)
    my_tar.extractall('./')
    my_tar.close()

    iris_X =  pd.read_csv('irisX.csv')
    iris_y =  pd.read_csv('irisY.csv')

    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))

    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]

    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train)

    result = knn.predict(iris_X_test)

    # To confirm 
    return pd.DataFrame(result)