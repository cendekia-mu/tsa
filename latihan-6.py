data = []

def input_data():
    print("Masukan Informasi Anda")
    nama = input("Masukan Nama: ")
    umur = input("Masukan Umur: ")
    alamat = input("Masukan Alamat: ")
    data.append(
        {"nama": f"{nama}", "umur": f"{umur}", "alamat": f"{alamat}"})
    
def lihat_data():
    print("Tampilkan Data")
    if len(data) == 0:
        print("Data tidak ditemukan")
        input("Tekan Enter untuk kembali ke menu...")
        return
    print("Nama".ljust(10), "Usia".rjust(5), "Alamat".ljust(20))
    for entry in data:
        print(
            f"{entry['nama'].ljust(10)} {entry['umur'].rjust(5)} {entry['alamat'].ljust(20)}")
    input("Tekan Enter untuk kembali ke menu...")
    
def edit_data():
    edit_1 = input("Masukan Nama yg akan di edit: ")
    edit_nama = input("Masukan Nama: ")
    edit_umur = input("Masukan Umur: ")
    edit_alamat = input("Masukan Alamat: ")
    for i in range(len(data)):
        if data[i]["nama"] == edit_1:
            data[i]["nama"] = edit_nama if edit_nama else data[i]["nama"]
            data[i]["umur"] = edit_umur if edit_umur else data[i]["umur"]
            data[i]["alamat"] = edit_alamat if edit_alamat else data[i]["alamat"]
            print("Data berhasil diupdate")
    else:
        print("Data tidak ditemukan")
    input("Tekan Enter untuk kembali ke menu...")

def hapus_data():
    hapus = input("Masukan Nama yg akan di hapus: ")
    for i in range(len(data)):
        if data[i]["nama"] == hapus:
            del data[i]
            print("Data berhasil dihapus")
    else:
        print("Data tidak ditemukan")
    input("Tekan Enter untuk kembali ke menu...")

def main():
    menu = 0
    while menu != 5:
        print("=== Program Input Data Diri ===")
        print("1. Input Data")
        print("2. Lihat Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Selesai")

        menu = input("Pilih Menu (1-5): ")
        try:
            menu = int(menu)
        except:
            menu = 0
            print("Pilihan tidak valid, 1-5 silakan coba lagi.")
            continue

        if menu < 1 or menu > 5:
            print("Pilihan tidak valid, 1-5 silakan coba lagi.")
            continue

        if menu == 1: # input
            input_data()
        elif menu == 2: # lihat
            lihat_data()
        elif menu == 3: # edit
            edit_data()
        elif menu == 4: # hapus
            hapus_data()
        elif menu == 5:
            print("Selesai")

main()