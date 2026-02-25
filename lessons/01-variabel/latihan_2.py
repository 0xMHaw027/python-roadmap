"""
========================================================
SOAL 2 - LEVEL HARD
VARIABLE + LOGIKA LANJUTAN
========================================================
Instruksi:
- Tidak boleh menggunakan if
- Tidak boleh menggunakan loop
- Tidak boleh membuat function
- Gunakan hanya variable, assignment,
  built-in function, comparison, boolean operator
========================================================
"""


# ======================================================
# SOAL 1 - REFERENCE CHAIN
# ------------------------------------------------------
# Buat:
# a = 100
# b = a
# c = b
#
# Tampilkan id(a), id(b), id(c)

# Lalu ubah:
# a = 200
#
# Tampilkan kembali id(a), id(b), id(c)
#
# Jelaskan melalui output apakah b dan c ikut berubah.
# ======================================================
a = 100
b = a
c = b
print (f"{id(a)} , {id(b)} , {id(c)}")
a = 200
print (f"{id(a)} , {id(b)} , {id(c)}")
# b dan c tidak ikut berubah , b dan c masih merujuk pada object pertama 100 , sedangkan python membuat object baru 200 yang merujuk pada variable a


# ======================================================
# SOAL 2 - BOOLEAN EVALUATION CHAIN
# ------------------------------------------------------
# Buat:
# x = 10
# y = 0
# z = "AI"
#
# Buat variable hasil dengan ekspresi:
# hasil = x and y or z
#
# Tampilkan hasil dan type(hasil)
#
# Pahami bagaimana Python mengevaluasi ekspresi ini.
# ======================================================
x = 10
y = 0
z = "AI"

hasil = x and y or z
print (f"{hasil} , {type(hasil)}")

# x and y
# x = 10 (truthy)
# maka hasilnya = y
# y = 0 (falsy)
# Jadi ekspresi jadi:
# 0 or z
# 0 falsy → maka hasil = z

# ======================================================
# SOAL 3 - DYNAMIC TYPING EDGE CASE
# ------------------------------------------------------
# Buat:
# data = "50"
#
# Ubah menjadi integer
# Lalu ubah lagi menjadi boolean menggunakan bool()
#
# Tampilkan nilai dan tipe pada setiap tahap perubahan.
# ======================================================
data = "50"
print (f"{data} : {type(data)}")
dataInt = int(data)
print (f"{dataInt} : {type(dataInt)}")
dataBool = bool(data)
print (f"{dataBool} : {type(dataBool)}")




# ======================================================
# SOAL 4 - MULTI TYPE CHECK
# ------------------------------------------------------
# Buat:
# value = 0
#
# Buat variable cek_tipe yang bernilai True
# jika value adalah int ATAU float
#
# Gunakan isinstance()
#
# Tampilkan hasil cek_tipe
# ======================================================
value = 0
cek_tipe = isinstance(value,int) or isinstance(value,float)
print (f"{cek_tipe}")

# ======================================================
# SOAL 5 - MEMORY & RE-ASSIGNMENT TRICK
# ------------------------------------------------------
# Buat:
# angka = 256
# salinan = angka
#
# Tampilkan id(angka) dan id(salinan)
#
# Lalu lakukan:
# angka = angka
#
# Tampilkan kembali id(angka) dan id(salinan)
#
# Apakah berubah? Pahami kenapa.
# ======================================================

angka = 256
salinan = angka
print (f"{id(angka)} , {id(salinan)}")
angka = angka
print (f"{id(angka)} , {id(salinan)}")

# Penjelasan:
# - angka dan salinan menunjuk object yang sama.
# - angka = angka tidak membuat object baru.
# - ID tetap sama karena reference tidak berubah.

# Catatan:
# Integer kecil (-5 sampai 256 biasanya)
# di-cache oleh Python (integer interning).
"""
========================================================
SELESAI
========================================================
Level ini menguji:
- Reference reasoning
- Boolean evaluation tanpa if
- Dynamic typing
- isinstance multi-type
- Memory identity behavior

Setelah selesai kirim hasil kodenya.
Aku akan review seperti technical mentor.
========================================================
"""
