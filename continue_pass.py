# continue and pass
# sumber: kelas terbuka -> https://youtu.be/hGvikdHVRME

# pass -> dia berfungsi dummy, tidak akan di eksekusi

angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass  # ini tidak akan dieksekusi

    print(angka)


# continue

angka = 0

print(f"angka sekarang -> {angka} \n")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice!")
        continue  # akan membuat loop meloncat ke awal dan menskip step dibawahnya

    print("whatuppp!!!")

print("Nice!")
