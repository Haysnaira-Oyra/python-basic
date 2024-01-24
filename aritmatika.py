#Operasi Aritmatika

a =  10
b = 4
#operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

#operasi kurang -
hasil = a - b
print(a, '-', b, '=', hasil)

#operasi kali *
hasil = a * b
print(a, '*', b, '=', hasil)

#operasi bagi /
hasil = a / b
print(a, '/', b, '=', hasil) #hasilnya float

#operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

#operasi modulus %
hasil = a % b
print(a, '%', b, '=', hasil)

#operasi floor division //
hasil = a // b
print(a, '//', b, '=', hasil)

#prioritas operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)

hasil = x + y * z
print(x, '+', y, '*', z, '=', hasil)
hasil = (x + y) * z
print('(', x, '+', y, ')', '*', z, '=', hasil)
