import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv("emotion1000.csv")
df = df.rename(columns={df.columns[1]:"emotion", df.columns[4]:"x", df.columns[5]:"y"})

outliers = []


for emo, group in df.groupby("emotion"):
    
    cx, cy = group["x"].mean(), group["y"].mean()

    dists = np.sqrt((group["x"] - cx)**2 + (group["y"] - cy)**2)

    threshold = np.percentile(dists, 95)

    group_outliers = group[dists > threshold].copy()
    outliers.append(group_outliers)

df_outliers = pd.concat(outliers)

fig = px.scatter(
    df_outliers,
    x="x", y="y",
    color="emotion",           
    hover_data=["emotion"],
    title="Outliers (5% más lejanos) por emoción"
)

fig.show()
