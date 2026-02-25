"""
========================================================
MATERI PYTHON: VARIABLE (FONDASI KUAT UNTUK AI ENGINEER)
========================================================

1. APA ITU VARIABLE?
--------------------------------------------------------
Variable adalah nama (identifier) yang digunakan
untuk mereferensikan sebuah object di memory.

Konsep penting:
Variable ≠ kotak penyimpanan
Variable = label / penunjuk alamat object

Contoh:
x = 10

Penjelasan teknis:
- Python membuat object integer 10 di memory
- x menunjuk ke object tersebut
- "=" adalah assignment operator

========================================================
2. ATURAN PENULISAN VARIABLE
--------------------------------------------------------
- Tidak boleh diawali angka
- Tidak boleh mengandung spasi
- Tidak boleh simbol khusus (!@#$%)
- Boleh menggunakan underscore (_)
- Case-sensitive (umur ≠ Umur)

Contoh benar:
nilai_akhir = 90
namaLengkap = "Budi"

Contoh salah:
1nilai = 90      ❌
nama lengkap     ❌
nilai-akhir      ❌

========================================================
3. TIPE DATA DASAR DALAM VARIABLE
--------------------------------------------------------
int     -> bilangan bulat
float   -> bilangan desimal
str     -> teks
bool    -> True / False
None    -> tidak ada nilai

========================================================
4. CONTOH VARIABLE DAN OUTPUT
========================================================
"""

# Integer
umur = 25
print("Umur:", umur)
# Output:
# Umur: 25

# Float
tinggi = 170.5
print("Tinggi:", tinggi)
# Output:
# Tinggi: 170.5

# String
nama = "Andi"
print("Nama:", nama)
# Output:
# Nama: Andi

# Boolean
lulus = True
print("Lulus:", lulus)
# Output:
# Lulus: True

# None
data_kosong = None
print("Data:", data_kosong)
# Output:
# Data: None


"""
========================================================
5. BUILT-IN FUNCTION TERKAIT VARIABLE
========================================================
"""

angka = 100

# type() -> mengetahui tipe data
print(type(angka))
# Output:
# <class 'int'>

# id() -> melihat alamat memory object
print(id(angka))
# Output:
# (angka unik di memory)

# isinstance() -> cek apakah variable bertipe tertentu
print(isinstance(angka, int))
# Output:
# True

# bool() -> konversi ke boolean
print(bool(0))
# Output:
# False

print(bool(10))
# Output:
# True


"""
========================================================
6. VARIABLE ADALAH REFERENCE (KONSEP PENTING)
========================================================
"""

a = 10
b = a

print("a:", a)
print("b:", b)
# Output:
# a: 10
# b: 10

a = 20

print("a setelah diubah:", a)
print("b tetap:", b)
# Output:
# a setelah diubah: 20
# b tetap: 10

"""
Penjelasan:
Ketika a = 10
b = a
Maka b menunjuk ke object yang sama (10)

Saat a = 20
Python membuat object baru (20)
b tetap menunjuk ke 10

Inilah konsep reference + immutable
"""


"""
========================================================
7. LOGIKA DALAM VARIABLE
========================================================

Operator Perbandingan:
==   sama dengan
!=   tidak sama
>    lebih besar
<    lebih kecil
>=   lebih besar sama dengan
<=   lebih kecil sama dengan

Operator Boolean:
and
or
not
"""

nilai = 85

print(nilai > 75)
# Output:
# True

print(nilai == 90)
# Output:
# False

lulus = nilai >= 75
print("Lulus:", lulus)
# Output:
# Lulus: True

# Operator boolean
umur = 20
punya_sim = True

boleh_menyetir = umur >= 17 and punya_sim
print("Boleh menyetir:", boleh_menyetir)
# Output:
# Boleh menyetir: True


"""
========================================================
8. FAKTOR LOGIKA PADA VARIABLE
========================================================

Konsep Truthy & Falsy:

Falsy:
0
0.0
""
None
False

Selain itu dianggap True (Truthy)
"""

print(bool(""))
# Output:
# False

print(bool("AI"))
# Output:
# True

print(bool(0))
# Output:
# False

print(bool(100))
# Output:
# True


"""
========================================================
9. TYPE CASTING (PERUBAHAN TIPE DATA)
========================================================
"""

angka_string = "50"

angka_int = int(angka_string)
print(angka_int)
# Output:
# 50

print(type(angka_int))
# Output:
# <class 'int'>

float_number = float("10.5")
print(float_number)
# Output:
# 10.5


"""
========================================================
10. KESIMPULAN BESAR
========================================================

1. Variable adalah reference ke object.
2. "=" bukan menyimpan nilai, tetapi menghubungkan nama dengan object.
3. Python bersifat dynamic typing.
4. Gunakan type(), id(), isinstance() untuk memahami object.
5. Logical operator menghasilkan nilai boolean (True/False).
6. Konsep ini akan menjadi dasar:
   - Parameter model
   - Tensor
   - Weight update
   - Conditional training

========================================================
SELESAI - FONDASI VARIABLE
========================================================
"""
