"""Charts for the report.

Owner: Member 3 (ML Engineer, linear regression & visualization).
Skeleton: to be implemented.

The project plan names two plots. Save every plot as a PNG in config.RESULTS_DIR.
"""
import pandas as pd


def plot_predicted_vs_actual(predictions: pd.DataFrame, path) -> None:
    """Line plot of predicted vs. actual monthly returns over the test years.

    predictions: monthly index; one column "actual" plus one column per model
    (for example "baseline", "linear", "forest").
    """
    raise NotImplementedError("Member 3: implement plot_predicted_vs_actual")


def plot_feature_importance(importance: pd.Series, path) -> None:
    """Bar chart of which economic indicators influenced returns the most.

    importance: the Series from random_forest.feature_importance().
    """
    raise NotImplementedError("Member 3: implement plot_feature_importance")
