import pandas as pd
import re
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Ridge
from scipy.sparse import hstack

os.makedirs("Otvet", exist_ok=True)

train = pd.read_csv("salary-train.csv")
test = pd.read_csv("salary-test-mini.csv")

train["FullDescription"] = train["FullDescription"].apply(
    lambda text: re.sub("[^a-zA-Z0-9]", " ", text.lower())
)

test["FullDescription"] = test["FullDescription"].apply(
    lambda text: re.sub("[^a-zA-Z0-9]", " ", text.lower())
)

vectorizer = TfidfVectorizer(min_df=5)

X_train_text = vectorizer.fit_transform(train["FullDescription"])
X_test_text = vectorizer.transform(test["FullDescription"])

train["LocationNormalized"] = train["LocationNormalized"].fillna("nan")
train["ContractTime"] = train["ContractTime"].fillna("nan")

test["LocationNormalized"] = test["LocationNormalized"].fillna("nan")
test["ContractTime"] = test["ContractTime"].fillna("nan")

enc = DictVectorizer()

X_train_categ = enc.fit_transform(
    train[["LocationNormalized", "ContractTime"]].to_dict("records")
)

X_test_categ = enc.transform(
    test[["LocationNormalized", "ContractTime"]].to_dict("records")
)

X_train = hstack([X_train_text, X_train_categ])
X_test = hstack([X_test_text, X_test_categ])

y_train = train["SalaryNormalized"]

model = Ridge(alpha=1)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

answer = f"{predictions[0]:.2f} {predictions[1]:.2f}"

with open("Otvet/answer.txt", "w", encoding="utf-8") as file:
    file.write(answer)

print("Ответ:", answer)