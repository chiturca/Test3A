### 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
fibonacci = [1, 1]  # İlk iki elemanı 1'e eşit olan Fibonacci serisi

while len(fibonacci) < 20:  # En az 20 elemanlı bir Fibonacci serisi oluşturmak için döngü
    next_fib = fibonacci[-1] + fibonacci[-2]  # Fibonacci serisindeki son iki elemanın toplamı
    fibonacci.append(next_fib)  # Yeni Fibonacci sayısını listeye ekle

print("20 elemanlı Fibonacci serisi:", fibonacci)

# ---------------- ya da ----------------
def soru1():
    fibonacci_serisi = [1, 1]  # İlk iki elemanı 1'e eşit olan Fibonacci serisi

    while len(fibonacci_serisi) < 20:
        yeni_eleman = fibonacci_serisi[-1] + fibonacci_serisi[-2]  # Son iki elemanın toplamı
        fibonacci_serisi.append(yeni_eleman)  # Yeni elemanı serinin sonuna ekle

    print("20 elemanlı Fibonacci serisi:", fibonacci_serisi)

soru1()


### 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
def mukemmel_mi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    if toplam == sayi:
        return True
    else:
        return False

sayi = int(input("Mükemmel olup olmadığını bulmak için bir sayı girin: "))

if mukemmel_mi(sayi):
    print(sayi, "mükemmel bir sayıdır.")
else:
    print(sayi, "mükemmel bir sayı değildir.")

# ---------------- ya da ----------------
def odev2():
    sayi = int(input("Mükemmel olup olmadığını bulmak için bir sayı girin: "))
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    if toplam == sayi:
        print(sayi, "mükemmel sayıdır.")
    else:
        print(sayi, "mükemmel sayı değildir.")
odev2()


### 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
def odev3():
    sayi1 = int(input("EBOB-EKOK bulmak için lütfen birinci sayıyı giriniz: "))
    sayi2 = int(input("EBOB-EKOK bulmak için lütfen ikinci sayıyı giriniz: "))
    ebob = 1
    ekok = 1
    for i in range(1, min(sayi1, sayi2) + 1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ebob = i  # EBOB değeri güncellenir
    ekok = (sayi1 * sayi2) //ebob
    print("Ebob:", ebob)
    print("Ekok:", ekok)
odev3()
    
### 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
def odev4():
    sayi = int(input("Asal olup olmadığını bulmak için lütfen bir sayı giriniz: "))
    asal = True
    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print(sayi, "asal sayıdır.")
    else:
        print(sayi, "asal sayı değildir.")
odev4()

### 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
def asal_carpanlari_bul(sayi):
    carpanlar = []
    k = 2
    while sayi > 1:
        if sayi % k == 0:
            carpanlar.append(k)
            sayi //= k
        else:
            k += 1
    return carpanlar

sayi = int(input("Asal çarpanlarını bulmak için bir sayı girin: "))

print(f"{sayi} sayısının tüm asal çarpanları:", asal_carpanlari_bul(sayi))

# ---------------- || ----------------
def cevap5():
    def asal_carpanlar(sayi):
        asal_carpanlar_listesi = []
        carpan = 2

        while sayi > 1:
            if sayi % carpan == 0:
                if carpan not in asal_carpanlar_listesi:
                    asal_carpanlar_listesi.append(carpan)
                sayi //= carpan
            else:
                carpan += 1
        return asal_carpanlar_listesi

    sayi = int(input("Asal çarpanlarını bulmak için bir sayı girin: "))
    asal_carpanlar_listesi = asal_carpanlar(sayi)
    print(f"{sayi} sayısının asal çarpanları:", asal_carpanlar_listesi)
cevap5()