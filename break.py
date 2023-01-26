# Break -> akan langsung memfinis program

# angka = 0

# while angka < 5:
#     angka += 1
#     print(f"angka sekarang -> {angka}")

#     if angka == 3:
#         print("nice!")
#         break  # akan memfinis program ke akhir

#     print("wassup!")

# print("cukup Finiss!")

nilai_int = int(input("Hitung sampai = "))

angka = 0

while True:
    angka += 1
    print(f"count {angka}")

    if angka == nilai_int:
        print("nice!!")
        break  # akan memfinis program ke akhir

    print("whatupp")

print("cukup finish")
