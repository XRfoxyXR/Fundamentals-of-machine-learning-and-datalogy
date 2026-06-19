import pandas as pd
import numpy as np
import os
from sklearn.metrics import roc_auc_score

os.makedirs("Otvet", exist_ok=True)

# Загрузка данных
data = pd.read_csv(
    "logistic.csv",
    header=None
)

y = data[0]
X1 = data[1]
X2 = data[2]

# Градиентный спуск
def gradient_descent(C):
    w1 = 0.0
    w2 = 0.0

    k = 0.1
    eps = 1e-5
    max_iter = 10000

    for _ in range(max_iter):

        w1_old = w1
        w2_old = w2

        s1 = 0
        s2 = 0

        for i in range(len(y)):
            yi = y.iloc[i]
            xi1 = X1.iloc[i]
            xi2 = X2.iloc[i]

            margin = yi * (w1 * xi1 + w2 * xi2)

            coef = yi * (1 - 1 / (1 + np.exp(-margin)))

            s1 += xi1 * coef
            s2 += xi2 * coef

        w1 += k * (s1 / len(y) - C * w1)
        w2 += k * (s2 / len(y) - C * w2)

        distance = np.sqrt(
            (w1 - w1_old) ** 2 +
            (w2 - w2_old) ** 2
        )

        if distance <= eps:
            break

    return w1, w2


# Без регуляризации
w1, w2 = gradient_descent(0)

scores = 1 / (
    1 + np.exp(-(w1 * X1 + w2 * X2))
)

auc_no_reg = roc_auc_score(y, scores)

# С регуляризацией
w1_reg, w2_reg = gradient_descent(10)

scores_reg = 1 / (
    1 + np.exp(-(w1_reg * X1 + w2_reg * X2))
)

auc_reg = roc_auc_score(y, scores_reg)

answer = (
    f"{round(auc_no_reg, 3)} "
    f"{round(auc_reg, 3)}"
)

with open(
    "Otvet/answer.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(answer)

print("AUC без регуляризации:", round(auc_no_reg, 3))
print("AUC с регуляризацией:", round(auc_reg, 3))
print("Ответ:", answer)