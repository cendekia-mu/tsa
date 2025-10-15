# def contoh_argumen(*args):
#     print("Argumen posisi (args):", args)


# contoh_argumen(1, 2, 3, 'a', 'b')



# def contoh_argumen_kata_kunci(**kwargs):
#     print("Argumen kata kunci (kwargs):", kwargs)

# contoh_argumen_kata_kunci(nama="Andi", umur=20, alamat="Jakarta")


# def contoh_argumen2(*args):
#     if len(args) >= 1:
#         print("Argumen posisi (args 1):", args[0])

#     if len(args) >= 2:
#         print("Argumen posisi (args 2):", args[1])

#     for arg in args:
#         print("Argumen posisi (args loop):", arg)

# contoh_argumen2(1, 2, 3, 'a', 'b')

# def hitung_panjang_luas(*args):
#     if len(args) < 2:
#         print("Minimal dua argumen diperlukan: panjang dan lebar")
#         return
    
#     panjang = args[0]
#     lebar = args[1]
    
#     print("Panjang:", panjang, "Lebar:", lebar, "Luas:", panjang * lebar)
#     if len(args) >= 3:
#         tinggi = args[2]
#         print("Panjang:", panjang, "Lebar:", lebar, "Tinggi:", tinggi,
#                "Volume:", panjang * lebar * tinggi)
#     print("-----------------------------------------")


# hitung_panjang_luas()
# hitung_panjang_luas(10)
# hitung_panjang_luas(10, 5)
# hitung_panjang_luas(7, 7, 2)


# def hitung_panjang_luas(**kwargs):
#     if 'panjang' not in kwargs or 'lebar' not in kwargs:
#         print("Minimal dua argumen diperlukan: panjang dan lebar")
#         print("-------------------------------------------------")
#         return

#     panjang = kwargs['panjang']
#     lebar = kwargs['lebar']

#     print("Panjang:", panjang, "Lebar:", lebar, "Luas:", panjang * lebar)
#     if 'tinggi' in kwargs:
#         tinggi = kwargs['tinggi']
#         print("Panjang:", panjang, "Lebar:", lebar, "Tinggi:", tinggi,
#               "Volume:", panjang * lebar * tinggi)
#     print("-----------------------------------------")


# hitung_panjang_luas()
# hitung_panjang_luas(panjang=10)
# hitung_panjang_luas(panjang=10, lebar=5)
# hitung_panjang_luas(panjang=7, lebar=7, tinggi=2)
# hitung_panjang_luas(panjang=10, tinggi=5)

# def hitung_panjang_luas(panjang=5, lebar=5, tinggi=2):
#     print("Panjang:", panjang, "Lebar:", lebar, "Luas:", panjang * lebar)
#     print("Panjang:", panjang, "Lebar:", lebar, "Tinggi:", tinggi,
#           "Volume:", panjang * lebar * tinggi)
#     print("---------------------------------------------")


# hitung_panjang_luas()
# hitung_panjang_luas(10)
# hitung_panjang_luas(10, 7)
# hitung_panjang_luas(10, 7, 5)
# hitung_panjang_luas(tinggi=10, lebar=6)

x = lambda a : a + 10
print(x(5))

def x(a):
    return a + 10