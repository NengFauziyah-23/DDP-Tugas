# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
#  buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method
#  buat minimal 2 objek untuk setiap class childnya. 

from Animal import Animal

class Ikan(Animal):

    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran, warna):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran = ukuran
        self.warna = warna

    def info_ikan(self):
        super().info_animal(),
        print("Ukuran \t\t\t : ", self.ukuran,
              "\nWarna \t\t\t : ", self.warna)
        
ikan_cupang = Ikan("Cupang", "Jentik nyamuk", "Air tawar", "Bertelur", " Kecil", "Warna-warni")  
ikan_cupang.info_ikan()
print("=================================================")
ikan_paus = Ikan("Paus putih", "Ikan", "Air laut", "Melahirkan", "Besar", "Putih")  
ikan_paus.info_ikan()