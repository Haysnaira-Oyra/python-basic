#Operasi Logika atau Boolean
#Not, Or, And, Xor

print('==== NOT ====')
a = False
c = not a
print('data a =', a)
print('------------------ NOT')
print('data c =', c)

print('==== OR ====')
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, ' OR', b, '=', c)
a = True
b = True
c = a or b
print(a, ' OR', b, '=', c)
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

print('==== AND ====')
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, ' AND', b, '=', c)
a = True
b = True
c = a and b
print(a, ' AND', b, '=', c)
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

print('==== XOR ====')
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, ' XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, ' XOR', b, '=', c)
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
