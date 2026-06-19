import pandas as pd
import re
import os

# Каталог ответов
os.makedirs("Otvet", exist_ok=True)

# Загрузка
data = pd.read_csv("titanic/train.csv", index_col="PassengerId")

# Задание 1
sex_counts = data["Sex"].value_counts()

answer1 = f"{sex_counts['male']} {sex_counts['female']}"

# Задание 2
survived_percent = round(data["Survived"].mean() * 100, 2)

answer2 = str(survived_percent)

# Задание 3
first_class_percent = round((data["Pclass"] == 1).mean() * 100, 2)

answer3 = str(first_class_percent)

# Задание 4
mean_age = round(data["Age"].mean(), 2)
median_age = round(data["Age"].median(), 2)

answer4 = f"{mean_age} {median_age}"

# Задание 5
correlation = round(data["SibSp"].corr(data["Parch"]), 2)

answer5 = str(correlation)

# Задание 6
female_data = data[data["Sex"] == "female"]

names = []

for full_name in female_data["Name"]:

    if "(" in full_name:
        match = re.search(r"\((.*?)\)", full_name)

        if match:
            first_name = match.group(1).split()[0]
            names.append(first_name)

    else:
        match = re.search(r"Miss\.\s+([A-Za-z]+)", full_name)

        if match:
            first_name = match.group(1)
            names.append(first_name)

popular_name = pd.Series(names).value_counts().idxmax()

answer6 = popular_name

# Сохранение ответы
answers = [
    answer1,
    answer2,
    answer3,
    answer4,
    answer5,
    answer6
]

for i, answer in enumerate(answers, start=1):
    with open(
        f"Otvet/answer{i}.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(str(answer))

# Уведомленя
print("Задание 1:", answer1)
print("Задание 2:", answer2)
print("Задание 3:", answer3)
print("Задание 4:", answer4)
print("Задание 5:", answer5)
print("Задание 6:", answer6)

print("\nВсе ответы сохранены в каталог 'Otvet'.")