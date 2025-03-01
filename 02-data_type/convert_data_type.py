#MENGKONVERSI TIPE DATA MENGGUNAKAN FUNCTION CONSTRUCTOR


nomor = 99
angka = 9.6
kata = "Aku"

print("ini integer")
print("ini adalah nomor integer: ", nomor)
print(type(nomor))#int
print("ini string")
print(type(kata)) #str
print("ini float")
print(type(angka)) #float

#convert dari integer ke float
nomor = float(nomor)
print("ini adalah nomor float: ", nomor)
print(type(nomor))