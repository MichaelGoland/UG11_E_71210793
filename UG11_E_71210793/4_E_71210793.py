import random
def generate(Operasi_pertama):
    alatoperator = ['+','-','/','*']
    implementasi = random.choice(alatoperator)
    if Operasi_pertama == '1':
        pertama = random.randint(20,50)
        kedua = random.randint(20,50)
        implementasi = random.choice(alatoperator)
        Keluaran = eval(str(pertama) + implementasi + str(kedua))
        Keluaran = round(Keluaran,3)
        print("Berapakah hasil dari ", pertama, implementasi, kedua,)
        hasil = float(input("Masukkan jawaban anda :")) 
        if hasil == Keluaran:
            return print("Jawaban anda benar!")
        else:
            print("jawaban anda salah!")
            print("Hasil dari", pertama, implementasi, kedua, "=", Keluaran)

    elif Operasi_pertama == '2':
        implementasi_pertama = random.choice(alatoperator)
        implementasi_kedua = random.choice(alatoperator)
        pertama = random.randint(20,70)
        kedua = random.randint(20,70)
        ketiga = random.randint(20,70)
        Keluaran = eval(str(pertama) + implementasi_pertama + str(kedua) + implementasi_kedua + str(ketiga))
        Keluaran = round(Keluaran,3)
        print("Berapakah hasil dari", pertama, implementasi_pertama, kedua, implementasi_kedua, ketiga)
       
        hasil = float(input("Masukkan jawaban anda :")) 
        if hasil == Keluaran:
            return print("Jawaban anda benar!")
        else:
            print("jawaban anda salah!")
            print("Hasil dari", pertama, implementasi, kedua, "=", Keluaran)


    elif Operasi_pertama == '3':
        implementasi_pertama = random.choice(alatoperator)
        implementasi_kedua = random.choice(alatoperator)
        implementasi_ketiga  = random.choice(alatoperator)
        pertama = random.randint(20,100)
        kedua = random.randint(20,100)
        ketiga = random.randint(20,100)
        keempat = random.randint(20,100)
        Keluaran = eval(str(pertama) + implementasi_pertama + str(kedua) + implementasi_kedua + str(ketiga) + implementasi_ketiga + str(keempat))
        Keluaran = round(Keluaran,3)
        print("Berapakah hasil dari", pertama, implementasi_pertama, kedua, implementasi_kedua, ketiga, implementasi_ketiga, keempat)
       
        hasil = int(input("Masukkan jawaban anda :")) 
        if hasil == Keluaran:
            return print("Jawaban anda benar!")
        else:
            print("jawaban anda salah!")
            print("Hasil dari", pertama, implementasi, kedua, "=", Keluaran)




print("=====Program Aritmatika Dasar=====")
print("pilihan level yang tersedia :")
print("1. Easy")
print("2. Medium")
print("3. Hard")
Operasi_pertama = input("Masukkan tingkatan yang ingin anda pilih :")
generate(Operasi_pertama)
