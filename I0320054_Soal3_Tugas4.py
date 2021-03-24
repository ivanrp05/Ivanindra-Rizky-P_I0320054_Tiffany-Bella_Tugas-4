#Bismillah
#Mulai
print("==========================================")
print("Selamat datang di bandara UNS")
print("==========================================")
print("Izinkan kami untuk mendata berat barang bawaan anda")
#Mengimput berat dalam Kg agar mudah
#Merubah Lbs menjadi Kg
a = 0.45
b = a * 50
print("Berat max untuk 1 orang penumpang adalah ", b , "Kg")
print("Silahkan input berat bawaan anda dalam Kg")
x = int(input("Masukkan berat barang bawaan anda : "))
if x > 22.5 :
    print("================================================================")
    print("Berat bawaan anda melebihi batas maximum :", x > 22.5)
    print("================================================================")
    print("Anda dapat mengurangi barang bawaan atau membayar fee lebih")
else :
    print("================================================================")
    print("Bawaan anda tidak melebihi batas maximum : ", x > 22.5)
    print("================================================================")
    print("Silahkan langsung menuju waiting room")

input("Tekan enter untuk kembali.....")

#Selesai


