import matplotlib.pyplot as plt
import pandas as pd

# Задаем имена столбцов для считывания данных
column_names = ['Time', 'PPF']

# Считывание данных из CSV файлов, предполагая, что у файлов нет заголовков,
# что десятичный разделитель — запятая, и что столбцы разделены точкой с запятой
data_24 = pd.read_csv('24.csv', header=None, names=column_names, decimal=',', sep=';').sort_values(by='Time')
data_100 = pd.read_csv('100.csv', header=None, names=column_names, decimal=',', sep=';').sort_values(by='Time')
data_200 = pd.read_csv('200.csv', header=None, names=column_names, decimal=',', sep=';').sort_values(by='Time')

min_ppf = min(data_24['PPF'].min(), data_100['PPF'].min(), data_200['PPF'].min())
# Построение графиков
plt.figure(figsize=(10, 6))  # Можно задать размер фигуры, если необходимо
plt.plot(data_24['Time'], data_24['PPF'], marker='o', color='blue', label='24°C')
plt.plot(data_100['Time'], data_100['PPF'], marker='o', color='purple', label='100°C')
plt.plot(data_200['Time'], data_200['PPF'], marker='o', color='red', label='200°C')

# Установка лимитов для оси Y согласно графику
plt.ylim(min_ppf * 0.96, max(data_24['PPF'].max(), data_100['PPF'].max(), data_200['PPF'].max()) + 10)

# Добавление легенды
plt.legend()

# Добавление заголовков осей
plt.xlabel('Δt (s)')
plt.ylabel('PPF index (%)')
#plt.subplots_adjust(bottom=0)
# Добавление сетки
#plt.grid(True)
plt.savefig('ppf_index_plot.png', dpi=3000, bbox_inches='tight')
# Сохранение графика перед показом в высоком качеств

# Отображение графика
plt.show()




