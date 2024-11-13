tahun = int(input('Masukan Tahun Yang Akan Anda Cek : '))
if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
    print('-----Hasil Pencarian-----')
    print(f'Tahun {tahun} Merupakan Tahun Kabisat')
else:
    print('-----Hasil Pencarian-----')
    print('Maaf Tahun Yang Anda Cek BUkan Tahun Kabisat')