import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

# Загрузка данных
close_prices = pd.read_csv("close_prices.csv")
djia = pd.read_csv("djia_index.csv")

# Удаляем столбец даты
X = close_prices.drop("date", axis=1)

# PCA
pca = PCA(n_components=10)
pca.fit(X)

# 1. Сколько компонент объясняют >= 90% дисперсии
cum_var = np.cumsum(pca.explained_variance_ratio_)
n_components = np.argmax(cum_var >= 0.9) + 1

print("Компонент:", n_components)

# 2. Первая главная компонента
first_component = pca.transform(X)[:, 0]

# 3. Корреляция с индексом Доу-Джонса
corr = np.corrcoef(first_component, djia["^DJI"])[0, 1]

print("Корреляция:", corr)

# 4. Компания с максимальным весом
weights = pca.components_[0]
company = X.columns[np.argmax(np.abs(weights))]

print("Компания:", company)