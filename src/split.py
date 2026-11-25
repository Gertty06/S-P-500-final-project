"""Split the dataset by time into training and test sets.

Owner: Member 2 (ML Lead). Skeleton: to be implemented.

Project plan: train on data before 2010, test on 2011 onward. Never shuffle.
"""
import pandas as pd


def time_split(data: pd.DataFrame):
    """Split the table from features.build_dataset() by date.

    Returns (X_train, y_train, X_test, y_test):
        X_* are DataFrames of feature columns, y_* are Series of the target.
    Must guarantee every training month comes before every test month.
    Split dates come from config.py.
    """
    raise NotImplementedError("Member 2: implement time_split")


def tuning_folds(n_splits: int = 5):
    """Cross-validation folds for tuning, used only inside the training years.

    Each fold must train on earlier months and validate on later ones
    (for example sklearn's TimeSeriesSplit). Members 3 and 4 both use this,
    so their tuning is comparable.
    """
    raise NotImplementedError("Member 2: implement tuning_folds")
