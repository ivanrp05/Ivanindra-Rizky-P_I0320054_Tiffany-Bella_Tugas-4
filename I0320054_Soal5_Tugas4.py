#Mulai
#Bismillah


s = "Strings are awesome!"

print(type(s))

#Panjangnya harus 20
print("panjang dari s = %d" %len(s))

#Huruf pertama 'a' harusnya di index no 8
print("Kemunculan pertama a = %d" % s.index("a"))

#memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" % s[:5]) # Start to 5
print("Lima karakter berikutnya adalah '%s'" % s [5:10]) #5 to 10
print("Karakter ketiga belas adalah '%s'" % s [12]) # Just number 12
print("Karakter dengan indeks ganjil adalah '%s'" % s [1::2])
print("Lima karakter terakhir adalah '%s'" % s [-5:])

#konversikan ke uppercase
print("String dalam huruf besar: '%s'" % s.upper())

#Konversikan ke lowercase
print("String dalam huruf kecil:'%s'" % s.lower())

#Cek bagaimana string dimulai
if s.startswith("Str"):
    print("String dimulai dengan 'Str'. Good!")

#Cek bagaimana string itu diakhiri
if s.endswith("ome!"):
    print("String diakhiri dengan 'ome!'. Good!")

#pisahkan string menjadi tiga string yang terpisah,
#masing masing hanya berisi satu kata

print("Pisahkan kata kata dari string tersebut: %s" % s.split(" "))



