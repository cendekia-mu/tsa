# fungsi tanpa argumen dan tanpa nilai kembalian
def nihil():
    """Fungsi tanpa argumen dan tanpa nilai kembalian"""
    print("Fungsi nihil dipanggil")

# fungsi dengan argumen dan tanpa nilai kembalian
def greet(nama):
    """Fungsi dengan argumen dan tanpa nilai kembalian

    Args:
        nama (str): Nama yang akan disapa
    """
    print("Halo", nama)

# fungsi tanpa argumen dan dengan nilai kembalian
def pi():
    """Fungsi tanpa argumen dan dengan nilai kembalian

    Returns:
        float: Nilai pi
    """
    return 3.14

# fungsi dengan argumen dan mengembalikan nilai
def kuadrat(x):
    """Menghitung kuadrat dari x

    Args:
        x (int, float): Nilai yang akan dikuadratkan

    Returns:
        int, float: Hasil kuadrat dari x
    """
    return x * x


def hitung_luas(panjang, lebar): 
    """Menghitung luas persegi panjang

    Args:
        panjang (float): Panjang persegi panjang
        lebar (float): Lebar persegi panjang

    Returns:
        float: Luas persegi panjang
    """
    # return panjang * lebar
    print("Panjang:", panjang, "Lebar:", lebar, "Luas:", panjang * lebar)

hitung_luas(10, 5)
hitung_luas(lebar=7, panjang=10)
hitung_luas(panjang=6, lebar=6)
hitung_luas(8, lebar=5)
# print(hitung_luas(panjang=10, 5))
# contoh salah memanggil fungsi karena argumen posisi setelah argumen kata kunci
