"""
========================================================
LATIHAN VARIABLE MURNI
========================================================
Kerjakan tanpa operasi matematika,
tanpa perbandingan, tanpa boolean operator.
========================================================
"""


# ======================================================
# SOAL 1
# ------------------------------------------------------
# Buat 5 variable dengan tipe berbeda:
# int, float, str, bool, None
# Tampilkan tipe masing-masing menggunakan type()
# ======================================================
variableInt = 50
variableFloat = 50.5
variableStr = "Hamw"
variableBool = True
variableNone = None

print (f"{type(variableInt)} , {type(variableFloat)} , {type(variableStr)} , {type(variableBool)} , {type(variableNone)}")

# ======================================================
# SOAL 2
# ------------------------------------------------------
# Buat variable x = 500
# Buat variable y = x
# Tampilkan id(x) dan id(y)
# ======================================================
x = 500
y = x

print (f"Id x :{id(x)} , Id y : {id(y)}")


# ======================================================
# SOAL 3
# ------------------------------------------------------
# Buat variable data = 100
# Tampilkan id(data)
# Ubah data menjadi string "Seratus"
# Tampilkan kembali id(data)
# ======================================================
data = 100
print (f"Id Data : {id(data)}")
data = "seratus"
print (f"Id Data : {id(data)}")


# ======================================================
# SOAL 4
# ------------------------------------------------------
# Gunakan multiple assignment untuk membuat
# variable a, b, c dengan nilai berbeda.
# Tampilkan masing-masing nilainya.
# ======================================================
a,b,c = 3,4,5
print (f"a = {a} , b = {b} , c : {c}")

# ======================================================
# SOAL 5
# ------------------------------------------------------
# Buat variable angka = 1000
# Gunakan isinstance() untuk mengecek
# apakah angka bertipe int
# Hapus variable angka menggunakan del
# ======================================================
angka = 1000
print (f"{isinstance(angka,int)}")
del angka



"""
========================================================
SELESAI
========================================================
Setelah selesai kirim jawabanmu.
Aku akan review sebagai code reviewer engineering.
========================================================
"""
