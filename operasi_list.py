# sumber: kelas terbuka -> https://youtu.be/HVyMl3GIw20

data_angka = [2, 1, 2, 2, 6, 2, 3, 4, 5, 2, 8, 5]

print(f"data angka = \n{data_angka}")

# count data
# menghitung data berapa kali muncul pada list

jumlah_Data_2 = data_angka.count(2)  # .count(data list)
jumlah_Data_3 = data_angka.count(3)
print(f"Jumlah data 2 = {jumlah_Data_2}")
print(f"Jumlah data 3 = {jumlah_Data_3}")

# ambil posisi data

data = ["Ucup", "Otong", "Dudung", "Ujang"]

print(f"data = \n{data}")

# .index(data pada list) -> berfungsi untuk mencari letak/index data list
index_dudung = data.index("Dudung")

# output = 2 (karena Dudung pada list terletak pada index 2)
print(f"index si Dudung = {index_dudung}")

# mengurutkan list

print(f"data angka sebelum sort (urut) = \n{data_angka}")
data_angka.sort()  # .sort() -> untuk mengurutkan data pada list dari terkecil ke terbesar
print(f"data angka setelah sort (urut) = \n{data_angka}")

print(f"data = {data}")
data.sort()  # untuk data string akan diurutkan menurud alpabet(abc)
print(f"data sort = {data}")

# balik list

'''
.reverse() -> akan membalikan nilai data list dari yang sudah
diurutkan dari terkecil ke terbesar, menjadi terbesar ke terkecil
'''

data_angka.reverse()
data.reverse()
print(f"data di reverse setelah di urutkan = \n{data_angka} \n{data}")
