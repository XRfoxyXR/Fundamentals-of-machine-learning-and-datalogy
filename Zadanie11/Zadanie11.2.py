import pandas as pd
import numpy as np
import os

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

os.makedirs("Otvet", exist_ok=True)

data = pd.read_csv("gbm-data.csv").values

X = data[:, 1:]
y = data[:, 0]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.8,
    random_state=241
)

learning_rates = [1, 0.5, 0.3, 0.2, 0.1]

best_result_lr_02 = None

for learning_rate in learning_rates:
    clf = GradientBoostingClassifier(
        n_estimators=250,
        verbose=False,
        random_state=241,
        learning_rate=learning_rate
    )

    clf.fit(X_train, y_train)

    test_loss = []

    for y_pred in clf.staged_decision_function(X_test):
        y_pred = y_pred.ravel()
        probability = 1 / (1 + np.exp(-y_pred))
        test_loss.append(log_loss(y_test, probability))

    min_loss = min(test_loss)
    best_iter = test_loss.index(min_loss) + 1

    print("learning_rate =", learning_rate)
    print("Минимальный log-loss:", round(min_loss, 2))
    print("Итерация:", best_iter)
    print()

    if learning_rate == 0.2:
        best_result_lr_02 = (min_loss, best_iter)

# Ответ 1
answer1 = "overfitting"

# Ответ 2
loss_02, iter_02 = best_result_lr_02
answer2 = f"{loss_02:.2f} {iter_02}"

# Случайный лес
rf = RandomForestClassifier(
    n_estimators=iter_02,
    random_state=241
)

rf.fit(X_train, y_train)

rf_pred = rf.predict_proba(X_test)[:, 1]
rf_loss = log_loss(y_test, rf_pred)

answer3 = f"{rf_loss:.2f}"

with open("Otvet/answer1.txt", "w", encoding="utf-8") as f:
    f.write(answer1)

with open("Otvet/answer2.txt", "w", encoding="utf-8") as f:
    f.write(answer2)

with open("Otvet/answer3.txt", "w", encoding="utf-8") as f:
    f.write(answer3)

print("Ответ 1:", answer1)
print("Ответ 2:", answer2)
print("Ответ 3:", answer3)