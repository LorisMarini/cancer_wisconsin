from dependencies import *

def learn_tree(*, X_train, y_train, X_test, y_test, features, max_features=None, max_leaf_nodes=None):
    """
    Implements training and testing for a decision tree classifier
    """
    if max_features:
        if max_features < 1 or max_features>len(features):
            raise ValueError("max_features expected to be between 2 and len(features)")

    # Instantiate mdoel from its scikit learn class
    estimator = tree.DecisionTreeClassifier(criterion="gini",
                                            max_leaf_nodes=max_leaf_nodes,
                                            random_state=0)

    # Induce the model
    fitted_estimator = estimator.fit(X_train, y_train)

    # Induce model with k-fold cross-validation (with k=10)
    accuracies = cross_val_score(fitted_estimator, X_train, y_train, cv=3, scoring=None)

    avg_training_score = np.mean(accuracies)
    avg_testing_score = estimator.score(X_test, y_test, sample_weight=None)

    return avg_training_score, avg_testing_score
