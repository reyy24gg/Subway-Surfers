class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(f"{self.nama} sedang berlari menyusuri rel kereta, menghindari kejaran inspektur!")

    def ambil_koin(self, jumlah):
        if not self.is_running:
            print(f"{self.nama} tidak bisa mengambil koin karena game over.")
            return
        self.koin += jumlah
        self.skor += jumlah * 10
        print(f"{self.nama} mengambil {jumlah} koin! Total koin sekarang: {self.koin}")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"{self.nama} menabrak rintangan! Tertangkap inspektur dan anjingnya.")
        print("Game Over!")

    def info_player(self):
        if self.is_running:
            status = "Sedang Berlari"
        else:
            status = "Game Over"
        print(f"Nama     : {self.nama}")
        print(f"Skor     : {self.skor}")
        print(f"Koin     : {self.koin}")
        print(f"Status   : {status}")


# Uji coba
player1 = KarakterSurfer("Jake")

print("Status awal player:")
player1.info_player()

print()
player1.berlari()

print()
player1.ambil_koin(10)
player1.ambil_koin(20)

print()
print("Status setelah mengambil koin:")
player1.info_player()

print()
player1.tabrak_rintangan()

print()
print("Status setelah menabrak rintangan:")
player1.info_player()

