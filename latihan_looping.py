# latihan perulangan membuat segitiga
# sumber: kelas terbuka -> https://youtu.be/szyfqq_whIg

sisi = 10

# 1. menggunakan For

print("Awal For")
jarak = 5
print("="*jarak)  # Mengeprint "=" sesuai jumlah yang ada di jarak
# dummy variable
count = 1

for i in range(sisi):
    print("*"*count)
    count += 1

print("Akhir For")

# 2. Menggunakan While

print("Awal While")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("Akhir While")

# 3. Hanya ganjil saja

print("Awal While")
count = 1
while True:
    if count % 2 == 1:
        # Print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # Akan break jika count melebihi sisi
    if count > sisi:
        break

print("Akhir While")

# 4. Segitiga sama kaki

print("Awal While")
count = 1
spasi = int(sisi/2)
while True:
    if count % 2 == 1:
        # Print jika ganjil
        print(" "*spasi, "*"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # Akan break jika count melebihi sisi
    if count > sisi:
        break

print("Akhir While")
