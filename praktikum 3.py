nama = 'Alfurqan Pallawagau'
nim = '231031105'
prodi = 'Sistem Informasi D'
meet = 'praktikum 3'
email = 'dowloadpa@gmail.com'

sp = 40
#print(len(nama))#19

print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))

print()

print(f'''\tHalo, selamat datang perkenalkan nama saya {nama} dengan NIM {nim} dari prodi {prodi}. Ini adalah file {meet}.
''')
print(f'''Halo, selamat datang perkenalkan nama saya {nama} dengan NIM {nim} dari prodi {prodi}. Ini adalah file {meet}.
''')


p = paragraf.format(nama,nim,prodi,meet)
print(p)




#1. input nilai x
x = int (input('Masukkan Nilai'))
#2. cek1 apakah x>5 true
cek1 = x>5
#3. cek2 apakah x<9 true
cek2 = x<9
#4. status = cek1 and cek2
status = cek1 and cek2
#5. cetak status
print('Hasilnya adalah',status)
#+++++++++++++5------------9+++++++++++
# 1. input x
x = int(input('masukkan nilai '))
# 2. cek1 apakah x<5 true
cek1 = x<=5
#3. cel2 apakah x>9 false
cek2 = x>=9
#4. status = cek1 or cek2 true
status = cek1 or cek2
#5 .cetak status
print('hasilnya adalah',status)

# +++++5------9+++++13------
# 1. input x
x = int(input('masukkan nilai +++5--9++13--= '))
# 2. cek1 x<5
cek1 = x<5
# 3. cek2 x>9
cek2 = x>9
# 4. cek3 x<13
cek3 = x<13
# 5. status cek1 or cek2 and cek3
status = cek1 or cek2 and cek3
# 6. cetak status
print('hasilnya adalah',status)
#tugas
