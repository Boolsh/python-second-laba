import numpy as np
import math
import matplotlib.pyplot as plt

# Автор: Пекшин 9 группа

# Цвет: любой который можно задать одной буквой (но для каждого свой).
# Линия: сплошная, пунктирная, сплошная, пунктирная.
# Толщина: 2, 3, 2, 3.
# Сетка: ☒,☑,☑,☑.
# Задать пользовательские значения вдоль оси x (θ или φ)
#
# (A) Формула задана параметрически:
# 𝑥 = 2 cos 𝑡 + 4 cos2𝑡/3
# 𝑦 = 2 sin 𝑡 − 4 sin2𝑡/3
# где 𝑡 ∈ [0; 6𝜋]
# (B) Формула задана параметрически:
# 𝑥 = (𝑒^√𝑡)*cos𝑡

# 𝑦 = (𝑒^√𝑡)*sin𝑡
# (C)
# 𝑦 = ±√𝑥^3 + 𝑥^2
# (D)
# y = x^3


plt.figure("Figures", figsize=(15, 10))
t1 = np.linspace(0, 6 * np.pi, 1000)

x1 = 2*np.cos(t1) + 4*np.cos(2*t1/3)
y1 = 2*np.sin(t1) - 4*np.sin(2*t1/3)

first = plt.subplot2grid((2, 2), (0, 0))
first.plot(x1, y1, linewidth=2, linestyle='-', color='b')

custom_ticks = [-3, -2, -1, 0, 1.25, 2, 3, 4, 5,6]

first.set_xticks(custom_ticks)
first.set_yticks(custom_ticks)
####################################################################

t2 = np.linspace(0, 10 * np.pi, 1000)

x2 = (math.e**(t2**0.5)*np.cos(t2))
y2 = (math.e**(t2**0.5)*np.sin(t2))

second = plt.subplot2grid((2, 2), (0, 1))
second.plot(x2, y2, linewidth=3, linestyle='--', color='r')
second.grid(True)

####################################################################

x3 = np.linspace(0, 10000, 100)

y3plus = (x3**3 + x3**2)**0.5
y3minus = -(x3**3+ x3**2)**0.5

third = plt.subplot2grid((2, 2), (1, 0))
third.plot(y3plus, x3, linewidth=2, linestyle='--', color='g')
third.plot(y3minus, x3, linewidth=2, linestyle='--', color='g')
third.grid(True)

####################################################################

x4 = np.linspace(-100, 100, 100)

y4 = x4**3

fourth = plt.subplot2grid((2, 4), (1, 3))
fourth.plot(y4, x4, linewidth=3, linestyle='--', color='y')
fourth.grid(True)


plt.show()



