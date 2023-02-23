# operasi
# sumber: kelas terbuka --> https://youtu.be/Xqvui6Bmrj0

# index   0(-3)  1(-2)    2(-1)
data = ["ucup", "otong", "dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index -1) = {data_terakhir}")

data_otong = data[1]
print(f"data otong = {data_otong}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# Manipulasi data list

# menambahkan item data pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1, "Asep")  # .insert(posisi, item)
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Jajang")
print(f"data ditambah lagi =\n{data}")
# output: ['ucup', 'Asep', 'otong', 'dudung', 'Jajang']

# menambah list dengan list
data_baru = ["ujang", "usep", "dadang"]
# .extend(list yang ingin ditambah) -> untuk menambah list
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# Ubah data

# kita ubah data 2 (otong) menjadi michael
data[2] = "Michael"  # merubah otong menjadi Michael
print(f"Data yang telah diubah = \n{data}")

# meremove data
data.remove("ujang")
print(f"Data remove = \n{data}")
''' catatan!! 
untuk data.remove() -> harus sesuai dengan huruf yang ada pada list, jika tidak maka akan eror
'''

# remove data paling belakang
data.pop()
print(f"Data remove paling belakang = \n{data}")
