import numpy as np
import matplotlib.pyplot as plt
'''
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)

plt.figure(figsize=(8, 8))
plt.scatter(x, y, alpha=0.6)
plt.scatter(0, 0, c='red', s=100)

# Окружности
circle_99 = plt.Circle((0, 0), 2.58, color='green', fill=False, linestyle='--')
plt.gca().add_patch(circle_99)

circle_3sigma = plt.Circle((0, 0), 3, color='orange', fill=False, linestyle='--')
plt.gca().add_patch(circle_3sigma)

plt.axis('equal')
plt.grid(True)
plt.show()
'''
# Генерация точек
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)

# График
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

# Основной график
ax2.scatter(x, y, alpha=0.6)
ax2.scatter(0, 0, c='red', s=100)
circle = plt.Circle((0, 0), 3, color='orange', fill=False, linestyle='--')
ax2.add_patch(circle)
ax2.set_xlim(-6, 6)
ax2.set_ylim(-6, 6)
ax2.set_aspect('equal')

# Гистограммы
ax1.hist(x, bins=10, density=True, alpha=0.6)
ax4.hist(y, bins=10, density=True, alpha=0.6)

# Пустой график
ax3.axis('off')

plt.tight_layout()
plt.show()