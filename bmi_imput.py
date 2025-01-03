def main():
    print("Kalkulator BMI")
    print("Wybierz system jednostek:")
    print("1. Metryczny (kg i metry)")
    print("2. Imperialny (funty, stopy i cale)")

    system = input("Wybierz (1 lub 2): ")
    if system == "1":
        bmi_metryczne()
    elif system == "2":
        bmi_imperialne()
    else:
        print("Nieprawidłowy wybór. Uruchom program ponownie.")

def bmi_metryczne():  
    waga_kg=float(input("Podaj wage [kg]: "))
    wzrost_m=float(input("Podaj wzrost [m] (np 1.80): "))
    bmi = waga_kg/wzrost_m**2
    print("Twoje BMI wynosi:", bmi)
    if bmi<=16:
        print("jesteś wygłodzony; proszę poszukaj pomocy")
    elif bmi>16 and bmi<17:
        print("jestes wychudzony, na pewno wszystko dobrze?")
    elif bmi>=17 and bmi<18.5:
        print("masz niedowagę")
    elif bmi>=18.5 and bmi<25:
        print("jesteś w prawidłowej kategorii wagowej; oby tak dalej")
    elif bmi>=25 and bmi<30:
        print("masz nadwagę")
    elif bmi>=30 and bmi <35:
        print("masz otyłość pierwszego stopnia")
    elif bmi>=35 and bmi<40:
        print("masz otyłość drugiego stopnia")
    elif bmi>=40:
        print("masz otyłośc trzeciego stopnia")
        
def bmi_imperialne():
        waga_lbs = float(input("Podaj wagę [lbs]: "))
        stopy = int(input("Podaj wzrost cz.1 [ft]: "))
        cale = int(input("Podaj wzrost cz.2 [in]: "))

        if waga_lbs <= 0 or stopy < 0 or cale < 0 or cale >= 12:
            print("Wprowadź poprawne wartości (Waga > 0, Cale w zakresie 0-11).")
            return

        waga_kg = waga_lbs * 0.453592  
        wzrost_m = (stopy * 0.3048) + (cale * 0.0254)
        bmi = waga_kg/wzrost_m**2
        print("Twoje BMI wynosi:", bmi)
        if bmi<=16:
            print("jesteś wygłodzony; proszę poszukaj pomocy")
        elif bmi>16 and bmi<17:
            print("jestes wychudzony, na pewno wszystko dobrze?")
        elif bmi>=17 and bmi<18.5:
            print("masz niedowagę")
        elif bmi>=18.5 and bmi<25:
            print("jesteś w prawidłowej kategorii wagowej; oby tak dalej")
        elif bmi>=25 and bmi<30:
            print("masz nadwagę")
        elif bmi>=30 and bmi <35:
            print("masz otyłość pierwszego stopnia")
        elif bmi>=35 and bmi<40:
            print("masz otyłość drugiego stopnia")
        elif bmi>=40:
            print("masz otyłośc trzeciego stopnia")

main()
