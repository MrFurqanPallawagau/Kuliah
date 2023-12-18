a = [2,3,1,0,3,1,1,0,5]
# akses item
print(a)
print(f"item indeks-0{a[0]}")
print(f"item indeks-3{a[0]}")
print(f"item indeks-terakhir: {a[len(a)-1]}")
# akses item indeks negatif
print(f"item indeks--1 {a[-1]}")
print(f"item indeks-pertama (-9): {a[-len(a)]}")
print(f"item indeks-1 (-8) {a[-8]}")
print(f"item indeks-5 (-4) {a[-4]}")
# akses indeks batas
print(f"item indeks:1,2,3 {a[1:4]}")
print(f"item indeks:1,2,... {a[1:]}")
print(f"item indeks:3,4,... {a[3:]}")
print(f"item indeks:0,1,2,3,4 {a[:5]}")
print(f"item indeks:semua {a[:]}")
# pengirisan indeks
print(f"item indeks:1,2,3 {a[1:4]}")
print(f"item indeks:2,3,4 {a[2:5]}")
print(f"item indeks:[1:8] {a[1:-1]}")

# Nested List
kelas = [('Agama',3),
         ('pancasila',2),
         ('PTI',2)]
print(f"data kelas {kelas}")
kelas.append((matkul4,3))
print(f"data kelas {kelas}")