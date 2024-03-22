sayilar = [100,200,300,"Merhaba"]
#Programcılar saymaya sıfırdan başlar!!
print(sayilar)
print(sayilar[0])

sayilar.append(200)
print(sayilar)

sayilar.remove(200) #değere göre siler
print(sayilar)

sayilar.pop(2) #indexe göre siler 
print(sayilar)

sayilar.extend([100,200,300])
print(sayilar)

sayilar.clear()
print(sayilar)