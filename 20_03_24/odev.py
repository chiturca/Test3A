# 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy = float(input("Lutfen boyunuzu giriniz : "))
kilo = int(input ("Lutfen kilonuzu giriniz :"))
vki=kilo/(boy*boy)
print("vücut kitle indeksiniz:",vki)

# 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
Maas = 50000
Zam = 10

Zamlimaas = Maas + (Maas * Zam / 100)

print("Zamlı maaşınız:", Zamlimaas)

# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
sayi1 = float(input("1. Sayıyı giriniz: "))
sayi2 = float(input("2. Sayıyı giriniz: "))
sayi3 = float(input("3. Sayıyı giriniz: "))

if(sayi1>sayi2 and sayi1>sayi3):
    print("En buyuk sayi:",sayi1)
elif(sayi2>sayi1 and sayi2>sayi3):
    print("En buyuk sayi:",sayi2)
elif(sayi3>sayi1 and sayi3>sayi2):
    print("En buyuk sayi:",sayi3)

# 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
import math

yaricap = int(input("Dairenin yarıçapını girin: "))

alan = math.pi * yaricap ** 2
cevre = 2 * 3.14 * yaricap

print("Dairenin alanı:", alan)
print("Dairenin çevresi:", cevre)

# 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = int(input ("Lutfen bir sayi giriniz :"))
def is_palindrome(number):
    reverse_number = int(str(number)[::-1])
    return number == reverse_number

if is_palindrome(sayi):
    print("Girdiginiz sayi palindromdur.")
else:
    print("Girdiginiz sayi palindrom degildir.")
