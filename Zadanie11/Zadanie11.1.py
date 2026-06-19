import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score

data = pd.read_csv("abalone.csv")

data["Sex"] = data["Sex"].map(
    lambda x: 1 if x == "M" else (-1 if x == "F" else 0)
)

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=1
)

for k in range(1, 51):
    clf = RandomForestRegressor(
        n_estimators=k,
        random_state=1
    )

    score = cross_val_score(
        clf,
        X,
        y,
        cv=kf,
        scoring="r2"
    ).mean()

    print(k, score)

    if score > 0.52:
        print("Ответ:", k)
        break