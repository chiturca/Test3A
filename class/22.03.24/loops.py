# SOLİD PRENSİPLERİ

# FOR
# start: i'nin başlangıç değeri (default:0)
# stop: döngünün hangi noktada duracağı
# step: artış sayısı (default:1)

for i in range(10):
    print(i)

# kullanıcıının girdiği sayılar arasında en büyüğü bulan kod

biggestValue = 0
for i in range(3):
    number = int(input(f"{i + 1}. sayıyı giriniz: "))
    if number > biggestValue:
        biggestValue = number
print(f"Sayılar arasında en büyüğü: {biggestValue}")

numbers = []
for i in range(3):
    numbers.append(int(input(f"{i + 1}. sayıyı giriniz: ")))
print(numbers)
numbers.sort(reverse = True)
print(numbers)
print(min(numbers))
index = int(input("Sayılar arasında en büyük kaçıncı elemanı istiyorsun?: "))
print(numbers[index-1])

students = ["Ahmet", "Hakan", "Kabe", "Ercan", "Tuba"]
for i in range(len(students)):
    if i>2:
        break #ilgili döngünün verilen index noktasında kırılması
    print(f"{i + 1}. öğrenci: {students[i]}")
for student in students:
    if student == "Ercan":
        continue #bir sonraki değer ile devam et
    print(f"{student}")

# WHILE
i=0
while i<10:
    print(i)
    i=i+1