from numpy.random import RandomState
import pandas as pd


#filename = "google_review_ratings.csv"


df = pd.read_csv('google_review_ratings.csv')
rng = RandomState()

train = df.sample(frac=0.7, random_state=rng)
test = df.loc[~df.index.isin(train.index)]

print(test)
print(train)

train.to_csv("TrainingSet.csv")
test.to_csv("TestingSet.csv")
