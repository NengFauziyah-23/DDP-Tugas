# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
#  buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method
#  buat minimal 2 objek untuk setiap class childnya. 

from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, ukuran, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ukuran = ukuran                    
        self.warna = warna                

    def info_ular(self):
        super().info_animal()
        print("Ukuran \t\t\t : ", self.ukuran)
        print("Warna \t\t\t : ", self.warna)

ular_kobra = Ular("Kobra", "Mamalia kecil", "Daratan", "Telur", "Besar", "Hitam dengan kerah kuning")
ular_kobra.info_ular()
print("=================================================")
ular_python = Ular("Python", "Mamalia kecil", "Hutan tropis", "Telur", "Besar", "Coklat dengan pola hitam")
ular_python.info_ular()