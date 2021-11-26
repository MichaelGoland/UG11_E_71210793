def string_parser():
    Kata_katanya = input("Masukkan kata:")
    jumlah_kata = len(Kata_katanya)

    if jumlah_kata%2==0:
        half_length = int((jumlah_kata/2)/2)
        tengah_kiri = int(len(Kata_katanya)/2)-1
        tengah_kanan = tengah_kiri+1

        index_start = tengah_kiri-(half_length-1)
        index_end = tengah_kanan+(half_length-1)

        print(Kata_katanya[index_start:len(Kata_katanya[:index_end+1])])

    else:
        jumlah_genap = jumlah_kata+1
        half_length = int((jumlah_genap/2)/2)

        mid_index = int(len(Kata_katanya)/2)

        index_start = mid_index-(half_length-1)
        index_end = mid_index+(half_length-1)

        print(Kata_katanya[index_start:len(Kata_katanya[:index_end+1])])

string_parser()