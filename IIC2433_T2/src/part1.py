import matplotlib.pyplot as plt
import numpy
from numpy import *    
from sklearn import neighbors
import sklearn.metrics
import sklearn.cross_validation

# Generamos una clasificacion knn de los datos, obteniendo precision, recall de esta
def KNN_classifier(data, labels, k, folds=10):
    # Creamos clasificador
    clf = neighbors.KNeighborsClassifier(k)

    # Realizamos cross validation con 10 folds:    
    scores = sklearn.cross_validation.cross_val_score(clf, data, labels, cv=folds, score_func= sklearn.metrics.precision_recall_fscore_support)
    
    meanScores = numpy.mean(scores, axis=0)
    
    print meanScores
