print('===== NAMA KELOMPOK =====')
print('Addin Noor Helmi')
print('Alfa Rizki Armi')
print('Nico Gawa Lahara')
print('M.Taqwa.Jusli')
print('Silmi Kaffah')
print('')
print('')
print("program menghitung huruf vokal dan konsonan ")

kata = input("Masukkan Kata = ")

panjangkata = len(kata)
i = 0
jumlahVokal = 0
jumlahKonsonan = 0
while i < panjangkata :
    if(kata[i] == "a" or kata[i] == "A" or kata[i] == "i" or kata[i] == "I" or kata[i] == "u"or kata[i] == "U" or kata[i] == "e" or kata[i] == "E" or kata[i] == "o" or kata[i] == "O") :
            jumlahVokal += i
    else :
        jumlahKonsonan += i
    i += 1
print("Jumlah Huruf Vokal Pada Kata = ", jumlahVokal)
print("Jumlah Huruf Konsonan Pada Kata = ", jumlahKonsonan)
