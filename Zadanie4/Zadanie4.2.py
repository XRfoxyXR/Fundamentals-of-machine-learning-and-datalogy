import pandas as pd
import os

from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale

os.makedirs("Otvet", exist_ok=True)

data = pd.read_csv(
    "wine.data",
    header=None
)

y = data[0]

X = data.loc[:, 1:]

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = {}

for k in range(1, 51):

    model = KNeighborsClassifier(
        n_neighbors=k
    )

    cv_scores = cross_val_score(
        model,
        X,
        y,
        cv=kf,
        scoring="accuracy"
    )

    scores[k] = cv_scores.mean()

best_k = max(scores, key=scores.get)
best_score = scores[best_k]

X_scaled = scale(X)

scores_scaled = {}

for k in range(1, 51):

    model = KNeighborsClassifier(
        n_neighbors=k
    )

    cv_scores = cross_val_score(
        model,
        X_scaled,
        y,
        cv=kf,
        scoring="accuracy"
    )

    scores_scaled[k] = cv_scores.mean()

best_k_scaled = max(scores_scaled, key=scores_scaled.get)
best_score_scaled = scores_scaled[best_k_scaled]

answers = [
    str(best_k),
    str(round(best_score, 2)),
    str(best_k_scaled),
    str(round(best_score_scaled, 2))
]

for i, answer in enumerate(answers, start=1):
    with open(f"Otvet/answer{i}.txt", "w") as file:
        file.write(answer)

print("Ответ 1:", best_k)
print("Ответ 2:", round(best_score, 2))
print("Ответ 3:", best_k_scaled)
print("Ответ 4:", round(best_score_scaled, 2))