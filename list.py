# LIST
# sumber: kelas terbuka --> https://youtu.be/tERK7b5Woqs

# Kumpulan data numbers
data_angka = [1, 2, 3, 4, 5]
print(data_angka)

# Kumpulan data string
data_string = ["ucup", "otong", "odah"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "bala-bala", 2, "cireng", "otong", True]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0, 10, 2)  # range(start,stop,step)
print(data_range)  # output = range(0,10,2)
data_list = list(data_range)  # merubah data_range menjadi list
print(data_list)  # output = [0,2,4,6,8]

# membuat list dengan for loop
list_pake_for = [i**2 for i in range(0, 10)]  # i kuadrat 2
print(list_pake_for)

# membuat list dengan for dan if
list_pake_for_if = [i**2 for i in range(0, 10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)  # output [0,2,4,6,8]

list_pake_for_if = [i for i in range(0, 10) if i % 2 == 1]
print(list_pake_for_if)  # output [1,3,5,7,9]
