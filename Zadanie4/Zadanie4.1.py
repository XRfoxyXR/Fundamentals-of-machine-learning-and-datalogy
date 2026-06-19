import numpy as np
import pandas as pd
import os

from sklearn.preprocessing import scale
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold, cross_val_score

os.makedirs("Otvet", exist_ok=True)

data_url = "http://lib.stat.cmu.edu/datasets/boston"

raw_df = pd.read_csv(
    data_url,
    sep=r"\s+",
    skiprows=22,
    header=None
)

X = np.hstack([
    raw_df.values[::2, :],
    raw_df.values[1::2, :2]
])

y = raw_df.values[1::2, 2]

X = scale(X)

# Кросс-валидация
kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

p_values = np.linspace(1, 10, 200)

best_p = None
best_score = -999999

for p in p_values:
    model = KNeighborsRegressor(
        n_neighbors=5,
        weights="distance",
        metric="minkowski",
        p=p
    )

    scores = cross_val_score(
        model,
        X,
        y,
        cv=kf,
        scoring="neg_mean_squared_error"
    )

    mean_score = scores.mean()

    if mean_score > best_score:
        best_score = mean_score
        best_p = p

answer = str(round(best_p, 1))

with open("Otvet/answer.txt", "w", encoding="utf-8") as file:
    file.write(answer)

print("Лучший p:", best_p)
print("Ответ:", answer)
print("Файл сохранен: Otvet/answer.txt")