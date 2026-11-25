"""Turn clean monthly data into model features and the prediction target.

Owner: Member 1 (Data & Features Engineer). Skeleton: to be implemented.

Input:  the DataFrame from data.load_clean()
Output: one DataFrame, same monthly index, holding every feature column
        plus the target column TARGET, with incomplete rows removed.

Rule that must always hold: a feature for month t may only use information
that was public at the end of month t. Earnings and dividends are published
months late, so account for that delay.
"""
import pandas as pd

TARGET = "next_ret"   # next month's % return, as set out in the project plan
FEATURES: list[str] = []  # TODO(Member 1): list the feature column names you choose


def make_target(df: pd.DataFrame) -> pd.Series:
    """Next month's % return for every month: price(t+1) / price(t) - 1.

    Returns a Series on the same index as df. The last month has no
    next month, so its value is missing.
    """
    raise NotImplementedError("Member 1: implement make_target")


def make_features(df: pd.DataFrame) -> pd.DataFrame:
    """Build the input features from the clean data.

    Returns a DataFrame on the same index, with exactly the columns in FEATURES.
    The team decides which features to use; document each one in the README's
    data dictionary.
    """
    raise NotImplementedError("Member 1: implement make_features")


def build_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Features and target in one table, with rows that have missing values dropped.

    This is the table every other module works from.
    """
    raise NotImplementedError("Member 1: implement build_dataset")
