#Mulai
#Menhitung berapa kali angka kedua dapat dibagi menjadi angka pertama
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MULAI>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Mengitung operation floor")
print("Note :output dari program ini adalah berapa kali angka kedua dapat dibagi menjadi angka pertama ")
x = int(input("Masukkan data bilangan bulat pertama : "))
y = int(input("Masukkan data bilangan bulat kedua   : "))

print(" Angka pertama anda adalah :", x,
      " Angka kedua anda adalah   :", y)
op_floor = x // y
print(" Hasil perhitungan adalah : ")
print(" Angka pertama yang anda input hanya dapat dibagi sebanyak  :", op_floor, "kali oleh angka kedua")



b = str(input("Ketik 'Yes' jika anda menyukai program ini: "))
if b == 'Yes':
    print("Terima kasih")
else :
    input("Klik enter untuk selesai :")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<SELESAI>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#Selesai
