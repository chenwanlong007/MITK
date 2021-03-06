'''
Created on Oct 20, 2015

@author: wirkert
'''

import numpy as np
from sklearn.cross_validation import KFold
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model.logistic import LogisticRegressionCV
from sklearn.ensemble.forest import RandomForestClassifier


def prepare_data_for_weights_estimation(X_s, X_t):
    nr_s = X_s.shape[0]
    nr_t = X_t.shape[0]
    source_labels = np.zeros(nr_s)
    target_labels = np.ones(nr_t)
    X_all = np.concatenate((X_s, X_t))
    all_labels = np.concatenate((source_labels, target_labels))
    return X_all, all_labels


def estimate_weights_random_forests(X_s, X_t, X_w):

    X_all, all_labels = prepare_data_for_weights_estimation(X_s, X_t)
    # train logistic regression
    kf = KFold(X_all.shape[0], 10, shuffle=True)
    param_grid_rf = [
      {"n_estimators": np.array([500]),
       "max_depth": np.array([6]),
       # "max_features": np.array([1, 2, 4, 8, 16]),
       "min_samples_leaf": np.array([100])}]
    rf = GridSearchCV(RandomForestClassifier(50, max_depth=10,
                                             class_weight="auto", n_jobs=-1),
              param_grid_rf, cv=kf, n_jobs=-1)
    rf = RandomForestClassifier(100, max_depth=6, min_samples_leaf=200,
                                class_weight="auto", n_jobs=-1)
    rf.fit(X_all, all_labels)
    # print "best parameters for rf weights determination: ", rf.best_estimator_
    probas = rf.predict_proba(X_w)
    weights = probas[:, 1] / probas[:, 0]
    return weights


def estimate_weights_logistic_regresssion(X_s, X_t):
    """ estimate a logistic regressor to predict the probability of a sample
    to be generated by one class or the other.
    If one class is over or under represented weights will be adapted.

    Parameters:
        X_s: samples from the source domain
        X_t: samples from the target domain

    Returns:
        weigths for X_s """
    X_all, all_labels = prepare_data_for_weights_estimation(X_s, X_t)

    kf = KFold(X_all.shape[0], 10, shuffle=True)
    best_lr = LogisticRegressionCV(class_weight="auto",
                                   Cs=np.logspace(4, 8, 10),
                                   fit_intercept=False)
    best_lr.fit(X_all, all_labels)

    weights = X_s.shape[0] / X_t.shape[0] * np.exp(np.dot(X_s, best_lr.coef_.T)
                                                   + best_lr.intercept_)
    return weights


def resample(X, y, w, nr_samples=None):
    """bootstrapping: resample with replacement according to weights

    Returns:
        (X_new, w_new): the chosen samples and the new weights.
            by design these new weights are all equal to 1."""
    if (nr_samples is None):
        nr_samples = X.shape[0]
    w = w / np.sum(w)  # normalize
    # create index array with samples to draw:
    total_nr_samples = X.shape[0]  # nr total samples
    chosen_samples = np.random.choice(total_nr_samples,
                                      size=nr_samples,
                                      replace=True, p=np.squeeze(w))
    if y.ndim == 1:
        y_chosen = y[chosen_samples]
    else:
        y_chosen = y[chosen_samples, :]
    return X[chosen_samples, :], y_chosen, np.ones(nr_samples)
