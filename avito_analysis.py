import pandas as pd
import matplotlib.pyplot as plt

#Загружаем собранные данные
df = pd.read_csv("avito_data.csv")

#Анализ распределения цен
plt.figure(figsize=(10, 5))
df["Цена"].hist(bins=30, color="green", edgecolor="black")
plt.title("Распределение цен")
plt.xlabel("Цена (₽)")
plt.ylabel("Количество")
plt.grid(True)
plt.show()

#Анализ распределения валют (если есть разные валюты)
currency_counts = df["Валюта"].value_counts()

plt.figure(figsize=(8, 5))
currency_counts.plot(kind="pie", autopct="%.1f%%", colors=["skyblue", "orange"], startangle=140)
plt.title("Распределение валют")
plt.ylabel("")
plt.show()

print("Анализ завершён!")