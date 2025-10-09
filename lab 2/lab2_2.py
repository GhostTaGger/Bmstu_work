import csv
import matplotlib.pyplot as plt
import numpy as np

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

# === 1. Тепловая карта с помощью matplotlib ===
plt.figure(figsize=(10, 8))
im = plt.imshow(corr, cmap='RdYlGn', vmin=-1, vmax=1)

plt.xticks(range(len(feature_names)), feature_names, rotation=45)
plt.yticks(range(len(feature_names)), feature_names)

plt.colorbar(im)
plt.title("Тепловая карта корреляций (matplotlib)")
plt.tight_layout()
plt.show()

