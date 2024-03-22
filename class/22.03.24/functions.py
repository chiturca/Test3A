# DEFINITION: TANIMLAMA
def ortalamaHesaplama():
    vize=67
    final=86
    ortalama=(vize*0.4)+(final*0.6)
    print(ortalama)
def ortalamaHesaplama2():
    vize=67
    final=86
    ortalama=(vize*0.4)+(final*0.6)
    return ortalama #hesap yapıyor;ancak print içinde gösterilsin ki consoleda görünsün

# ortalamaHesaplama()
# print(ortalamaHesaplama2())

def ortalamaHesaplama3(vize:float, final:float)-> float:
    return (vize*0.4)+(final*0.6)

vize= int(input("Vize notunu giriniz: "))
final= int(input("Final notunu giriniz: "))

print(ortalamaHesaplama3(vize, final))