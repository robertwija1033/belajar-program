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
#         print(total)
#     return total, i

# tupple = (8,2,3,-1,7)
# print(total(tupple))

# # def hasil(item) :
# #     hasil = 1
# #     for i in item :
# #         hasil *= i
# #     return hasil

# # tupple = (8,2,3,-1,7)
# # print(hasil(tupple))

# def kalimat(x) :
#     for a in x :
#         if a.isalpha() :
#             return True
#         return False
# while True :
#     try :
#         x = input('masukkan kalimat : ')
#         if x.isspace() :
#             raise Exception('yang anda masukkan adalah kosong')
#         elif not kalimat(x) :
#             raise Exception('masukkan minimal 1 huruf')
#     except Exception as d :
#         print('ERROR', d)
#     else :
#         def upper(lower) :
#             upper = 0
#             for a in x :
#                 if ord(a) >= ord('A') and ord(a) <= ord('Z') :
#                     upper += 1
#             return upper 

#         def lower(low) :
#             lower = 0
#             for a in x :
#                 if ord(a) >= ord('a') and ord(a) <= ord('z') :
#                     lower += 1
#             return lower
            

#         print('Sample String :',x)
#         print('expected Output :')
#         print('No. of Upper case characters : ', upper(x))
#         print('No. of Lower case characters : ', lower(x))
#     finally :
#         while True :
#             c = input('ulangi[y/n]')
#             if c in ['y','n'] :
#                 break
#         if c == 'n' :
#             break

def kalimat(n) :
    for b in n :
        if b.isdecimal() :
            return True
        return False
while True :
    try :
        n = input('angka : ')
        if n.isspace() :
            raise Exception('yang anda masukkan adalah kosong')
        elif not kalimat(n) :
            raise Exception('masukkan minimal 1 angka!')
    except Exception as d :
        print('ERROR', d)
    else :
        a = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh','delapan', 'sembilan', 'sepuluh']
        def bilangan(angka) :
            if angka <= 10 :
                return a[angka]
            elif angka == 11 :
                return 'sebelas'
            elif angka > 10 and angka <= 19 :
                return bilangan(angka % 10) + ' belas '
            elif angka > 19 and angka <= 99:
                return bilangan(angka // 10) + ' puluh ' + bilangan(angka % 10)
            elif angka == 100 :
                return "seratus"
            elif angka > 100:
                if angka > 100 and angka <= 109 :
                    return 'seratus ' + bilangan(angka % 100)  
                elif angka > 109 and angka <= 110:
                    return 'seratus ' + bilangan(angka % 100)
                elif angka > 110 and angka <= 999 :
                    return bilangan(angka // 100) + ' ratus ' + bilangan(angka % 100)
            if angka > 1000 :
                if angka > 1000 and angka <= 1009 :
                    return 'seribu ' + bilangan(angka % 1000)  
                elif angka > 1009 and angka <= 1999 :
                    return 'seribu ' + bilangan(angka % 1000)
                elif angka > 1999 and angka <= 9999 :
                    return bilangan(angka // 1000) + ' ribu ' + bilangan(angka % 1000)
            if angka > 10000 : 
                if angka > 10000 and angka <= 10009 :
                    return bilangan(angka // 1000) + ' ribu ' + bilangan(angka % 10000)  
                elif angka > 10009 and angka <= 19999 :
                    return bilangan(angka // 1000) + ' ribu ' + bilangan(angka % 10000)
                elif angka > 19999 and angka <= 99999 :
                    return bilangan(angka // 1000) + ' ribu ' + bilangan(angka % 10000)
            if angka >= 100000 : 
                if angka >= 100000 and angka <= 100009 :
                    return 'seratus ribu ' + bilangan(angka % 10000)  
                elif angka > 100009 and angka <= 199999 :
                    return 'seratus ribu ' + bilangan(angka % 100000)
                elif angka > 199999 and angka <= 999999 :
                    return bilangan(angka // 100000) + ' ratus ribu ' + bilangan(angka % 100000)
            if angka >= 1000000 : 
                if angka >= 1000000 and angka <= 1000009 :
                    return bilangan(angka // 1000000) + ' juta ' + bilangan(angka % 1000000)
                if angka > 1000009 and angka < 1999999 :
                    return bilangan(angka // 1000000) + ' juta ' + bilangan(angka % 1000000)
                if angka >= 1999999 and angka < 1000000000 :
                    return bilangan(angka // 1000000) + ' juta ' + bilangan(angka % 1000000)
            if angka >= 1000000000 : 
                if angka >= 1000000000 and angka <= 1000000009 :
                    return 'satu miliyar ' + bilangan(angka % 1000000000)  
                elif angka > 100009 and angka <= 1999999999 :
                    return 'satu miliyar ' + bilangan(angka % 100000000)
                elif angka > 1999999999 :
                    return bilangan(angka // 1000000000) + ' miliyar ' + bilangan(angka % 100000000)
            else :
                if angka == 1000 :
                    return 'seribu'
                elif angka == 1000000 :
                    return 'sejuta'

        m = str(n).split('.')

        x = int(m[0])
        y = int(m[-1])

        if '.' not in n :
            print(bilangan(x))
        elif '.' in n :
            print(bilangan(x) ,'koma', bilangan(y))
    finally :
            while True :
                f = input('ulangi[y/n] : ')
                if f in ['y','n'] :
                    break
            if f == 'n' :
                break

def kalimat(n) :
    for b in n :
        if b.isdecimal() :
            return True
        return False
while True :
    try :
        n = input('angka : ')
        if n.isspace() :
            raise Exception('yang anda masukkan adalah kosong')
        elif not kalimat(n) :
            raise Exception('masukkan minimal 1 angka!')
    except Exception as d :
        print('ERROR', d)
    else :
        a = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']
        def bilangan(angka) :
            if angka <= 10 :
                return a[angka]
            elif angka == 10 :
                return 'ten'
            elif angka == 11 :
                return 'eleven'
            elif angka == 12 :
                return "twelve"
            elif angka > 10 and angka <= 19 :
                return bilangan(angka % 10) + ' teen '
            elif angka > 59 and angka <= 99:
                return bilangan(angka // 10) + '-ty ' + bilangan(angka % 10)
            elif angka == 100 :
                return "seratus"
            elif angka > 100:
                if angka > 100 and angka <= 109 :
                    return 'one hundred ' + bilangan(angka % 100)  
                elif angka > 109 and angka <= 110:
                    return 'one hundred ' + bilangan(angka % 100)
                elif angka > 110 and angka <= 999 :
                    return bilangan(angka // 100) + ' hundred ' + bilangan(angka % 100)
            if angka > 1000 :
                if angka > 1000 and angka <= 1009 :
                    return 'one thousand ' + bilangan(angka % 1000)  
                elif angka > 1009 and angka <= 1999 :
                    return 'one thousand ' + bilangan(angka % 1000)
                elif angka > 1999 and angka <= 9999 :
                    return bilangan(angka // 1000) + ' thousand ' + bilangan(angka % 1000)
            if angka > 10000 : 
                if angka > 10000 and angka <= 10009 :
                    return bilangan(angka // 1000) + ' thousand ' + bilangan(angka % 10000)  
                elif angka > 10009 and angka <= 19999 :
                    return bilangan(angka // 1000) + ' thousand ' + bilangan(angka % 10000)
                elif angka > 19999 and angka <= 99999 :
                    return bilangan(angka // 1000) + ' thousand ' + bilangan(angka % 10000)
            if angka >= 100000 : 
                if angka >= 100000 and angka <= 100009 :
                    return 'one hundred thousand ' + bilangan(angka % 10000)  
                elif angka > 100009 and angka <= 199999 :
                    return 'one hundred thousand ' + bilangan(angka % 100000)
                elif angka > 199999 and angka <= 999999 :
                    return bilangan(angka // 100000) + ' hundred thousand ' + bilangan(angka % 100000)
            if angka >= 1000000 : 
                if angka >= 1000000 and angka <= 1000009 :
                    return bilangan(angka // 1000000) + ' million ' + bilangan(angka % 1000000)
                if angka > 1000009 and angka < 1999999 :
                    return bilangan(angka // 1000000) + ' million ' + bilangan(angka % 1000000)
                if angka >= 1999999 and angka < 1000000000 :
                    return bilangan(angka // 1000000) + ' million ' + bilangan(angka % 1000000)
            if angka >= 1000000000 : 
                if angka >= 1000000000 and angka <= 1000000009 :
                    return 'one billion ' + bilangan(angka % 1000000000)  
                elif angka > 100009 and angka <= 1999999999 :
                    return 'one billion ' + bilangan(angka % 100000000)
                elif angka > 1999999999 :
                    return bilangan(angka // 1000000000) + ' billion ' + bilangan(angka % 100000000)
            else :
                if angka >= 20 :
                    if angka // 10 == 2 :
                        return "twen-ty "+bilangan(angka % 10)
                    elif angka // 10 == 3 :
                        return "thir-ty "+bilangan(angka % 10)
                    elif angka // 10 == 4 :
                        return "for-ty "+bilangan(angka % 10)
                    elif angka // 10 == 5 :
                        return "fif-ty "+bilangan(angka % 10)
                    else :
                        return bilangan(angka // 10)+("-ty "if angka // 10 != 8 else "y ")+bilangan(angka % 10)
                elif angka == 1000 :
                    return 'one thousand'
                elif angka == 1000000 :
                    return 'one million'

        m = str(n).split('.')
        print(m)
        x = int(m[0])
        y = int(m[-1])

        if '.' not in n :
            print(bilangan(x))
        elif '.' in n :
            print(bilangan(x) ,'coma', bilangan(y))
    finally :
            while True :
                f = input('ulangi[y/n] : ')
                if f in ['y','n'] :
                    break
            if f == 'n' :
                break