import matplotlib.pyplot as plt
import numpy
from numpy import *    
from sklearn.naive_bayes import GaussianNB
import sklearn.metrics
import sklearn.cross_validation
import sklearn.tree

# Generamos una clasificacion knn de los datos, obteniendo precision, recall de esta
def GaussianNB_classifier(data, labels, folds=10):
    # Creamos clasificador
    clf = GaussianNB()
    
    # Realizamos cross validation con 10 folds:    
    scores = sklearn.cross_validation.cross_val_score(clf, data, labels, cv=folds, score_func= sklearn.metrics.precision_recall_fscore_support)
        
    meanScores = numpy.mean(scores, axis=0)
    
    print meanScores
