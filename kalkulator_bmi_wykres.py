import matplotlib.pyplot as plt

# Funkcja do obliczania BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Wczytywanie danych z pliku
def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        try:
            height, weight = map(float, line.strip().split())
            data.append((height, weight))
        except ValueError:
            print(f"Pominięto nieprawidłowy wiersz: {line.strip()}")
    return data

# Generowanie wykresu
def plot_bmi(bmi_values):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(bmi_values) + 1), bmi_values, marker='o', linestyle='-', color='b')
    plt.title('BMI dla poszczególnych osób')
    plt.xlabel('Numer osoby')
    plt.ylabel('BMI')
    plt.grid(True)
    plt.show()

# Główna funkcja programu
def main():
    filename = input("Podaj nazwę pliku (np. dane.txt): ")
    data = read_file(filename)

    if not data:
        print("Brak poprawnych danych w pliku.")
        return

    bmi_values = [calculate_bmi(weight, height) for height, weight in data]

    for idx, bmi in enumerate(bmi_values, start=1):
        print(f"Osoba {idx}: BMI = {bmi:.2f}")

    plot_bmi(bmi_values)

if __name__ == "__main__":
    main()
