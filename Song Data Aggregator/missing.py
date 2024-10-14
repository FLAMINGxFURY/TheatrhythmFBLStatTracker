import pandas as pd

# import data
df = pd.read_csv("Combined Data.csv")

# create a list of titles that are missing data from trig_basic
missing_name = df[df["trig_basic"].isnull()]["eng_name"].tolist()
missing_series = df[df["trig_basic"].isnull()]["series"].tolist()
missing_ms_type = df[df["trig_basic"].isnull()]["ms_type"].tolist()

missing = zip(missing_name, missing_series, missing_ms_type)

# write to text file
with open("missing.txt", "w", encoding="utf-8") as f:
    for name, series, ms_type in missing:
        f.write(f"{series} | {ms_type} | {name}\n")