#KUIS 1 NOMOR 3
#BUATLAH SUATU CLASS KALKULATOR DIMANA BISA UNTUK TAMBAH, KURANG, BAGI, KALI
#CLASS KALKULATOR
print("3. CLASS CALCULATOR")
class calculator:
    def __init__(obj, a=0, b=0):
        obj.a=a
        obj.b=b
    def kurang (obj, a, b):
        hkurang= a-b
        #print ("a-b = " + str(hkurang))
        return hkurang
    def tambah(obj, a, b):
        htambah= a+b
        return htambah
    def kali (obj, a, b):
        hkali= a*b
        return hkali
    def bagi (obj, a, b):
        hbagi= a/b
        return hbagi
#menu operasi
print ("PILIH OPERASI YANG DIINGINKAN")
print("1. PENJUMLAHAN")
print ("2. PENGURANGAN")
print("3. PERKALIAN")
print("4. PEMBAGIAN")

#INPUTAN DARI USER
pilih= input("Masukkan pilihan: ")
a = int(input("Bilangan pertama: "))
b = int(input("Bilangan kedua: "))
run= calculator()
if pilih == '1':
    print(a, "+", b, "=", run.tambah(a,b))
elif pilih == '1':
    print(a, "-", b, "=", run.kurang(a,b))
elif pilih == '3':
    print(a, "*", b, "=", run.kali(a,b))
elif pilih == '4':
    print(a, "/", b, "=", run.bagi(a,b))
else:
    print("inputan salah")
