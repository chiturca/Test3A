ortalamaNot = int(input("Lütfen ortalamanızı giriniz: "))

if ortalamaNot > 80:
    print("Bravo")
    if ortalamaNot < 40:
        print("Kötü")
    elif ortalamaNot > 40:
        print("İyi")
elif ortalamaNot > 50:
    print("Harika")
else:
    print("Dersten Kaldınız!!")