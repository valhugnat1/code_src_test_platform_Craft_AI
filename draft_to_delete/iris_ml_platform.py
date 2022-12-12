from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import datasets



def entryStepIris () :
    
    iris_X, iris_y = datasets.load_iris(return_X_y=True)
    np.unique(iris_y)
    
    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))

    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]

    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train)

    result = knn.predict(iris_X_test)
    print (knn.predict([[5, 8, 9, 1]])[0])

    print (result)
    print (iris_y_test)



entryStepIris ()