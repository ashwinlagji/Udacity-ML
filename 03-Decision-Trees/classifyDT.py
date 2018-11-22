def classify(features_train, labels_train, features_test, labels_test):
    
    ### your code goes here--should return a trained decision tree classifer

    from sklearn import tree
    from sklearn.metrics import accuracy_score
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_train, labels_train)
    
    pred = clf.predict(features_test)
    
    print accuracy_score(pred, labels_test)
    
    return clf