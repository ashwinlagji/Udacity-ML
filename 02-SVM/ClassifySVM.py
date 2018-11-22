def classify(features_train, labels_train, features_test, labels_test):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score
    
    clf = SVC(kernel="rbf",gamma=10.0,C=1)
    clf.fit(features_train, labels_train)

    pred = clf.predict(features_test)
    
    print accuracy_score(pred, labels_test)

    return clf
    