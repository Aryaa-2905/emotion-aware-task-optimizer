import pandas as pd

df = pd.read_csv("emotion_logs.csv")
print(df.groupby("emotion").count())
