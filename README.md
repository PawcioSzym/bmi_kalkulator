# bmi_kalkulator
 kalkulator bmi
Kategoria	| Zakres BMI (kg/m²)
Niedowaga 	< 18,5
Prawidłowa masa ciała	 18,5 – 24,9
Nadwaga 	25,0 – 29,9
Otyłość I stopnia	 30,0 – 34,9
Otyłość II stopnia	 35,0 – 39,9
Otyłość III stopnia	 ≥ 40,0



import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generowanie przykładowych danych
data = np.random.normal(size=1000)

# Tworzenie wykresu dystrybucji za pomocą histplot
sns.histplot(data, kde=True, color="blue", bins=30)

# Dostosowanie wykresu
plt.title("Distributional Representation")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Wyświetlenie wykresu
plt.show()
