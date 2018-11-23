import random
liczby = ["2", "345","677890", "22", "435", "466", "888", "21","564", "787"]
operacja = random. randrange(len(liczby))
print(operacja)



if operacja%2 == 0:
    print("Ta liczba jest parzysta")

else:
    print("Liczba jest nieparzysta")
