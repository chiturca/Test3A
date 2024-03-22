""" print("Merhaba Tobeto Test Üyesi") #Anasayfa
print("Merhaba Tobeto Test Üyesi") #profil
print("Merhaba Tobeto Test Üyesi") #about
print("Merhaba Tobeto Test Ekibi") #contact """

#degiskenler 
#string => metinsel ifade 
text = "Merhaba Tobeto Test Üyesi!!!"
print(text)
#print(type(text))

#int ,integer => tam sayı 
studentCount = 45
print(studentCount + 5)

#double,decimal,float => ondalıklı sayılarımız 
point = 25.5
print(25.5 + 5)

#bool , boolean 0-1 => true false 
isVerified = True 
print(isVerified)

#Matematiksel
# + - * / %

number = 20
print(number + 20)

print(number - 5)

print(number * 5)

print(number / 5)

print(number % 3) 

#Mantıksal 
print(number == 20) #True
print(number == 25) #False

print(number != 20) #False
print(number != 25) #True

print(number >20) #False
print(number >= 20) #True

print(number <20) #False
print(number <= 20) #True



#string interpolation => metin birleştirme 
hello = "Merhaba"
userName = "irem"

totalText = hello + " " + userName
print(totalText)

totalText = "{message} Sayın {name}".format(message = "Selamlar", name=userName)
print(totalText)

totalText = f"Hoşgeldiniz {userName}" 
print(totalText)