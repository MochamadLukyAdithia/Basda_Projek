

def delete_pengepul(admin):
    read_pengepul(cur)
    id_pengepul = input('Masukkan id pengepul yang ingin dihapus: ') 
    delete_pengepul = f"DELETE FROM admin WHERE id_pengepul = {id_pengepul}"
    cur.execute(delete_pengepul)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()



def delete_pegawai(pegawai_penjemputan):
    read_pegawai(cur)
    id_pegawai = input('Masukan id pegawai yang ingin dihapus')
    delete_pegawai = f"DELETE FROM pegawai_penjemputan WHERE id_pegawai = {id_pegawai}"
    cur.execute(delete_pegawai)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()


def delete_layanan(service):
    read_layanan(cur)
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
    read_petani(cur)
    id_petani = input('Masukan id Petani yang ingin dihapus: ')
    delete_petani = f"DELETE FROM User WHERE id_petani = {id_petani}"
    cur.execute(delete_petani)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def delete_kualitas(kualitas_kopi):
    read_kualitas(cur)
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
    read_penjemputan(cur)
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
    read_pembayaran_cash(cur)
    id_cash = input('Masukan id Pembayaran cash yang ingin dihapus: ')
    delete_pembayaran_cash = f"DELETE FROM cash WHERE id_cash = {id_cash}"
    cur.execute(delete_pembayaran_cash)
    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()

def delete_pembayaran_debit(debit):
    read_pembayaran_debit(cur)
    id_debit = input('Masukan id Pembayaran Debit yang ingin dihapus: ')
    delete_pembayaran_debit = f"DELETE FROM debit WHERE id_debit = {id_debit}"
    cur.execute(delete_pembayaran_debit)

    conn.commit()
    print(f"total baris yang dihapus: {cur.rowcount}")

    cur.close()
    conn.close()