# Nested List
kelas = [('Agama', 3),
         ('pancasila', 2),
         ('PTI', 2)]

print(f"data kelas {kelas}")
kelas.append(('matkul4', 3))
kelas.append(('matkul5', 3))  # Menambahkan matkul5 dengan jumlah sks 3
print(f"data kelas {kelas}")

i = 1
for matkul, sks in kelas:
    print(f'Nama mata kuliah {i}: {matkul} dengan jumlah sks: {sks}')
    i += 1

print('A.Alfurqan Pallawagau')
print('231031105')
print('Sistem Informasi D S1-reguler')
print('2023-Ganjil')

data_nilai = [90, 89, 93, 97]
jumlah_nilai = sum(data_nilai)
rata_rata = jumlah_nilai / len(data_nilai)
nilai_terkecil = min(data_nilai)
nilai_terbesar = max(data_nilai)

print(f"jumlah nilai Alfurqan adalah: {jumlah_nilai}")
print(f"Data Terbesar Alfurqan adalah: {nilai_terbesar}")
print(f"Data Terkecil Alfurqan adalah: {nilai_terkecil}")
print(f"Rata-rata nilai Alfurqan adalah: {rata_rata}")
kelas = [('matkul1', 3),
         ('matkul2', 2),
         ('matkul3', 2),
         ('matkul4', 3),
         ('matkul5', 3)]

i = 1
for matkul, sks in kelas:
    print(f'Nama mata kuliah {i}: {matkul} dengan jumlah sks: {sks}')
    i += 1

