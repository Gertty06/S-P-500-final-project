# S&P 500 ML Stock Predictor (CP322)

Predict next month's S&P 500 return from monthly market and economic data,
compare **linear regression** and a **random forest** against a
**historical-average baseline**, and show the result in a simple app for
beginner investors. Educational tool, not financial advice.

**Status:** skeleton. Only `src/data.py` is implemented. Every other file
defines its functions, inputs, outputs and rules, and raises
`NotImplementedError` until its owner builds it. How each piece is
implemented is up to its owner, as long as it keeps the contracts below.

## Architecture

```
sp500-ml-predictor/
├── config.py            shared settings: paths, split dates, seed      (Member 2)
├── run_pipeline.py      runs every step in order, saves results/        (Member 2)
├── src/
│   ├── data.py          load + clean the raw CSV           DONE         (Member 1)
│   ├── features.py      features + target                               (Member 1)
│   ├── split.py         time-based train/test split, tuning folds       (Member 2)
│   ├── evaluate.py      baseline model + shared scoring                 (Member 2)
│   ├── linear_model.py  linear regression                               (Member 3)
│   ├── plots.py         the plan's two charts                           (Member 3)
│   └── random_forest.py random forest + feature importance              (Member 4)
├── app/app.py           Streamlit app for users                         (Member 4)
├── tests/               data tests (passing) + contract checks (skipped)
├── data/raw/data.csv    dataset snapshot, so everyone uses the same data
└── results/             outputs written by run_pipeline.py
```

## Data flow and contracts

Each step hands the next one a fixed shape of data. Keep these the same so
the pieces fit together; agree any change with the ML Lead first.

| Step | Function | Gives the next step |
|---|---|---|
| 1. Load | `data.load_clean()` | DataFrame, monthly `Date` index, columns `price, dividend, earnings, cpi, long_rate, pe10` (all > 0) |
| 2. Features | `features.build_dataset(df)` | Same index; one column per name in `FEATURES`, plus target `next_ret`; no missing values |
| 3. Split | `split.time_split(data)` | `X_train, y_train, X_test, y_test`; every training month before every test month |
| 4. Models | `build_linear()`, `build_forest()`, `HistoricalMeanBaseline()` | Objects with `fit(X, y)` and `predict(X)` (scikit-learn style) |
| 5. Score | `evaluate.evaluate(name, y_true, y_pred, baseline_pred)` | Dict of metrics for one model |
| 6. Show | `plots.*`, `app/app.py` | PNG charts in `results/`; the app reads saved results and models |

## Roles and expectations

Fill in names. Each person owns their files: they write them, keep them
working, and review any change someone else makes to them.

### Member 1: Data & Features Engineer — [Name]
**Owns:** `src/data.py` (done), `src/features.py`
- Maintain `data.py`; refresh the dataset snapshot only when the team agrees.
- Implement `make_target`, `make_features` and `build_dataset`.
- Choose the features, and write a data dictionary below (name, meaning, how it's built).
- Make sure no feature uses information from after month t, including reporting delays.
- Enable the two feature checks in `tests/test_contracts.py`.

**Done when:** `build_dataset()` returns the agreed table, the data dictionary is written, and the feature tests pass.

### Member 2: ML Lead — [Name]
**Owns:** `config.py`, `src/split.py`, `src/evaluate.py`, `run_pipeline.py`, `tests/`
- Set the shared settings in `config.py` (split dates from the plan, seed, and so on).
- Implement `time_split`, `tuning_folds`, `HistoricalMeanBaseline` and `evaluate`.
- Complete `run_pipeline.py` so one command produces every result.
- Keep an experiment log: one row per run with model, settings, features, scores and date.
- Run the final comparison on the test years once tuning is finished.

**Done when:** `python run_pipeline.py` runs end to end, the log is in use, and the split and baseline tests pass.

### Member 3: ML Engineer, linear regression & visualization — [Name]
**Owns:** `src/linear_model.py`, `src/plots.py`
- Implement `build_linear` and `explain_linear`; optionally `tune_linear` using `tuning_folds()`.
- Fit any preprocessing (such as scaling) on training data only.
- Implement the plan's two plots: predicted vs. actual returns, and feature importance.

**Done when:** the linear model is scored with `evaluate()` and logged, and both plots are saved to `results/`.

### Member 4: ML Engineer, random forest & app — [Name]
**Owns:** `src/random_forest.py`, `app/app.py`
- Implement `build_forest`, `tune_forest` (using `tuning_folds()`) and `feature_importance`.
- Watch for overfitting: compare training and validation scores.
- Build the Streamlit app: forecast, recent trend, model scores and a not-financial-advice note.

**Done when:** the tuned forest is scored and logged, importance values feed Member 3's chart, and the app runs from saved results.

### Everyone
- Write one section of the final report.
- Run `python -m pytest -q` before every pull request; get one teammate's review.

## Rules for the whole team

- Never shuffle the data. Training months always come before test months.
- Tune only inside the training years. Open the test years once, for the final comparison.
- Score every model with `evaluate()` and log every run.
- Known data limit: the economic columns end in mid-2023, so test data ends there too.

## Quick start

```bash
pip install -r requirements.txt
python -m src.data          # prints a short data report (works now)
python -m pytest -q         # data tests pass; contract checks are skipped for now
python run_pipeline.py      # stops with NotImplementedError until steps 2-7 exist
```

## Data dictionary

To be written by Member 1.

| Feature | Meaning | How it's built |
|---|---|---|
| | | |
