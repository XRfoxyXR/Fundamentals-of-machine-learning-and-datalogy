import pandas as pd
import os

from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

os.makedirs("Otvet", exist_ok=True)

train = pd.read_csv("perceptron-train.csv")
test = pd.read_csv("perceptron-test.csv")

y_train = train.iloc[:, 0]
X_train = train.iloc[:, 1:]

y_test = test.iloc[:, 0]
X_test = test.iloc[:, 1:]

clf = Perceptron(random_state=241)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)
accuracy_before = accuracy_score(y_test, pred)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = Perceptron(random_state=241)
clf.fit(X_train_scaled, y_train)

pred_scaled = clf.predict(X_test_scaled)
accuracy_after = accuracy_score(y_test, pred_scaled)

answer = round(
    accuracy_after - accuracy_before,
    3
)

with open("Otvet/answer.txt", "w") as file:
    file.write(str(answer))

print("До нормализации:", accuracy_before)
print("После нормализации:", accuracy_after)
print("Ответ:", answer)