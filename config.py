"""Project-wide settings. Owner: Member 2 (ML Lead).

Keep every setting the team shares here, so nobody hard-codes values
inside the modules.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW_CSV = ROOT / "data" / "raw" / "data.csv"
PROCESSED_DIR = ROOT / "data" / "processed"
RESULTS_DIR = ROOT / "results"

DATA_URL = "https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv"

# TODO(Member 2): add the shared settings the team agrees on, for example:
#   - train/test split dates (project plan: train before 2010, test 2011 onward)
#   - reporting lag for earnings and dividends
#   - random seed
