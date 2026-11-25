"""Run the whole project end to end:  python run_pipeline.py

Owner: Member 2 (ML Lead). Skeleton: to be implemented.

Expected order (each step uses the module that owns it):
    1. data.load_clean()                      Member 1 (done)
    2. features.build_dataset()               Member 1
    3. split.time_split()                     Member 2
    4. fit the baseline, linear and forest    Members 2, 3, 4
    5. evaluate.evaluate() for every model    Member 2
    6. plots.* and save results/              Member 3
    7. save trained models for the app        Member 4

Outputs go to results/: a metrics table, test-year predictions, the two
plots, and the saved models. Also append each run to the experiment log.
"""
from src.data import describe, load_clean


def main():
    df = load_clean()
    print("Data:", describe(df))
    # TODO(Member 2): add steps 2-7 above as each module is finished.
    raise NotImplementedError("Member 2: complete the pipeline steps")


if __name__ == "__main__":
    main()
