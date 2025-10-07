import pandas as pd
import plotly.express as px

df = pd.read_csv("emotion1000.csv")
df = df.rename(columns={df.columns[1]:"emotion", df.columns[4]:"x", df.columns[5]:"y"})
emotions = df["emotion"].unique()

df["x_quartile"] = pd.qcut(df["x"], q=4, labels=["Q1","Q2","Q3","Q4"])

counts = df.groupby(["emotion","x_quartile"]).size().reset_index(name="count")
dominant = counts.loc[counts.groupby("emotion")["count"].idxmax()]
dominant = dominant[["emotion","x_quartile"]]
dominant_sorted = dominant.sort_values(
    by=["x_quartile", "emotion"],
    key=lambda col: col.map({"Q1":1, "Q2":2, "Q3":3, "Q4":4}) if col.name=="x_quartile" else col
)

print(dominant_sorted[["x_quartile","emotion"]])
df = df.merge(dominant, on="emotion", how="left", suffixes=("","_dominant"))

max_points = 2000
df_limited = (
    df.groupby("x_quartile_dominant", group_keys=False)
      .apply(lambda g: g.sample(n=min(len(g), max_points), random_state=42))
)


fig = px.scatter(df_limited, x="x", y="y",
                 color="x_quartile_dominant", hover_data=["emotion"])
fig.show()
