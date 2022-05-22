import pandas as pd
import glob 
import json

def fn2annotation(fn, annotator):
    df = pd.read_csv(fn)
    cols = {k: v for k,v in zip(df.columns, ["label", "text", "annotator", "a", "b"])}
    df = df.rename(columns=cols)
    df = df.iloc[1:]
    df = df[["text", "label"]]
    for i, j in zip(df["text"].to_list(), df["label"].to_list()):
        yield({"text": i, "label": j, "annotator": annotator})

with open("annotation.jsonl", "w") as of:
    for fno, fn in enumerate(glob.glob("submissions/*yelp*csv")):
        for d in fn2annotation(fn, fno):
            of.write(json.dumps(d) + "\n")