import pandas as pd
import plotly.express as px

df = pd.read_csv("emotion1000.csv")
df = df.rename(columns={df.columns[1]:"emotion", df.columns[4]:"x", df.columns[5]:"y"})
emotions = df["emotion"].unique()

def plot(selected):
    filt = df[df["emotion"].isin(selected)]
    fig = px.scatter(filt, x="x", y="y", color="emotion", opacity=alpha)
    fig.show()

plot(emotions)
