from Tools.Connection import *
import Tools.CRUD as CRUD

class DevPetani:
    def show():
        print("Selamat Datang di Aplikasi Petani")
        print("Silahkan Pilih Menu")
        print("1. Lihat Harga")
        print("2. Request Penjemputan")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1:
            DevPetani.lihat_harga()
        elif pilih == 2:
            DevRequestPenjemputan.request_penjemputan()
        else:
            print("Pilihan Tidak Tersedia")

    def view_price():
        # Misal harga diambil dari API atau database
        harga_kopi = CRUD.get_harga_kopi()
        print(f"Harga Kopi Saat Ini: {harga_kopi}")
        DevPetani.show()

class DevPickupRequest:
    requests = []

    @staticmethod
    def request_penjemputan():
        print("Request Penjemputan")
        petani = input("Masukkan nama Anda: ")
        tanggal = input("Masukkan tanggal penjemputan yang diinginkan (YYYY-MM-DD): ")
        waktu = input("Masukkan waktu penjemputan yang diinginkan (HH:MM): ")
        lokasi = input("Masukkan lokasi penjemputan: ")
        catatan = input("Masukkan catatan tambahan: ")

        request = {
            "petani": petani,
            "tanggal": tanggal,
            "waktu": waktu,
            "lokasi": lokasi,
            "catatan": catatan
        }

        DevRequestPenjemputan.requests.append(request)
        print("Request penjemputan berhasil dikirim.")
        DevPetani.show()