import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np

# Функция для аппроксимации
def approx_func(x, C1, t1, C2, t2):
    return C1 * np.exp(-x / t1) + C2 * np.exp(-x / t2)

# Задаем имена столбцов для считывания данных
column_names = ['Time', 'PPF']

# Считывание данных
data_24 = pd.read_csv('24.csv', header=None, names=column_names, decimal=',', sep=';').sort_values(by='Time')
data_100 = pd.read_csv('100.csv', header=None, names=column_names, decimal=',', sep=';').sort_values(by='Time')
data_200 = pd.read_csv('200.csv', header=None, names=column_names, decimal=',', sep=';').sort_values(by='Time')

# Подготовка графика
plt.figure(figsize=(10, 6))

# Данные для построения графика и аппроксимации
datasets = [(data_24, 'blue', '24°C'), (data_100, 'purple', '100°C'), (data_200, 'red', '200°C')]

initial_guess_1 = [150, 20, 50, 5] 
initial_guess_2 = [1, 1, 1, 1]

for data, color, label in datasets:

    if label == '200°C':
        initial_guess = initial_guess_1
    else:
        initial_guess = initial_guess_2

    # Аппроксимация данных
    params, _ = curve_fit(approx_func, data['Time'], data['PPF'], p0 = initial_guess)
    C1, t1, C2, t2 = params
    # Построение точек данных
    plt.scatter(data['Time'], data['PPF'], color=color, label=f'{label}: C1={C1:.2f}, t1={t1:.2f}, C2={C2:.2f}, t2={t2:.2f}')
    # Построение линии аппроксимации
    x_line = np.linspace(data['Time'].min(), data['Time'].max(), 500)
    y_line = approx_func(x_line, *params)
    plt.plot(x_line, y_line, color=color)

# Настройка графика
plt.xlabel('Δt (s)')
plt.ylabel('PPF index (%)')
plt.legend()
plt.savefig('ppf_index_plot.png', dpi=3000, bbox_inches='tight')
plt.show()


