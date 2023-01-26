# Date and Time
# link documentation: https://docs.python.org/3/library/datetime.html

import datetime as dt

print("Masukan Tanggal, Bulan dan Tahun anda")

tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()  # tanggal hari ini
print(f"hari ini adalah tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir

# merubah tipe data "umur_hari" dari date > days
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Umur anda : {umur_tahun} tahun, {umur_bulan_sisa} bulan")
print(f"Anda lahir pada hari : {tanggal_lahir:%A}")  # %A for days
