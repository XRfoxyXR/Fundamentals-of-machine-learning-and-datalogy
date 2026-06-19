import pandas as pd
import os

from sklearn.tree import DecisionTreeClassifier

# Создание каталога
os.makedirs("Otvet", exist_ok=True)

# Загрузка данных
data = pd.read_csv("titanic/train.csv", index_col="PassengerId")

# Сбор признаков
features = data[["Pclass", "Fare", "Age", "Sex"]]

# Переменная 
target = data["Survived"]

# Замена пола на цифры
features = features.copy()
features["Sex"] = features["Sex"].map({
    "male": 0,
    "female": 1
})

# Объединение признаков 
dataset = features.copy()
dataset["Survived"] = target

# Удаление пропусков
dataset = dataset.dropna()

# Отделение признаков
X = dataset[["Pclass", "Fare", "Age", "Sex"]]
y = dataset["Survived"]

# Обучающее дерево
clf = DecisionTreeClassifier(random_state=241)
clf.fit(X, y)

# Получаем важности признаков
importances = clf.feature_importances_

# Сопоставление названия и важности
feature_importances = pd.Series(
    importances,
    index=X.columns
)

# Самые важные
top_features = feature_importances.sort_values(ascending=False).head(2)

answer = ",".join(top_features.index)

# Сохранение
with open("Otvet/answer.txt", "w", encoding="utf-8") as file:
    file.write(answer)

# вывод
print("Важность признаков:")
print(feature_importances)

print("\nОтвет:")
print(answer)

print("\nОтвет сохранен в файл Otvet/answer.txt")