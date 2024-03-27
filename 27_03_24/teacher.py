class Teacher:
    def __init__(self, isim, yas, bolumu):
        self.isim = isim
        self.yas = yas
        self.bolumu = bolumu

    def display_info(self):
        print(f"isim: {self.isim}, yas: {self.yas}, bolumu: {self.bolumu}")

    def teach(self, subject):
        print(f"{self.isim} is teaching {subject}")