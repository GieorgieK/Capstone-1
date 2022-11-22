# Data Karyawan Perusahaan 
listKaryawan = [
    {
        'Nama' : 'Gieorgie',
        'No Hp' : '081355667788',
        'Email' : 'gieorgie@gmail.com', 
        'Divisi' : 'Finance'
    },
    {
        'Nama' : 'Jonatan',
        'No Hp' : '081312121212',
        'Email' : 'jonatan@gmail.com',
        'Divisi' : 'Engineer' 
    },
    {
        'Nama' : 'Michael',
        'No Hp' : '082145758565',
        'Email' : 'michael@gmail.com',
        'Divisi' : 'Security'
    },
    {
        'Nama' : 'Paras',
        'No Hp' : '081366448899',
        'Email' : 'paras@gmaail.com',
        'Divisi' : 'Hrd'
    },
    {
        'Nama' : 'Gracia',
        'No Hp' : '08123456789',
        'Email' : 'gracia@gmail.com',
        'Divisi' : 'Marketing'
    }
]

def menampilkanDataKaryawan () :
    menampilkanData = True
    while menampilkanData != '3':
        print('''
        Menu Data Karyawan :

        1. Menampilkan Seluruh Data Karyawan
        2. Mencari Data Karyawan
        3. Kembali Ke Menu Utama

        ''')
        menampilkanData = input('Untuk Menjalankan Program input angka didepan Pilihan Menu :')
        if menampilkanData == '1':
            print('Menampilkan Seluruh Data Karyawan \n')
            print('Id \t| Nama \t \t| No Hp \t| Email \t\t| Divisi \t')
            for i in range(len(listKaryawan)):
                print(f"{i+1} \t| {listKaryawan[i]['Nama']} \t| {listKaryawan[i]['No Hp']} \t| {listKaryawan[i]['Email']} \t| {listKaryawan[i]['Divisi']} \t")
        elif menampilkanData == '2':
            masukanNama = input('Masukan Data yang ingin ditelurusi: ')
            print(f'Data Karyawan {masukanNama} milik')
            for i in range(len(listKaryawan)):
                if masukanNama in listKaryawan[i].values():
                    print ('Id \t| Nama \t \t| No Hp \t| Email \t\t| Divisi \t')
                    print (f"{i+1} \t| {listKaryawan[i]['Nama']} \t| {listKaryawan[i]['No Hp']} \t| {listKaryawan[i]['Email']} \t| {listKaryawan[i]['Divisi']} \t")
                    break
            else :
                print (f'Tidak ditemukan data {masukanNama}')


def menambahkanDataKaryawan ():
    menambahkanData = True
    while menambahkanData !='2':
        print('''
        Menu Menambahkan Data Karyawan :
        
        1. Tambah Data Karyawan
        2. Kembali Ke Menu Utama
        ''')
        menambahkanData = input('Untuk Menjalankan Program input angka didepan Pilihan Menu :')
        if menambahkanData == '1':
            namaBaru = input('Masukan Nama Karyawan : ')
            for i in range(len(listKaryawan)):
                if namaBaru in listKaryawan[i].values() :
                    print(f'Data dengan nama {namaBaru} Sudah ada')
                    break
            else :
                noHPbaru = str(input('Masukan Nomor Hp : '))
                emailBaru = input('Masukan Email : ')
                divisiBaru = input('Masukan Divisi : ')
                while True:
                    konfirmasi = input('Masukan 1 untuk simpan dan 2 untuk batal : ')
                    if konfirmasi == '1' or konfirmasi == '2':
                        break
                if konfirmasi == '1':
                    listKaryawan.append({
                        'Nama' : namaBaru,
                        'No Hp' : noHPbaru,
                        'Email' : emailBaru,
                        'Divisi' : divisiBaru
                    })
                    print('Data Karyawan Tersimpan')
                elif konfirmasi == '2' :
                    print('Data Karyawan Dibatalkan')


def mengubahDataKaryawan():
    mengubahData = True
    while mengubahData != '2':
        print('''
        Menu Mengubah Data Karyawan :

        1. Mengubah Data
        2. Kembali Ke Menu Utama

        ''')
        mengubahData = input('Untuk Menjalankan Program input angka didepan Pilihan Menu : ')
        if mengubahData == '1':
            masukanNama = input('Masukan Data Yang ingin Ditelusuri : ')
            for i in range(len(listKaryawan)):
                if masukanNama in listKaryawan[i].values():
                    print ('Id \t| Nama \t \t| No Hp \t| Email \t\t| Divisi \t')
                    print (f"{i+1} \t| {listKaryawan[i]['Nama']} \t| {listKaryawan[i]['No Hp']} \t| {listKaryawan[i]['Email']} \t| {listKaryawan[i]['Divisi']} \t")
                    while True:
                        pilihMenu = input('Masukan 1 untuk Melanjutkan dan 2 untuk batal : ')
                        if pilihMenu == '1' or pilihMenu == '2':
                            break
                    if pilihMenu == '1':
                        while True:
                            keyubah = input('Masukan Kolom Data yang ingin di ubah : ')
                            if keyubah in listKaryawan[i].keys():
                                valueBaru = input(f'Masukan {keyubah} Data Baru : ')
                                while True : 
                                    konfirmasi = input('Masukan 1 untuk simpan dan 2 untuk batal : ')
                                    if konfirmasi == '1' or konfirmasi == '2':
                                        break
                                if konfirmasi == '1':
                                    listKaryawan[i][keyubah] = valueBaru
                                    print('Data Berhasil Di ubah')
                                    break
                                elif konfirmasi == '2':
                                    print('Pengubahan Data Dibatalkan')
                                    break
                    elif pilihMenu == '2':
                        print('Pengubahan Data Dibatalkan')
                        break
                    break
            else:
                print (f'Tidak ditemukan data {masukanNama}')    

    

def menghapusDataKaryawan ():
    menghapusData = True
    while menghapusData !='2':
        print('''
        Menu Menghapus Data Karyawan
        
        1. Menghapus Data 
        2. Kembali Ke Menu Utama
        
        ''')
        menghapusData = input('Untuk Menjalankan Program input angka didepan Pilihan Menu : ')
        if menghapusData =='1':
            masukanNama = input('Masukan Data Yang ingin Ditelusuri : ')
            for i in range(len(listKaryawan)):
                if masukanNama in listKaryawan[i].values():
                    print ('Id \t| Nama \t \t| No Hp \t| Email \t\t| Divisi \t')
                    print (f"{i+1} \t| {listKaryawan[i]['Nama']} \t| {listKaryawan[i]['No Hp']} \t| {listKaryawan[i]['Email']} \t| {listKaryawan[i]['Divisi']} \t")
                
                    while True :
                        pilihMenu = input('Masukan 1 untuk hapus data dan 2 untuk batal : ')
                        if pilihMenu == '1' or pilihMenu == '2' :
                            break
                    if pilihMenu == '1':
                        del listKaryawan[i]
                        print ('Data Telah Di Hapus')
                        break
                    elif pilihMenu == '2':
                        print ('Membatalkan Penghapusan Data')
                        break
            else :
                print (f'Tidak ditemukan data {masukanNama}')
                        

while True :
    pilihMenu = input(''' 
        Selamat Datang Di Dashboard Informasi Karyawan

        Silahkan pilih menu dibawah ini :
        1. Data Karyawan
        2. Menambah Data Karyawan
        3. Mengubah Data Karyawan
        4. Menghapus Data Karyawan
        5. Keluar Dashboard
        
        Silahkan Input Angka Menu : ''')
        
    if pilihMenu == '1':
        menampilkanDataKaryawan()
    elif pilihMenu == '2':
        menambahkanDataKaryawan()
    elif pilihMenu == '3':
        mengubahDataKaryawan()
    elif pilihMenu == '4':
        menghapusDataKaryawan()
    elif pilihMenu == '5':
        print('Terimakasih Selamat Melanjutkan Aktifitas Anda')
        break
    else :
        print('Masukan Menu Dengan benar')    