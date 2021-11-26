def pangkatAngka():
     nilai_pangkat = int(input("Masukkan angka yang ingin dipangkatkan angka : "))
     modifikasi_pangkat_angka = input("ingin memodifikasi pangkat ? (yes/no):")
     if modifikasi_pangkat_angka == "yes":
        masukkan_pangkat = int(input("Masukkan nilai pangkat : " ))
        rumus = nilai_pangkat ** masukkan_pangkat
        print("Hasil dari", nilai_pangkat, "^", masukkan_pangkat, "=", rumus)
     elif modifikasi_pangkat_angka == "no":
         rumus_2 = nilai_pangkat ** 2
         print("Hasil dari", nilai_pangkat, "^", "2", "=", rumus_2)
         
def akarBilangan():
      nilai_akar = int(input("Masukkan angka yang ingin di akar Angka :"))
      modifikasi_pangkat_akar = input("ingin memodifikasi pangkat ? (yes/no):")
      if modifikasi_pangkat_akar == "yes":
          masukkan_akarpangkat = int(input("Masukkan nilai akar : " ))
          rumus_akar=nilai_akar**(1/masukkan_akarpangkat)
          print("Hasil akar pangkat", masukkan_akarpangkat, "dari", nilai_akar, "=", rumus_akar)
      elif modifikasi_pangkat_akar == "no":   
          rumus_akar_2 = nilai_akar**(1/2)
          print("Hasil akar pangkat 2 dari", nilai_akar, "=", rumus_akar_2)
def Pilih(options):
    if options == 1:
        pangkatAngka()
    elif options == 2:   
        akarBilangan()

print("Menu Program Yang Tersedia")
print("1. pangkatkan angka")
print("2. akarkan bilangan")

pilihan_angka = int(input("Masukkan pilihan yang diinginkan :"))
Pilih(pilihan_angka)
#nilai_pangkat = int(input("Masukkan angka yang ingin dipangkatkan angka : "))
#nilai_akar = int(input("Masukkan angka yang ingin di akar Angka :"))

#pangkatAngka()
#akarBilangan()








