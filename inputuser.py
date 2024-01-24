#Input User

#Data yang dimasukan pasti string
data = input("Masukan Data :")
print("data = ", data, ", type =", type(data))

#Jika kita ingin mengambil int, maka
angka = int(input("Masukan Angka : "))
print("data = ", angka, ", type =", type(angka))

angkapecahan = float(input("Masukan Angka Pecahan : "))
print("data = ", angkapecahan, ", type =", type(angkapecahan))

#Bagaimana dengan boolean
biner = bool(int(input("Masukan Nilai Boolean : ")))
print("data = ", biner, ", type =", type(biner))