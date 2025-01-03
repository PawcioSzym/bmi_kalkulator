def main():
    print("Kalkulator BMI")
    print("Wybierz system jednostek:")
    print("1. Metryczny (kg i metry)")
    print("2. Imperialny (funty, stopy i cale)")

    system = input("Wybierz (1 lub 2): ")
    if system == "1":
        bmi_calculator(metryczny=True)
    elif system == "2":
        bmi_calculator(metryczny=False)
    else:
        print("Nieprawidłowy wybór. Uruchom program ponownie.")

def bmi_calculator(metryczny):
    if metryczny:
        waga = float(input("Podaj wagę [kg]: "))
        wzrost = float(input("Podaj wzrost [m] (np 1.80): "))
    else:
        waga_lbs = float(input("Podaj wagę [lbs]: "))
        stopy = int(input("Podaj wzrost cz.1 [ft]: "))
        cale = int(input("Podaj wzrost cz.2 [in]: "))

        if waga_lbs <= 0 or stopy < 0 or cale < 0 or cale >= 12:
            print("Wprowadź poprawne wartości (Waga > 0, Cale w zakresie 0-11).")
            return

        waga = waga_lbs * 0.453592
        wzrost = (stopy * 0.3048) + (cale * 0.0254)

    if waga <= 0 or wzrost <= 0:
        print("Wartości wagi i wzrostu muszą być dodatnie.")
        return

    bmi = waga / wzrost**2
    print(f"Twoje BMI wynosi: {bmi:.2f}")
    kategoria_bmi(bmi)

def kategoria_bmi(bmi):
    if bmi <= 16:
        print("Jesteś wygłodzony; proszę poszukaj pomocy.")
    elif bmi <= 17:
        print("Jesteś wychudzony, na pewno wszystko dobrze?")
    elif bmi < 18.5:
        print("Masz niedowagę.")
    elif bmi < 25:
        print("Jesteś w prawidłowej kategorii wagowej; oby tak dalej!")
    elif bmi < 30:
        print("Masz nadwagę.")
    elif bmi < 35:
        print("Masz otyłość pierwszego stopnia.")
    elif bmi < 40:
        print("Masz otyłość drugiego stopnia.")
    else:
        print("Masz otyłość trzeciego stopnia.")

if __name__ == "__main__":
    main()
