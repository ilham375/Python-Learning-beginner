# Perulangan (Loop)
# sumber: kelas terbuka -> https://youtu.be/Z4qfMhx4XzQ

# for kondisi:
#   aksi

# for with list
angka2 = [0, 1, 2, 3, 4]

for i in angka2:
    print(f"i sekarang => {i}")

print(f"akhir dari program 1 \n ")

# for with range
for i in range(5):
    print(f"i sekarang => {i}")

print(f"akhir dari program 2 \n ")

# for with range_2
for i in range(1, 10):  # artinya angka 1 sampai 9
    print(f"i sekarang => {i}")
    # bisa juga print selain di atas
    # print(f"saya ganteng sekali")

print(f"akhir dari program 3 \n ")

# for with string
data_str = "saya ganteng sekali"

for i in data_str:
    print(i)

print(f"akhir program 4 \n")
