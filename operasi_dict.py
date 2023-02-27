# sumber: kelas terbuka -> https://youtu.be/6khlVRLJTl0

# operator dictionary

data_dict = {
    'cup': 'ucup surucup',
    'tong': 'otong surotong',
    'dung': 'dudung surudung',
}

# panjang dictionary
# untuk len di dictionary harus menggunakan huruf besar
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = 'cup'
CHEKKEY = KEY in data_dict  # hanya untuk mengecek key bukan value dari dictionary
print(f"apakah {KEY} ada di data_dict: {CHEKKEY}")

# mengakses value (read) menggunakan get
# .get -> untuk menandakan bahwa itu program dictionary
print(data_dict.get('cup'))
print(data_dict.get('kis'))  # output: none (karena tidak ada di data_dict)

# mengupdate data pada dictionary
data_dict.update({"cup": "surecep"})  # merubah/update value dari cup
print(data_dict)
# jika data yang dimasukkan tidak ada pada dictionary, maka akan ditambahkan di akhir
data_dict.update({'ilh': 'muhammad ilham anjayy'})
print(data_dict)

# mendelete data pada dictionary
del data_dict['ilh']
print(data_dict)
