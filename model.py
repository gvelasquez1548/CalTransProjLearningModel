import numpy as np
from sklearn.naive_bayes import GaussianNB

#Sklearn NB test code
def ml():
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 1, 1, 2, 2, 2])
    clf = GaussianNB()
    clf.fit(X,Y)
    #result
    res = clf.predict([[-0.8, -1]])
    #return result to HTML
    return res[0]
