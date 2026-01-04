import joblib


def predict(data):

    clf = joblib.load("decisiontree.sav")
                  
    return clf.predict(data)