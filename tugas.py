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

def kalimat(x) :
    for a in x :
        if a.isalpha() :
            return True
        return False
while True :
    try :
        x = input('masukkan kalimat : ')
        if x.isspace() :
            raise Exception('yang anda masukkan adalah kosong')
        elif not kalimat(x) :
            raise Exception('masukkan minimal 1 huruf')
    except Exception as d :
        print('ERROR', d)
    else :
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
            

        print('Sample String :',x)
        print('expected Output :')
        print('No. of Upper case characters : ', upper(x))
        print('No. of Lower case characters : ', lower(x))
    finally :
        while True :
            c = input('ulangi[y/n]')
            if c in ['y','n'] :
                break
        if c == 'n' :
            break