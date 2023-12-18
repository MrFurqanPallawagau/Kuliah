import os
os.system('cls')

pwd_benar ='si23d'
a = True
limit = 3
i = 0

while a:
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Password benar selamat anda login')
        a = False
    else:
        print('password salah!')
        a = True
        if i == limit:
            print('Kesempatan Hidup kamu habis')
            a = False
        else:print(f'kesempatan anda tersisa,{limit-i} kali')

buat password Berlapis 3
Jika salah: password salah,anda gagal pada halaman 1
Jika salah: password salah,anda gagal pada halaman 2
Jika salah: password salah,anda gagal pada halaman 3
jika benar: pertama: password Benar ,selamat datang di halaman 1
jika benar ke-2: Password Benar, Selamat datang dihalaman 2
Jika Benar ke-3: Password Benar,Selamat Anda Berhasil Login
Tiap Halaman,Memiliki Kesempatan 3 kali masukkan password

