p = input("Masukan Panjang: ")
l = input("Masukan Lebar: ")
t = input("Masukan Tinggi: ")
print("Luas Permukaan Balok: ", 2 * (int(p) * int(l) + int(p) * int(t) + int(l) * int(t)))
print("Luas Persegi Panjang: ", int(p) * int(l))
print("Volume Balok: ", int(p) * int(l) * int(t))

# input - proses - output

i =1
if i==1:
   print("Senin")
elif i==2:
   print("Selasa")
elif i==3:
   print("Rabu")
elif i==4:
   print("Kamis")
elif i==5:
    print("Jumat")
elif i==6:
    print("Sabtu")
elif i==7:
    print("Minggu")
else:
    print("Tidak ada hari ke-", i)\

match i:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case 4:
        print("Kamis")
    case 5:
        print("Jumat")
    case 6:
        print("Sabtu")
    case 7:
        print("Minggu")
    case _:
        print("Tidak ada hari ke-", i)