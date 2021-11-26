def Hitung_kata():
        kalimat = input("Masukkan sebuah kalimat/kata :")
        kata_dihitung = input("Masukkan kata yang ingin dihitung :")
        print("Terdapat sebanyak", (kalimat.lower().count(kata_dihitung.lower())), "kata", kata_dihitung, "di dalam string")
def Cek_kata():  
        kalimat = input("Masukkan sebuah kalimat/kata :")
        kata_dicek = input("Masukkan kata yang ingin dicek :")
        if(kata_dicek in kalimat):
            KALIMAT_BARU=kalimat.replace(kata_dicek,kata_dicek.upper())
            print("Kata diam terdapat di dalam string")
            print("String diubah menjadi:")
            print(KALIMAT_BARU)
        else:
            print(kalimat, kata_dicek)

def Ubah_kata():
        kalimat = input("Masukkan sebuah kalimat/kata :")
        kata_dicek = input("Masukkan kata yang ingin diubah :")
        kata_pengganti = input("Masukkan kata pengganti :")
        
        if(kata_dicek in kalimat):
            Kata_BARU=kalimat.replace(kata_dicek,kata_pengganti,1)
            modifikasi_ubah_kata = input("ingin memodifikasi pangkat ? (yes/no):")
            if modifikasi_ubah_kata == "yes":
                jumlah_penggantian = int(input("Masukkan jumlah total penggantian :"))
                Kata_BARU=kalimat.replace(kata_dicek,kata_pengganti,jumlah_penggantian)
                print("String berhasil diubah menjadi:")
                print(Kata_BARU)
            else:
                print(kalimat)   
        else:
            print(kalimat, kata_dicek)
        
def Pilih(options):
    if options == 1:
        Hitung_kata()
    elif options == 2:   
        Cek_kata()
    elif options == 3:
        Ubah_kata()

print("======Program Manipulasi String======")
print("Pilihan Menu :")
print("1. Hitung kata")
print("2. Cek kata")
print("3. Ubah kata")

pilihan = int(input("Pilihan anda :"))

Pilih(pilihan)

