from Tools.Connection import *
import Tools.CRUD as CRUD
class DevPengepul:
    harga = set()
    def show():
        print("Selamat Datang di Aplikasi Pengepul")
        print("Silahkan Pilih Menu")
        print("1. Lihat Harga")
        print("2. Update Harga")
        print("3. Lihat Request")
        print("4. Insert")
        print("5.  Atur Penjemputan")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1:
            print(f"Harga Kopi Saat Ini {DevPengepul.harga[0]}")
        elif pilih == 2:
            DevUpdatePengepul.update_harga()
        elif pilih == 3:
            print("Request Pilihan")
        elif pilih == 4:
            display.menu_crud()
        elif pilih == 5:
            DevJadwalpenjemputan.atur_penjemputan()
        else:
            print("Pilihan Tidak Tersedia")

class DevUpdatePengepul ():
    def update_harga():
        print("Anda Memilih Menu Update Harga")
        print("1. Update Harga")
        print("2. Kembali")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1:
            price = int(input("masukkan harga : "))
            # tambahkan ke harga diatas
            DevPengepul.harga.add(price)
            print(f"Harga Kopi Saat Ini {DevPengepul.harga[0]}")
            DevUpdatePengepul.update_harga()
        elif pilih == 2:
            DevPengepul.show()
        else:
            print("Pilihan Tidak Tersedia")

class display:
    def menu_crud():
        print("Tampilan")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Keluar")
        data = int(input("Pilih Menu : "))
        if data == 1:
            display.menu_tambah_kualitas()
        elif data == 2:
            display.menu_read_kualitas()
        elif data == 5:
            DevPengepul.show()
            print("Pilihan Tidak Tersedia")
    def menu_tambah_kualitas():
        print("Tambah Data")
        print("1. Tambah Data Kualitas")
        print("2. Kembali")
        chociate = int(input("masukkan Data :"))
        if chociate == 1:
            CRUD.tambah_kualitas()
        elif chociate == 2:
            display.menu_crud()

    def menu_read_kualitas():
        print("Tampilkan Data")
        print("1. Tampilkan Data Kualitas")
        print("2. Kembali")
        chociate = int(input("masukkan Data :"))
        if chociate == 1:
            CRUD.read_kualitas_kopi()
        elif chociate == 2:
            display.menu_crud()
            
class DevJadwalpenjemputan:
    schedules = []

    @staticmethod
    def atur_penjemputan():
        print("Menu Atur Penjemputan")
        print("1. Tambah Penjemputan")
        print("2. Lihat Penjemputan")
        print("3. Kembali")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1:
            DevJadwalpenjemputan.tambah_penjemputan()
        elif pilih == 2:
            DevJadwalpenjemputan.lihat_penjemputan()
        elif pilih == 3:
            DevPengepul.show()
        else:
            print("Pilihan Tidak Tersedia")

    @staticmethod
    def tambah_penjemputan():
        petani = input("Masukkan nama petani: ")
        tanggal = input("Masukkan tanggal penjemputan (YYYY-MM-DD): ")
        waktu = input("Masukkan waktu penjemputan (HH:MM): ")
        lokasi = input("Masukkan lokasi penjemputan: ")
        catatan = input("Masukkan catatan tambahan: ")

        schedule = {
            "petani": petani,
            "tanggal": tanggal,
            "waktu": waktu,
            "lokasi": lokasi,
            "catatan": catatan
        }

        DevJadwalpenjemputan.jadwal.append(jadwal)
        print("Penjemputan berhasil ditambahkan.")
        DevJadwalpenjemputan.atur_penjemputan()

    @staticmethod
    def lihat_penjemputan():
        if DevJadwalpenjemputan.jadwal:
            for idx, schedule in enumerate(DevJadwalpenjemputan.jadwal):
                print(f"{idx+1}. Petani: {jadwal['petani']}, Tanggal: {jadwal['tanggal']}, Waktu: {jadwal['waktu']}, Lokasi: {jadwal['lokasi']}, Catatan: {jadwal['catatan']}")
        else:
            print("Belum ada jadwal penjemputan.")
        DevJadwalpenjemputan.atur_penjemputan()