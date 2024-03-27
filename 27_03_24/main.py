# Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.

# main.py
from student import Student
from teacher import Teacher

# Öğrenci oluşturma
student1 = Student("Fatih", 19, 11)
student2 = Student("Yasemin", 15, 10)
student3 = Student("Revşen", 11, 2)

# Öğretmen oluşturma
teacher1 = Teacher("Ms. Miray", 35, "Mathematics")
teacher2 = Teacher("Mr. M.Fatih Yıldırım", 40, "Science")

ogretmenler = []
ogrenciler = []

ogretmenler.append(teacher1)
ogretmenler.append(teacher2)

ogrenciler.append(student1)
ogrenciler.append(student2)
ogrenciler.append(student3)

for ogretmen in ogretmenler:
    print("Öğretmen Adı :", ogretmen.isim, "Yaşı:", ogretmen.yas, "Bölümü :", ogretmen.bolumu)


for ogrenci in ogrenciler:
    print("Öğrenci Adı :", ogrenci.isim, "Yaşı:", ogrenci.yas, "Sınıfı :", ogrenci.sinifi)