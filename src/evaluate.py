"""The baseline model and the one shared scoring function.

Owner: Member 2 (ML Lead). Skeleton: to be implemented.

Every model in the project is scored with evaluate(), so comparisons are fair.
"""


class HistoricalMeanBaseline:
    """Baseline from the project plan: always predicts the average return
    seen in the training data.

    Must follow the scikit-learn style so it can be used like the real models:
        fit(X, y) -> self
        predict(X) -> array with one prediction per row of X
    """

    def fit(self, X, y):
        raise NotImplementedError("Member 2: implement HistoricalMeanBaseline.fit")

    def predict(self, X):
        raise NotImplementedError("Member 2: implement HistoricalMeanBaseline.predict")


def evaluate(name: str, y_true, y_pred, baseline_pred) -> dict:
    """Score one model's test predictions.

    Returns a dict with "model": name plus the metrics the team agrees on.
    Must include at least one error metric (e.g. RMSE or MAE) and one number
    that says directly whether the model beat the baseline.
    """
    raise NotImplementedError("Member 2: implement evaluate")
