from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import datasets
import joblib



def entryStepIris (dataFilePath, modelFilePath) :
    
    knn = joblib.load(modelFilePath)

    result = knn.predict(iris_X_test)
    print (knn.predict([[5, 8, 9, 1]])[0])

    print (result)
    print (iris_y_test)



