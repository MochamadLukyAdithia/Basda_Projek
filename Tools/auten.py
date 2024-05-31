from Tools.CRUD import *
import Developer.DevPengepul as p
class Pengepul:
    def login_pengepul():
        print("LOGIN PENGEPUL")
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        if username == "admin" and password == "123":
            print("Login Berhasil")
            p.DevPengepul.show()
        else:
            
                print("Login Gagal")
                
                


class Petani:
    def login_petani():
        print("LOGIN PETANI")
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        if username == "petani" and password == "123":
            print("Login Berhasil")
        else:
            print("Login Gagal")