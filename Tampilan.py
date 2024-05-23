import Tools.auten as auten

class Main:
    def display():
        # Buatkan tampilan untuk menanyakan mau login sebagai pengepul atau petani
        print("Login")
        print("1. Pengepul")
        print("2. Petani")
        data = input("Pilih Menu : ")
        if data == "1":
         auten.Pengepul.login_pengepul()
        elif data == "2":
            auten.Petani.login_petani()
        elif data not in ["1", "2"]:
            print("Menu tidak tersedia")
            Main.display()
        
Main.display()