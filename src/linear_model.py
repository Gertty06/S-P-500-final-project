"""Linear regression model.

Owner: Member 3 (ML Engineer, linear regression & visualization).
Skeleton: to be implemented.
"""
import pandas as pd


def build_linear():
    """Return an untrained linear regression model with fit(X, y) and predict(X).

    Any preprocessing (such as feature scaling) must be fit on training data
    only. Wrapping it in a scikit-learn Pipeline makes that automatic.
    """
    raise NotImplementedError("Member 3: implement build_linear")


def tune_linear(X_train, y_train):
    """Optional: choose settings (e.g. Ridge/Lasso strength) using
    split.tuning_folds() on the training years only. Return the best model.
    """
    raise NotImplementedError("Member 3: implement tune_linear (optional)")


def explain_linear(model, feature_names) -> pd.Series:
    """Return one value per feature showing how it pushes the forecast
    up or down (e.g. coefficients on scaled features), largest first.
    """
    raise NotImplementedError("Member 3: implement explain_linear")
