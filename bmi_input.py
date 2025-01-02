waga=float(input("podaj wage w kg; "))
wzrost=float(input("podaj wzrost w metrach (np 1.52); "))
bmi=waga/(wzrost)**2
print(f"twoje bmi; {bmi}")
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
