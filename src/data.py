"""Load and clean the raw monthly S&P 500 dataset.

Owner: Member 1 (Data & Features Engineer). Implemented; maintain it.

Source: the public "s-and-p-500" dataset on GitHub (Robert Shiller's data),
one row per month. Raw columns:
    Date, SP500, Dividend, Earnings, Consumer Price Index,
    Long Interest Rate, Real Price, Real Dividend, Real Earnings, PE10

Output of load_clean(): a DataFrame with a monthly DatetimeIndex named "Date"
and these columns, all strictly positive:
    price, dividend, earnings, cpi, long_rate, pe10
"""
import urllib.request

import pandas as pd

import config

# Raw column name -> name used everywhere else in the project.
COLUMNS = {
    "SP500": "price",
    "Dividend": "dividend",
    "Earnings": "earnings",
    "Consumer Price Index": "cpi",
    "Long Interest Rate": "long_rate",
    "PE10": "pe10",
}

# The dataset stores missing values as 0 (PE10 before 1881, and every column
# except the price after mid-2023). A 0 in these columns means "unknown".
ZERO_MEANS_MISSING = ["dividend", "earnings", "cpi", "long_rate", "pe10"]


def download_raw(force: bool = False) -> None:
    """Download data.csv into data/raw/ unless it is already there.

    The repo ships with a snapshot so everyone trains on the same data.
    Use force=True only when the team agrees to refresh it.
    """
    if config.RAW_CSV.exists() and not force:
        return
    config.RAW_CSV.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(config.DATA_URL, config.RAW_CSV)


def load_raw() -> pd.DataFrame:
    """Read the raw CSV, indexed by month and sorted oldest to newest."""
    download_raw()
    df = pd.read_csv(config.RAW_CSV, parse_dates=["Date"])
    return df.set_index("Date").sort_index()


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Keep the columns we use, rename them, and drop months with missing values."""
    df = df[list(COLUMNS)].rename(columns=COLUMNS)
    if df.index.duplicated().any():
        raise ValueError("raw data has duplicate months")
    complete = (df[ZERO_MEANS_MISSING] > 0).all(axis=1)
    return df[complete & (df["price"] > 0)]


def load_clean() -> pd.DataFrame:
    """Main entry point for the rest of the project."""
    return clean(load_raw())


def describe(df: pd.DataFrame) -> str:
    """Short data report: rows, date range, and any missing months inside the range."""
    expected = pd.date_range(df.index.min(), df.index.max(), freq="MS")
    gaps = expected.difference(df.index)
    return (
        f"{len(df)} months, {df.index.min():%Y-%m} to {df.index.max():%Y-%m}; "
        f"{len(gaps)} missing months inside the range"
    )


if __name__ == "__main__":
    print(describe(load_clean()))
