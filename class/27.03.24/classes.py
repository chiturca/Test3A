# class Student:
#     name="irem"
#     age= 25
    
#     def study(self):
#         print(f"{self.name} is studiying...")

# student1 = Student()
# student1.name = "Osman"

class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print("Yapıcı blok çalıştı")
    
    def study(self):
        print(f"{self.name} is studying...")

student2 = Student("murat", 25)