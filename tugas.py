# def angka_terbesar(a, b, c) :
#     terbesar = a
#     if a > b > c :
#         terbesar = a
#     elif b > c > a :
#         terbesar = b
#     else :
#         terbesar = c
        
#     return terbesar

# total = 3
# while total == 3 :
#     x = input('nilai a :')
#     y = input('nilai b :')
#     z = input('nilai c :')

#     print('nilai terbesar adalah : ', angka_terbesar(x, y, z))

# def total(items) :
#     total = 0
#     for i in items :
#         total += i
#     return total

# tupple = (8,2,3,-1,7)
# print(total(tupple))

# def hasil(item) :
#     hasil = 1
#     for i in item :
#         hasil *= i
#     return hasil

# tupple = (8,2,3,-1,7)
# print(hasil(tupple))

def upper(lower) :
    upper = 0
    for a in x :
        if ord(a) >= ord('A') and ord(a) <= ord('Z') :
            upper += 1
    return upper 

def lower(low) :
    lower = 0
    for a in x :
        if ord(a) >= ord('a') and ord(a) <= ord('z') :
            lower += 1
    return lower
    
x = 'The quick Brow Fox'
print('Sample String :',x)
print('expected Output :')
print('No. of Upper case characters : ', upper(x))
print('No. of Lower case characters : ', lower(x))

def lower(low) :
    lower = 0
    for alpha in range(ord('a'),ord('z')+1) :
        if chr(alpha) in x :
            lower += 1
    return lower
    
x = 'The quick Brow Fox'
print('Sample String :',x)
print('expected Output :')
print('No. of Upper case characters : ', upper(x))
print('No. of Lower case characters : ', lower(x))