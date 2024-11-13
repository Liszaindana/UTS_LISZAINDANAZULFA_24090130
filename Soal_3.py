total = 0
jumlah_barang = int(input('Masukan Jumlah Barang Anda : '))
for i in range(jumlah_barang):
    harga_barang = int(input(f"Masukkan harga barang ke-{i+1}: "))
    total += harga_barang
    total_harga = total
print(total_harga)