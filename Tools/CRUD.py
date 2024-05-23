#<<<<<<< HEAD
from Tools.Connection import *

def delete_pengepul():
    read_admin(cur)
    id_pengepul = input('Masukkan id pengepul yang ingin dihapus: ') 
    delete_pengepul = f"DELETE FROM admin WHERE id_pengepul = {id_pengepul}"
    cur.execute(delete_pengepul)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")



def update_admin():
    id_pengepul =       input("Masukkan Id Pengepul       : ")
    nama =              input("Masukkan Nama Pengepul     : ") 
    password_admin =    input("Masukkan Password Pengepul : ") 
    email =             input("Masukkan Email             : ") 
    nomor_telepon =     input("Masukkan Nomor Telepon     : ") 
    deskripsi1 =        input("Masukkan Deskripsi         : ") 

    query_update_admin = f"UPDATE Admin SET nama = {nama}, password_admin = {password_admin}, email = {email}, nomor_telepon = {nomor_telepon}, deskripsi1 = {deskripsi1} WHERE Id_Pengepul = {id_pengepul}"

    cur.execute(query_update_admin)

    conn.commit()
    print("admin berhasil diupdate")

    cur.close()
    conn.close()

def update_pegawai_penjemputan ():
    id_pegawai =        input("Masukkan Id Pegawai   : ")
    nama_pegawai =      input("Masukkan Nama Pegawai : ") 
    no_telepon =        input("Masukkan No Telepon   : ") 
    admin_id_pengepul = input("Masukkan Id Pengepul  : ") 
    alamat =            input("Masukkan Alamat       : ") 

    query_update_pegawai_penjemputan = f"UPDATE pegawai_penjemputan SET nama_pegawai = {nama_pegawai}, no_telepon = {no_telepon}, admin_id_pengepul = {admin_id_pengepul}, alamat = {alamat} WHERE id_pegawai = {id_pegawai}"

    cur.execute(query_update_pegawai_penjemputan)

    conn.commit()
    print("pegawai penjemputan berhasil diupdate")

    cur.close()
    conn.close()

def update_cash ():
    id_cash =           input("Masukkan Id Cash           : ") 
    nomor_telepon =     input("Masukkan No Telepon        : ") 
    jumlah_pembayaran = input("Masukkan Jumlah Pembayaran : ")

    query_update_cash = f"UPDATE cash SET nomor_telepon = {nomor_telepon}, jumlah_pembayaran = {jumlah_pembayaran} WHERE id_cash = {id_cash}"

    cur.execute(query_update_cash)

    conn.commit()
    print("cash berhasil diupdate")

    cur.close()
    conn.close()


def update_debit ():
    id_debit =       input("Masukkan Id Debit       : ") 
    nama_pemilik =   input("Masukkan Nama           : ") 
    nama_bank =      input("Masukkan Nama Bank      : ")
    nomor_rekening = input("Masukkan Nomor Rekening : ")  

    query_update_debit = f"UPDATE debit SET nama_pemilik = {nama_pemilik}, nama_bank = {nama_bank}, nomor_rekening = {nomor_rekening} WHERE id_debit = {id_debit}"

    cur.execute(query_update_debit)

    conn.commit()
    print("debit berhasil diupdate")

    cur.close()
    conn.close()

def update_gudang ():
    kode_gudang = input("Masukkan Kode Gudang   : ")
    kapasitas =   input("Masukkan Kapasitas     : ") 
    deskripsi =   input("Masukkan Deskripsi     : ") 

    query_update_gudang = f"UPDATE gudang SET kapasitas = {kapasitas}, deskripsi = {deskripsi} WHERE kode_gudang = {kode_gudang}"

    cur.execute(query_update_gudang)

    conn.commit()
    print("gudang berhasil diupdate")

    cur.close()
    conn.close()

def update_jadwal_penjemputan ():
    id_penjemputan =                           input("Masukkan Id Penjemputan           : ")
    waktu_penjemputan =                        input("Masukkan Waktu Penjemputan        : ") 
    status_penjemputan_id_status_penjemputan = input("Masukkan Id Status Penjemputan    : ") 

    query_update_jadwal_penjemputan = f"UPDATE jadwal_penjemputan SET waktu_penjemputan = {waktu_penjemputan}, status_penjemputan_id_status_penjemputan = {status_penjemputan_id_status_penjemputan} WHERE id_penjemputan = {id_penjemputan}"

    cur.execute(query_update_jadwal_penjemputan)

    conn.commit()
    print("jadwal penjemputan berhasil diupdate")

    cur.close()
    conn.close()

def update_pembayaran ():
    id_pembayaran =     input("Masukkan Id Pembayaran       : ")
    metode_pembayaran = input("Masukkan Metode Pembayaran   : ") 
    deskripsi =         input("Masukkan Deskripsi           : ") 

    query_update_pembayaran = f"UPDATE pembayaran SET metode_pembayaran = {metode_pembayaran}, deskripsi = {deskripsi} WHERE id_pembayaran = {id_pembayaran}"

    cur.execute(query_update_pembayaran)

    conn.commit()
    print("pembayaran berhasil diupdate")

    cur.close()
    conn.close()

def update_service ():
    id_layanan =    input("Masukkan Id Layanan      : ")
    nama_layanan =  input("Masukkan Nama Layanan    : ") 
    deskripsi =     input("Masukkan Deskripsi       : ") 

    query_update_service = f"UPDATE service SET nama_layanan = {nama_layanan}, deskripsi = {deskripsi} WHERE id_layanan = {id_layanan}"

    cur.execute(query_update_service)

    conn.commit()
    print("service berhasil diupdate")

    cur.close()
    conn.close()

def update_status_penjemputan ():
    id_status_penjemputan = input("Masukkan Id Status   : ")
    nama_status =           input("Masukkan Nama Status : ") 

    query_update_status_penjemputan = f"UPDATE status_penjemputan SET nama_status = {nama_status} WHERE id_status_penjemputan = {id_status_penjemputan}"

    cur.execute(query_update_status_penjemputan)

    conn.commit()
    print("service berhasil diupdate")

    cur.close()
    conn.close()

def update_status_transaksi ():
    id_transaksi =                      input("Masukkan Id Transaksi    : ")
    deskripsi =                         input("Masukkan Deskripsi       : ") 
    user_id_petani =                    input("Masukkan Id Petani       : ") 
    pembayaran_id_pembayaran =          input("Masukkan Id Pembayaran   : ") 
    gudang_kode_gudang =                input("Masukkan Kode Gudang     : ") 
    kopi_id_kopi =                      input("Masukkan Id kopi         : ") 
    service_id_layanan =                input("Masukkan Id Layanan      : ") 
    pegawai_penjemputan_id_pegawai =    input("Masukkan Id Pegawai      : ") 
    kualitas_kopi_id_kualitas =         input("Masukkan Id Kualitas Kopi: ") 
    jadwal_penjemputan_id_penjemputan = input("Masukkan Id Penjemputan  : ") 

    query_update_transaksi = f"UPDATE transaksi SET deskripsi = {deskripsi}, user_id_petani = {user_id_petani}, pembayaran_id_pembayaran = {pembayaran_id_pembayaran}, gudang_kode_gudang = {gudang_kode_gudang}, kopi_id_kopi = {kopi_id_kopi}, service_id_layanan = {service_id_layanan},  pegawai_penjemputan_id_pegawai = {pegawai_penjemputan_id_pegawai}, kualitas_kopi_id_kualitas = {kualitas_kopi_id_kualitas}, jadwal_penjemputan_id_penjemputan = {jadwal_penjemputan_id_penjemputan} WHERE id_transaksi = {id_transaksi}"

    cur.execute(query_update_transaksi)

    conn.commit()
    print("transaksi berhasil diupdate")

    cur.close()
    conn.close()

def update_User ():
    id_petani =     input("Masukkan Id Petani       : ")
    nama =          input("Masukkan Nama            : ") 
    password_user = input("Masukkan Password        : ") 
    email =         input("Masukkan Email           : ") 
    nomor_telepon = input("Masukkan Nomor Telepon   : ") 
    deskripsi =     input("Masukkan Deskripsi       : ") 
    
    query_update_User = f"UPDATE User SET nama = {nama}, password_user = {password_user}, email = {email}, nomor_telepon = {nomor_telepon}, deskripsi = {deskripsi} WHERE id_petani = {id_petani}"

    cur.execute(query_update_User)

    conn.commit()
    print("transaksi berhasil diupdate")
#>>>>>>> 0a25802316c15be663339d845f48aab8d3ba0e1f

    cur.close()
    conn.close()


def delete_pegawai():
    read_pegawai_penjemputan(cur)
    id_pegawai = input('Masukan id pegawai yang ingin dihapus')
    delete_pegawai = f"DELETE FROM pegawai_penjemputan WHERE id_pegawai = {id_pegawai}"
    cur.execute(delete_pegawai)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()


def delete_layanan(service):
    read_service(cur)
    id_layanan = input('Masukan id layanan yang ingin dihapus: ')
    delete_layanan = f"DELETE FROM service WHERE id_layanan = {id_layanan}"
    cur.execute(delete_layanan)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def delete_transaksi(transaksi):
    read_transaksi(cur)
    id_transaksi = input('Masukan id Transaksi yang ingin dihapus: ')
    delete_transaksi = f"DELETE FROM transaksi WHERE id_transaksi = {id_transaksi}"
    cur.execute(delete_transaksi)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()


def delete_petani(User):
    read_User(cur)
    id_petani = input('Masukan id Petani yang ingin dihapus: ')
    delete_petani = f"DELETE FROM User WHERE id_petani = {id_petani}"
    cur.execute(delete_petani)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def delete_kualitas(kualitas_kopi):
    read_kualitas_kopi(cur)
    id_kualitas = input('Masukan id Kualitas Kopi yang ingin dihapus: ')
    delete_kualitas = f"DELETE FROM kualitas_kopi WHERE id_kualitas = {id_kualitas}"
    cur.execute(delete_kualitas)
    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()


def delete_status_penjemputan(status_penjemputan):
    read_status_penjemputan(cur)
    id_status_penjemputan = input('Masukan id Status Penjemputan yang ingin dihapus: ')
    delete_status_penjemputan = f"DELETE FROM status_penjemputan WHERE id_status_penjemputan={id_status_penjemputan}"
    cur.execute(delete_status_penjemputan)
    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def delete_jadwal_penjemputan(jadwal_penjemputan):
    read_jadwal_penjemputan(cur)
    id_penjemputan = input('Masukan id Jadwal Penjeputan yang ingin dihapus: ')
    delete_jadwal_penjemputan = f"DELETE FROM jadwal_penjemputan WHERE id_penjemputan = {id_penjemputan}"
    cur.execute(delete_jadwal_penjemputan)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def delete_gudang(gudang):

    read_gudang(cur)
    kode_gudang = input('Masukan Kode Gudang yang ingin dihapus')
    delete_gudang = f"DELETE FROM gudang WHERE kode_gudang = {kode_gudang}"
    cur.execute(delete_gudang)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def delete_pembayaran(pembayaran):
    read_pembayaran(cur)
    id_pembayaran = input('Masukan id Pembayaran yang ingin dihapus:') 
    delete_pembayaran = f"DELETE FROM pembayaran WHERE id_pembayaran = {id_pembayaran}"
    cur.execute(delete_pembayaran)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def delete_pembayaran_cash(cash):
    read_cash(cur)
    id_cash = input('Masukan id Pembayaran cash yang ingin dihapus: ')
    delete_pembayaran_cash = f"DELETE FROM cash WHERE id_cash = {id_cash}"
    cur.execute(delete_pembayaran_cash)
    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def delete_pembayaran_debit(debit):
    read_debit(cur)
    id_debit = input('Masukan id Pembayaran Debit yang ingin dihapus: ')
    delete_pembayaran_debit = f"DELETE FROM debit WHERE id_debit = {id_debit}"
    cur.execute(delete_pembayaran_debit)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def read_kualitas_kopi():    
    query = "SELECT * FROM kualitas_kopi"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
    
        print(i)
    
    cur.close()
    conn.close()

# total_input = int(input(f"Ingin menambahkan berapa data?: "))

# for i in range(total_input):
#     id_kualitas = input(f"Masukkan id kualitas: ")
#     nama_kualitas = int(input(f"Masukkan nama kualitas: "))
#     deskripsi = int(input(f"Masukkan deskripsi: "))
#     query_read_kualitas_kopi = f"INSERT INTO nama_kualitas = {nama_kualitas}, deskripsi = {deskripsi}, WHERE Id_Kualitas = {id_kualitas}"
   
#     cur.execute(query_read_kualitas_kopi) 

#     conn.commit()

#     read_kualitas_kopi(cur)
#     cur.close()
#     conn.close()


def read_pegawai_penjemputan(cur):    
    query = "SELECT * FROM pegawai_penjemputan"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# for i in range(total_input):
#     id_pegawai = input(f"Masukkan id pegawai: ")
#     nama_pegawai = int(input(f"Masukkan nama pegawai: "))
#     no_telepon = int(input(f"Masukkan no telepon: "))
#     admin_id_pengepul = int(input(f"Masukkan admin id pengepul: "))
#     alamat = int(input(f"Masukkan alamat: "))
#     query_read_pegawai_penjemputan = f"INSERT INTO nama_kualitas = {nama_kualitas}, deskripsi = {deskripsi}, WHERE Id_pegawai = {id_pegawai}"
   
#     cur.execute(query_read_pegawai_penjemputan) 

#     conn.commit()

#     read_pegawai_penjemputan(cur)
#     cur.close()
#     conn.close()


def read_pembayaran(cur):    
    query = "SELECT * FROM pembayaran"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# for i in range(total_input):
#     id_pembayaran = input(f"Masukkan id pembayaran: ")
#     metode_pembayaran = int(input(f"Masukkan metode pembayaran: "))
#     deskripsi = int(input(f"Masukkan deskripsi: "))
#     query_read_pembayaran = f"INSERT INTO nama_kualitas = {nama_kualitas}, deskripsi = {deskripsi}, WHERE Id_Pembayaran = {id_pembayaran}"
   
#     cur.execute(query_read_pembayaran) 

#     conn.commit()

#     read_pembayaran(cur)
#     cur.close()
#     conn.close()


def read_service(cur):    
    query = "SELECT * FROM service"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# for i in range(total_input):
#     id_layanan = input(f"Masukkan id layanan: ")
#     nama_layanan = int(input(f"Masukkan nama layanan: "))
#     deskripsi = int(input(f"Masukkan deskripsi: "))
#     query_read_service = f"INSERT INTO nama_kualitas = {nama_kualitas}, deskripsi = {deskripsi}, WHERE Id_Layanan = {id_layanan}"
   
#     cur.execute(query_read_service) 

#     conn.commit()

#     read_kualitas_kopi(cur)
#     cur.close()
#     conn.close()


def read_status_penjemputan(cur):    
    query = "SELECT * FROM status_penjemputan"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# for i in range(total_input):
#     id_status_penjemputan = input(f"Masukkan id status penjemputan: ")
#     nama_kualitas = int(input(f"Masukkan nama status: "))
#     query_read_status_penjemputan = f"INSERT INTO id_status = {id_status_penjemputan}, nama_kualitas = {nama_kualitas}, WHERE Id_Status_Penjemputan = {id_status_penjemputan}"
   
#     cur.execute(query_read_status_penjemputan) 

#     conn.commit()

#     read_status_penjemputan(cur)
#     cur.close()
#     conn.close()


def read_transaksi(cur):    
    query = "SELECT * FROM transaksi"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# for i in range(total_input):
#     id_transaksi = input(f"Masukkan id transaksi: ")
#     deskripsi = int(input(f"Masukkan deskripsi: "))
#     user_id_petani = int(input(f"Masukkan user id petani: "))
#     pembayaran_id_pembayaran = int(input(f"Masukkan pembyaran id pembayaran: "))
#     gudang_kode_gudang = int(input(f"Masukkan gudang kode gudang: "))
#     kopi_id_kopi = int(input(f"Masukkan kopi id kopi: "))
#     service_id_layanan = int(input(f"Masukkan service id layanan: "))
#     pegawai_penjemputan_id_pegawai = int(input(f"Masukkan pegawai penjemputan id pegawai: "))
#     kualitas_kopi_id_kualitas = int(input(f"Masukkan kualitas kopi id kualitas: "))
#     jadwal_penjemputan_id_penjemputan = int(input(f"Masukkan jadwal penjemputan id penjemputan: "))
#     query_read_transaksi = f"INSERT INTO id_transaksi = {id_transaksi}, deskripsi = {deskripsi}, user_id_petani = {user_id_petani}, pembayaran_id_pembayaran = {pembayaran_id_pembayaran}, gudang_kode_gudang = {gudang_kode_gudang}, kopi_id_kopi = {kopi_id_kopi}, service_id_layanan = {service_id_layanan}, pegawai_penjemputan_id_pegawai,WHERE Id_Transaksi = {id_transaksi}"
   
#     cur.execute(query_read_transaksi) 

#     conn.commit()

#     read_transaksi(cur)
#     cur.close()
#     conn.close()

# SELECT USER
def read_User(cur):    
    query = "SELECT * FROM User"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# total_input = int(input(f"Ingin menambahkan berapa data?: "))

# for i in range(total_input):
#     id_petani = int(input(f"Masukkan Id petani: "))
#     nama = input(f"Masukkan nama petani: ")
#     password_user = input(f"Masukkan password: ")
#     email = input(f"Masukkan email")
#     nomor_telepon = int(input("nomor telepon"))
#     deskripsi = input(f"Masukkan deskripsi")
#     query = f"INSERT INTO User(id_petani, nama, password_user, email, nomor_telepon, deskripsi) VALUES('{id_petani}', {nama}, {password_user}, {email}, {nomor_telepon}, {deskripsi})"
#     # query = f"INSERT INTO User(id_petani, nama, password_user, email, nomor_telepon, deskripsi) VALUES(%s, %s, %s)"
#     cur.execute(query, (id_petani, nama, password_user, email, nomor_telepon, deskripsi))

#     conn.commit()

#     read_User(cur)
#     cur.close()
#     conn.close()

# SELECT ADMIN
def read_admin(cur):
    query = "SELECT * FROM admin"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# total_input = int(input(f"Ingin menambahkan berapa data?: "))

# for i in range(total_input):
#     id_pengepul = int(input(f"Masukkan Id pengepul: "))
#     nama = input(f"Masukkan nama pengepul: ")
#     password_admin = input(f"Masukkan password admin: ")
#     email = input(f"Masukkan email: ")
#     nomor_telepon = int(input(f"Masukkan nomor telepon: "))
#     deskripsi1 = input(f"Masukkan deskripsi: ")
#     # query = f"INSERT INTO admin(id_pengepul, nama, password_admin, email, nomor_telepon, deskripsi1) VALUES(%s, %s, %s)"
#     cur.execute(query, (id_pengepul, nama, password_admin, email, nomor_telepon, deskripsi1))

#     conn.commit()

#     read_admin(cur)
#     cur.close()
#     conn.close()

# SELECT CASH
def read_cash(cur):
    query = "SELECT * FROM cash"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# for i in range(total_input):
#     id_pembayaran = int(input(f"Masukkan id pembayaran: "))
#     id_cash = int(input(f"Masukkan id cash: "))
#     nomor_telepon = int(input(f"Masukkan nomor telepon: "))
#     jumlah_pembayaran = int(input(f"Masukkan jumlsh pembayaran: "))   
#     # query = f"INSERT INTO User(id_pembayaran, id_cash, nomor_telepon, jumlah_pembayaran) VALUES(%s, %s, %s)"
#     cur.execute(query, (id_pembayaran, id_cash, nomor_telepon, jumlah_pembayaran))

#     conn.commit()

#     read_cash(cur)
#     cur.close()
#     conn.close()

# SELECT DEBIT
def read_debit(cur):
    query = "SELECT * FROM debit"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# for i in range(total_input):
#     id_pembayaran = int(input(f"Masukkan Id pembayaran: "))
#     id_debit = int(input(f"Masukkan Id debit: "))
#     nama_pemilik = input(f"Masukkan nama pemilik: ")
#     nama_bank = input(f"Masukkan nama bank: ")
#     nomor_rekening = int(input(f"Masukkan Id pengepul: "))
    
# # query = f"INSERT INTO debit(id_pembayaran, id_debit, nama_pemilik, nama_bank, nomor_rekening) VALUES(%s, %s, %s)"
#     cur.execute(query, (id_pembayaran, id_debit, nama_pemilik, nama_bank, nomor_rekening))

#     conn.commit()

#     read_debit(cur)
#     cur.close()
#     conn.close()

# SELECT GUDANG
def read_gudang(cur):
    query = "SELECT * FROM gudang"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# for i in range(total_input):
#     kode_gudang = int(input(f"Masukkan kode gudang: "))
#     kapasitas = int(input(f"Masukkan kapasitas: "))
#     deskripsi = input(f"Masukkan deskripsi: ")

#     # query = f"INSERT INTO gudang(kode_gudang, kapasitas, deskripsi) VALUES(%s, %s, %s)"
#     cur.execute(query, (kode_gudang, kapasitas, deskripsi))

#     conn.commit()

#     read_gudang(cur)
#     cur.close()
#     conn.close()

# SELECT JADWAL PENJEMPUTAN
def read_jadwal_penjemputan(cur):
    query = "SELECT * FROM jadwal_penjemputan"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    conn.close()

# for i in range(total_input):
#     id_penjemputan = int(input(f"Masukkan Id penjeputan: "))
#     waktu_penjemputan = input(f"Masukkan waktu penjemputan: ")
#     status_penjemputan = int(input(f"Masukkan status penjemputan: "))

#     # query = f"INSERT INTO penjemputan(id_penjemputan, waktu_penjemputan, status_penjemputan) VALUES(%s, %s, %s)"
#     cur.execute(query, (id_penjemputan, waktu_penjemputan, status_penjemputan))

#     conn.commit()

#     read_jadwal_penjemputan(cur)
#     cur.close()
#     conn.close()

def tambah_kualitas():
    id_kualitas = int(input(f"Masukkan Id kualitas: "))
    kualitas = input(f"Masukkan kualitas: ")
    deskripsi = input(f"Masukkan deskripsi: ")
    query = f"INSERT INTO kualitas_kopi(id_kualitas, nama_kualitas, deskripsi) VALUES(%s, %s, %s)"
    cur.execute(query, (id_kualitas, kualitas, deskripsi))
    conn.commit()
    cur.close()
    conn.close()