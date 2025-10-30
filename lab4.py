import numpy as np
import matplotlib.pyplot as plt
import math

# Данные из варианта 4
x = np.array([2, 6, 10, 14, 18, 22])
y = np.array([3.1, 6.7, 9.5, 11.9, 14.0, 15.5])

print("Экспериментальные данные:")
print("x:", x)
print("y:", y)
print()

# 1.1 Линейная функция y = ax + b
print("1.1 Линейная функция y = ax + b")
print("=" * 50)

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_xy = np.sum(x * y)
n = len(x)

print(f"sum x = {sum_x}")
print(f"sum y = {sum_y}")
print(f"sum x2 = {sum_x2}")
print(f"sum xy = {sum_xy}")
print(f"n = {n}")

# Система уравнений
print("\nСистема уравнений:")
print(f"{sum_x2}a + {sum_x}b = {sum_xy}")
print(f"{sum_x}a + {n}b = {sum_y}")

# Решение методом Крамера
delta = sum_x2 * n - sum_x * sum_x
delta_a = sum_xy * n - sum_x * sum_y
delta_b = sum_x2 * sum_y - sum_xy * sum_x

print(f"\nDelta = {sum_x2}*{n} - {sum_x}*{sum_x} = {delta}")
print(f"Delta a = {sum_xy}*{n} - {sum_x}*{sum_y} = {delta_a}")
print(f"Delta b = {sum_x2}*{sum_y} - {sum_xy}*{sum_x} = {delta_b}")

a_linear = round(delta_a / delta, 2)
b_linear = round(delta_b / delta, 2)

print(f"\na = Delta a/Delta = {delta_a}/{delta} = {a_linear}")
print(f"b = Delta b/Delta = {delta_b}/{delta} = {b_linear}")
print(f"Уравнение: y = {a_linear}x + {b_linear}")
print()

# 1.2 Степенная функция y = beta * x^a
print("1.2 Степенная функция y = beta * x^a")
print("=" * 50)

ln_x = np.log(x)
ln_y = np.log(y)

print("ln(x):", [f"{val:.4f}" for val in ln_x])
print("ln(y):", [f"{val:.4f}" for val in ln_y])

sum_ln_x = np.sum(ln_x)
sum_ln_y = np.sum(ln_y)
sum_ln_x2 = np.sum(ln_x**2)
sum_ln_x_ln_y = np.sum(ln_x * ln_y)

print(f"\nsum ln(x) = {sum_ln_x:.4f}")
print(f"sum ln(y) = {sum_ln_y:.4f}")
print(f"sum ln2(x) = {sum_ln_x2:.4f}")
print(f"sum (ln(x)*ln(y)) = {sum_ln_x_ln_y:.4f}")

# Система уравнений
print(f"\nСистема уравнений:")
print(f"{sum_ln_x2:.4f}a + {sum_ln_x:.4f}b = {sum_ln_x_ln_y:.4f}")
print(f"{sum_ln_x:.4f}a + {n}b = {sum_ln_y:.4f}")

# Решение методом Крамера
delta_power = sum_ln_x2 * n - sum_ln_x * sum_ln_x
delta_a_power = sum_ln_x_ln_y * n - sum_ln_x * sum_ln_y
delta_b_power = sum_ln_x2 * sum_ln_y - sum_ln_x_ln_y * sum_ln_x

print(f"\nDelta = {sum_ln_x2:.4f}*{n} - {sum_ln_x:.4f}*{sum_ln_x:.4f} = {delta_power:.4f}")
print(f"Delta a = {sum_ln_x_ln_y:.4f}*{n} - {sum_ln_x:.4f}*{sum_ln_y:.4f} = {delta_a_power:.4f}")
print(f"Delta b = {sum_ln_x2:.4f}*{sum_ln_y:.4f} - {sum_ln_x_ln_y:.4f}*{sum_ln_x:.4f} = {delta_b_power:.4f}")

a_power = round(delta_a_power / delta_power, 2)
b_power = round(delta_b_power / delta_power, 2)
beta_power = round(math.exp(b_power), 2)

print(f"\na = Delta a/Delta = {delta_a_power:.4f}/{delta_power:.4f} = {a_power}")
print(f"b = Delta b/Delta = {delta_b_power:.4f}/{delta_power:.4f} = {b_power}")
print(f"beta = e^b = e^{b_power} = {beta_power}")
print(f"Уравнение: y = {beta_power} * x^{a_power}")
print()

# 1.3 Показательная функция y = beta * e^(ax)
print("1.3 Показательная функция y = beta * e^(ax)")
print("=" * 50)

print("x:", x)
print("ln(y):", [f"{val:.4f}" for val in ln_y])

sum_x_exp = sum_x
sum_ln_y_exp = sum_ln_y
sum_x2_exp = sum_x2
sum_x_ln_y = np.sum(x * ln_y)

print(f"\nsum x = {sum_x_exp}")
print(f"sum ln(y) = {sum_ln_y_exp:.4f}")
print(f"sum x2 = {sum_x2_exp}")
print(f"sum (x*ln(y)) = {sum_x_ln_y:.4f}")

# Система уравнений
print(f"\nСистема уравнений:")
print(f"{sum_x2_exp}a + {sum_x_exp}b = {sum_x_ln_y:.4f}")
print(f"{sum_x_exp}a + {n}b = {sum_ln_y_exp:.4f}")

# Решение методом Крамера
delta_exp = sum_x2_exp * n - sum_x_exp * sum_x_exp
delta_a_exp = sum_x_ln_y * n - sum_x_exp * sum_ln_y_exp
delta_b_exp = sum_x2_exp * sum_ln_y_exp - sum_x_ln_y * sum_x_exp

print(f"\nDelta = {sum_x2_exp}*{n} - {sum_x_exp}*{sum_x_exp} = {delta_exp}")
print(f"Delta a = {sum_x_ln_y:.4f}*{n} - {sum_x_exp}*{sum_ln_y_exp:.4f} = {delta_a_exp:.4f}")
print(f"Delta b = {sum_x2_exp}*{sum_ln_y_exp:.4f} - {sum_x_ln_y:.4f}*{sum_x_exp} = {delta_b_exp:.4f}")

a_exp = round(delta_a_exp / delta_exp, 2)
b_exp = round(delta_b_exp / delta_exp, 2)
beta_exp = round(math.exp(b_exp), 2)

print(f"\na = Delta a/Delta = {delta_a_exp:.4f}/{delta_exp} = {a_exp}")
print(f"b = Delta b/Delta = {delta_b_exp:.4f}/{delta_exp} = {b_exp}")
print(f"beta = e^b = e^{b_exp} = {beta_exp}")
print(f"Уравнение: y = {beta_exp} * e^({a_exp}x)")
print()

# 1.4 Квадратичная функция y = ax2 + bx + c
print("1.4 Квадратичная функция y = ax2 + bx + c")
print("=" * 50)

sum_x3 = np.sum(x**3)
sum_x4 = np.sum(x**4)
sum_x2y = np.sum(x**2 * y)

print(f"sum x = {sum_x}")
print(f"sum y = {sum_y}")
print(f"sum x2 = {sum_x2}")
print(f"sum x3 = {sum_x3}")
print(f"sum x4 = {sum_x4}")
print(f"sum xy = {sum_xy}")
print(f"sum x2y = {sum_x2y}")

# Система уравнений
print(f"\nСистема уравнений:")
print(f"{sum_x4}a + {sum_x3}b + {sum_x2}c = {sum_x2y}")
print(f"{sum_x3}a + {sum_x2}b + {sum_x}c = {sum_xy}")
print(f"{sum_x2}a + {sum_x}b + {n}c = {sum_y}")

# Решение системы уравнений
A = np.array([
    [sum_x4, sum_x3, sum_x2],
    [sum_x3, sum_x2, sum_x],
    [sum_x2, sum_x, n]
])
B = np.array([sum_x2y, sum_xy, sum_y])

solution = np.linalg.solve(A, B)
a_quad = round(solution[0], 2)
b_quad = round(solution[1], 2)
c_quad = round(solution[2], 2)

print(f"\nРешение системы:")
print(f"a = {a_quad}")
print(f"b = {b_quad}")
print(f"c = {c_quad}")
print(f"Уравнение: y = {a_quad}x2 + {b_quad}x + {c_quad}")
print()

# Вычисление значений функций в точках эксперимента
y_linear = a_linear * x + b_linear
y_power = beta_power * (x ** a_power)
y_exp = beta_exp * np.exp(a_exp * x)
y_quad = a_quad * x**2 + b_quad * x + c_quad

print("Сравнение значений:")
print("x     y     линейная степенная показательная квадратичная")
for i in range(len(x)):
    print(f"{x[i]}     {y[i]}     {y_linear[i]:.2f}       {y_power[i]:.2f}       {y_exp[i]:.2f}           {y_quad[i]:.2f}")

# Вычисление суммарных квадратов отклонений
L_linear = np.sum((y - y_linear)**2)
L_power = np.sum((y - y_power)**2)
L_exp = np.sum((y - y_exp)**2)
L_quad = np.sum((y - y_quad)**2)

print(f"\nСуммарные квадраты отклонений:")
print(f"Линейная функция: L = {L_linear:.4f}")
print(f"Степенная функция: L = {L_power:.4f}")
print(f"Показательная функция: L = {L_exp:.4f}")
print(f"Квадратичная функция: L = {L_quad:.4f}")

# Определение лучшей аппроксимации
errors = {
    "Линейная": L_linear,
    "Степенная": L_power,
    "Показательная": L_exp,
    "Квадратичная": L_quad
}
best_fit = min(errors, key=errors.get)

print(f"\nВывод: лучшей аппроксимирующей функцией является {best_fit.lower()} функция")

# Построение графиков
x_fit = np.linspace(1, 23, 100)
y_linear_fit = a_linear * x_fit + b_linear
y_power_fit = beta_power * (x_fit ** a_power)
y_exp_fit = beta_exp * np.exp(a_exp * x_fit)
y_quad_fit = a_quad * x_fit**2 + b_quad * x_fit + c_quad

plt.figure(figsize=(12, 8))

# Общий график
plt.subplot(2, 1, 1)
plt.plot(x_fit, y_linear_fit, 'r-', label=f'Линейная: y = {a_linear}x + {b_linear}')
plt.plot(x_fit, y_power_fit, 'g-', label=f'Степенная: y = {beta_power} * x^{a_power}')
plt.plot(x_fit, y_exp_fit, 'b-', label=f'Показательная: y = {beta_exp} * e^({a_exp}x)')
plt.plot(x_fit, y_quad_fit, 'm-', label=f'Квадратичная: y = {a_quad}x2 + {b_quad}x + {c_quad}')
plt.plot(x, y, 'ko', markersize=6, label='Экспериментальные точки')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Аппроксимация экспериментальных данных')
plt.legend()
plt.grid(True)

# График отклонений
plt.subplot(2, 1, 2)
deviations = [L_linear, L_power, L_exp, L_quad]
functions = ['Линейная', 'Степенная', 'Показательная', 'Квадратичная']
colors = ['red', 'green', 'blue', 'magenta']
plt.bar(functions, deviations, color=colors, alpha=0.7)
plt.ylabel('Сумма квадратов отклонений')
plt.title('Сравнение качества аппроксимации')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()