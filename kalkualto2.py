import pandas as pd

plik = input("Podaj ścieżkę do pliku:")

if plik.endswith('.xlsx'):
    dane = pd.read_excel(plik, engine='openpyxl')
elif plik.endswith('.txt'):
    dane = pd.read_csv(plik, delimiter="\t")
else:
    print("ścieżka, bądź format pliku jest niepoprawny")
    quit()
if 'wzrost w metrach' not in dane.columns or 'masa w kilogramach' not in dane.columns:
    print("nieprawidłowy sposób zapisu danych; wzrost w metrach, masa w kilogramach")
    quit()

wynik = dane['masa w kilogramach'] / (dane['wzrost w metrach'] ** 2)
print(wynik)
wynik.to_excel('BMIWYNIK.xlsx', index=False, engine='openpyxl')