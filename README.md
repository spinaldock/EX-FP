# Experiments on Database for Cluster Visualization
The idea here is to show how the data after an embedding can be used to visualize ceirtain clusters. In this case there are 3 types of clusterization that are used:

1. Quartiles.- Sorting one dimension of the vectors and dividing it into quartiles; each emotion was assigned to the quartile with the majority of its samples.

2. Semantics.- Grouping the 39 original emotions into Plutchik's eight primary emotions: Joy (joy, happiness, fun, amusement, excitement), Trust (love, caring, admiration, approval), Fear (fear, nervousness, worry) Surprise (surprise, realization, confusion, curiosity), Sadness (sadness, grief, disappointment, remorse, guilt, shame, emptiness, boredom, embarrassment), Disgust (disgust, disapproval, annoyance, hate), Anger (anger), and Anticipation (optimism, enthusiasm, desire)

3. Outliers.- Identifying whether the 5\% of the samples farthest from the centroid of each emotion cluster were grouped in a meaningful way.
