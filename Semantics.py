import pandas as pd
import plotly.express as px

df = pd.read_csv("emotion1000.csv")
df = df.rename(columns={df.columns[1]:"emotion", df.columns[4]:"x", df.columns[5]:"y"})
emotions = df["emotion"].unique()

basicas = {
    "curiosity":"surprise",
    "joy":"joy",
    "happiness":"joy",
    "happy":"joy",
    "fun":"joy",
    "amusement":"joy",
    "excitement":"joy",
    "optimism":"anticipation",
    "enthusiasm":"anticipation",
    "pride":"joy",
    "relief":"joy",
    "gratitude":"joy",
    "love":"trust",
    "caring":"trust",
    "admiration":"trust",
    "approval":"trust",
    "fear":"fear",
    "nervousness":"fear",
    "worry":"fear",
    "surprise":"surprise",
    "realization":"surprise",
    "confusion":"surprise",
    "sadness":"sadness",
    "sad":"sadness",
    "grief":"sadness",
    "disappointment":"sadness",
    "remorse":"sadness",
    "guilt":"sadness",
    "shame":"sadness",
    "empty":"sadness",
    "boredom":"sadness",
    "embarrassment":"sadness",
    "disgust":"disgust",
    "disapproval":"disgust",
    "annoyance":"disgust",
    "hate":"disgust",
    "anger":"anger",
    "desire":"anticipation"
}

df["basica"] = df["emotion"].map(basicas)

# Limitar puntos por categoría
max_points = 1000
df_limited = (
    df.groupby("basica", group_keys=False)
      .apply(lambda g: g.sample(n=min(len(g), max_points), random_state=42))
)

# Graficar
fig = px.scatter(df_limited, x="x", y="y", color="basica", hover_data=["emotion"])
fig.show()
