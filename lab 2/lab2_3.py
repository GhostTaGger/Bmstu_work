import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# === Загрузка данных из CSV вручную ===
with open('iris.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
    rows = list(reader)

# === Извлечение числовых данных ===
data = []
for i, row in enumerate(rows):
    if len(row) < 4:
        print(f"Пропущена строка {i}: недостаточно данных -> {row}")
        continue
    try:
        numeric_row = [float(val) for val in row[:4]]
        data.append(numeric_row)
    except ValueError as e:
        print(f"Пропущена строка {i}: невозможно преобразовать в float -> {row}")
        continue

# Преобразуем в numpy array
data = np.array(data)

print(f"Загружено {len(data)} строк данных.")

# === Корреляционная матрица ===
data_T = data.T
corr = np.corrcoef(data_T)

# Подписи осей
feature_names = headers[:4]

# === 2. Тепловая карта с помощью seaborn.heatmap ===
import pandas as pd

# Преобразуем в DataFrame для удобства
df = pd.DataFrame(data, columns=feature_names)

# Вычисляем корреляционную матрицу
corr = df.corr()

# Строим тепловую карту
plt.figure(figsize=(10, 8))
sns.heatmap(
    corr,
    annot=True,           # Отображать значения в ячейках
    fmt=".2f",            # Формат чисел
    cmap="RdYlGn",        # Цвета: красный - отрицательная, зелёный - положительная
    center=0,             # Центр цветовой шкалы
    square=True,          # Квадратные ячейки
    cbar_kws={'label': 'Корреляция'}
)

plt.title("Тепловая карта корреляций (seaborn)", fontsize=14)
plt.tight_layout()
plt.show()