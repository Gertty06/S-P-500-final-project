"""Random forest model.

Owner: Member 4 (ML Engineer, random forest & app). Skeleton: to be implemented.
"""
import pandas as pd


def build_forest():
    """Return an untrained random forest regressor with fit(X, y) and predict(X).

    Monthly returns are very noisy, so keep overfitting in mind when
    choosing tree depth and leaf size. Use the random seed from config.py.
    """
    raise NotImplementedError("Member 4: implement build_forest")


def tune_forest(X_train, y_train):
    """Choose settings (e.g. depth, leaf size, number of trees) using
    split.tuning_folds() on the training years only. Return the best model.
    """
    raise NotImplementedError("Member 4: implement tune_forest")


def feature_importance(model, X, y) -> pd.Series:
    """Return one importance value per feature, largest first.

    This feeds the plan's bar chart of which indicators mattered most.
    """
    raise NotImplementedError("Member 4: implement feature_importance")
