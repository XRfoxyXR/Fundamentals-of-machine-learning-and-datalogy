import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    precision_recall_curve
)

# Часть 1 
data = pd.read_csv("classification.csv")

y_true = data["true"]
y_pred = data["pred"]

TP = ((y_true == 1) & (y_pred == 1)).sum()
FP = ((y_true == 0) & (y_pred == 1)).sum()
FN = ((y_true == 1) & (y_pred == 0)).sum()
TN = ((y_true == 0) & (y_pred == 0)).sum()

print("TP FP FN TN:")
print(TP, FP, FN, TN)

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1:", f1_score(y_true, y_pred))

# Часть 2
scores = pd.read_csv("scores.csv")

y = scores["true"]

classifiers = [
    "score_logreg",
    "score_svm",
    "score_knn",
    "score_tree"
]

print("\nAUC-ROC:")

best_auc = 0
best_auc_name = ""

for clf in classifiers:
    auc = roc_auc_score(y, scores[clf])
    print(clf, auc)

    if auc > best_auc:
        best_auc = auc
        best_auc_name = clf

print("\nЛучший AUC:")
print(best_auc_name)

print("\nPrecision при Recall >= 0.7:")

best_precision = 0
best_precision_name = ""

for clf in classifiers:

    precision, recall, thresholds = precision_recall_curve(
        y,
        scores[clf]
    )

    current_precision = precision[recall >= 0.7].max()

    print(clf, current_precision)

    if current_precision > best_precision:
        best_precision = current_precision
        best_precision_name = clf

print("\nЛучший Precision:")
print(best_precision_name)
print(best_precision)