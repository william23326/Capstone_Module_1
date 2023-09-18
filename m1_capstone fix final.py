menus = ['Nama', 'Tanggal Lahir', 'Gender', 'Jabatan', 'Nomor HP', 'Gaji', 'Tanggal Bergabung']
database_karyawan = [
    {'Nama': 'Andrew', 'ID Karyawan': 'MIB 1', 'Gender':'Male',  'Nomor HP':'08123456', 'Tanggal Lahir': '15 Juni 1996', 'Jabatan': 'Project Officer', 'Gaji': 6500000, 'Tanggal Bergabung': '10 Desember 2021'},
    {'Nama': 'Bryan', 'ID Karyawan': 'MIB 2', 'Gender':'Male',  'Nomor HP':'123123', 'Tanggal Lahir': '4 Maret 1997', 'Jabatan': 'Project Officer', 'Gaji': 7000000, 'Tanggal Bergabung': '14 November 2022'},
    {'Nama': 'Cevin', 'ID Karyawan': 'MIB 3', 'Gender':'Male',  'Nomor HP':'543534', 'Tanggal Lahir': '7 Agustus 1996', 'Jabatan': 'Social Media Manager', 'Gaji': 9000000, 'Tanggal Bergabung': '5 Februari 2023'},
    {'Nama': 'Julio', 'ID Karyawan': 'MIB 4', 'Gender':'Male',  'Nomor HP':'67546745', 'Tanggal Lahir': '9 Juli 1993', 'Jabatan': 'Project Manager', 'Gaji': 12000000, 'Tanggal Bergabung': '17 Mei 2019'},
    {'Nama': 'Ruth', 'ID Karyawan': 'MIB 5', 'Gender':'Female',  'Nomor HP':'2452345245', 'Tanggal Lahir': '19 Januari 1994', 'Jabatan': 'Business Development', 'Gaji': 13000000, 'Tanggal Bergabung': '16 Maret 2023'}
]

def printMenu():
    input_angka = 0
    while(input_angka != 5):
        print('PORTAL DATA KARYAWAN PT SEMOGA SEMUA LULUS PURWADHIKA')
        print('=====================================================')
        print('1. Tampilkan Data Karyawan')
        print('2. Generate Data Karyawan')
        print('3. Update Data Karyawan')
        print('4. Hapus Data Karyawan')
        print('5. Exit')
        print('=====================================================')
        try:
            input_angka = int(input('Masukkan nomor menu: '))
            getMenu(input_angka)
        except ValueError:
            print('Masukkan nomor menu yang valid.')

def read():
    while True:
        print('''
------------------------      
   MENU DATA KARYAWAN
------------------------
    1. Tampilkan Data Seluruh Karyawan
    2. Tampilkan Data Karyawan
    3. Cari Data Karyawan
    4. Urutkan Data Karyawan         
              
    5. Main Menu
            ''')
        
        input_angka = int(input('Masukkan nomor menu:  '))

        if input_angka == 1:
            getAllKaryawan() 
        elif input_angka == 2:
            id_karyawan = input('Masukkan ID Karyawan yang ingin ditampilkan (ex: MIB 1): ')
            getKaryawan(id_karyawan)
        elif input_angka == 3:
            nama = input('Masukkan Nama Karyawan yang ingin dicari (ex: John): ')
            searchKaryawan(nama)
        elif input_angka == 4:
            sortKaryawan()
        elif input_angka == 5:
            break
        else:
            print('Masukkan nomor menu yang valid.')

def create():
    while True:
        print('''
---------------------------------
      GENERATE DATA KARYAWAN
---------------------------------
    1. Tambahkan Data Karyawan
              
    2. Main Menu
                ''')
        
        input_angka = int(input('Masukkan nomor menu: '))

        if input_angka == 1:
             karyawan = addKaryawanMenu()
             addKaryawan(karyawan)
        elif input_angka == 2:
            break
        else:
            print('Masukkan nomor menu yang valid.')
 
def update():
    while True:
        print('''
-----------------------------------
        UPDATE DATA KARYAWAN
-----------------------------------
    1. Perbaharui Data Karyawan
              
    2. Main Menu
                ''') 
        input_angka = int(input('Masukkan nomor menu: '))

        if input_angka == 1:
            id_karyawan = baca_input('Masukkan ID Karyawan yang ingin diupdate (ex: MIB 1): ')
            updateDataKaryawan(id_karyawan)
        elif input_angka == 2:
           break
        else:
            print('Masukkan nomor menu yang valid.')

def delete():
    while True:
         print('''
-----------------------------------
        HAPUS DATA KARYAWAN
-----------------------------------
    1. Hapus Data Karyawan
    2. Hapus Seluruh Data Karyawan
               
    3. Main Menu
        ''')
         input_angka = int(input('Masukkan nomor menu: '))

         if input_angka == 1:
            id_karyawan = baca_input('Masukkan ID Karyawan yang ingin dihapus (ex: MIB 1): ')
            deleteKaryawan(id_karyawan)
         elif input_angka == 2:
             konfirmasi = input('Apakah benar ingin menghapus semua data? Pilih y untuk hapus atau n untuk batalkan (y/n): ')
             if konfirmasi.lower() == 'y':
                total_karyawan = len(database_karyawan)
                database_karyawan.clear()
                print(f'{total_karyawan} data karyawan berhasil dihapus')
             elif konfirmasi.lower() == 'n':
                 delete()
         elif input_angka == 3: 
             printMenu()
         else: 
             print('Masukkan nomor menu yang valid.')
             
def getMenu(input_angka):
    if input_angka == 1:
        read()
    elif input_angka == 2:
        create()
    elif input_angka == 3:
        update()
    elif input_angka == 4:
        delete()
    elif input_angka == 5:
        exit()
    else:
        print('Menu yang dipilih tidak valid!')

# Untuk menampilkan seluruh data karyawan yang ada dalam database
def getAllKaryawan():
    if len(database_karyawan) == 0:
        print('Data karyawan tidak ditemukan')
        return
    print('DATA KARYAWAN KESELURUHAN')
    print('=========================')
    for karyawan in database_karyawan:
        print(f"==========({karyawan['ID Karyawan']})==========")   # mengambil value dari key ID Karyawan dalam database karyawan
        for menu in menus:
            print(f"{menu}: {karyawan[menu]}")
        print('===========================')
    print(f'Total Karyawan: {len(database_karyawan)}')

# Untuk mencari data karyawan berdasarkan ID nya
def getKaryawan(id_karyawan):
    for karyawan in database_karyawan:
        if id_karyawan.upper() == karyawan['ID Karyawan']:
            print(f"==========({karyawan['ID Karyawan']})==========")
            for menu in menus:
                print(f"{menu}: {karyawan[menu]}")
            print('================================================')
            return 
    print('ID Karyawan tersebut tidak ditemukan.')

# Untuk mencari data karyawan berdasarkan nama
def searchKaryawan(nama):
    is_found = False
    for karyawan in database_karyawan:
        if nama.lower() in karyawan['Nama'].lower():
            is_found = True
            print(f"==========({karyawan['ID Karyawan']})==========")
            for menu in menus:
                print(f"{menu}: {karyawan[menu]}")
            print('================================================')
    if is_found == False:
        print(f'Tidak ada data yang ditemukan untuk {nama}')

# Function untuk semua input
def baca_input(kalimat):
    var = input(kalimat)
    if var == '-1':
        return printMenu()
    return var

def sortKaryawan():
    while True:
        print('''
-----------------------------------
    URUTKAN DATA KARYAWAN
-----------------------------------
    1. Urutkan berdasarkan Nama
    2. Urutkan berdasarkan ID Karyawan          
    3. Urutkan berdasarkan Tanggal Lahir
    4. Urutkan berdasarkan Gender
    5. Urutkan berdasarkan Jabatan
    6. Urutkan berdasarkan Gaji
    7. Urutkan berdasarkan Tanggal Bergabung
              
    8. Main Menu
        ''')
        input_angka = int(input('Masukkan nomor menu: '))

        if input_angka == 1:
            printSortedKaryawanByCriteria('Nama')
        elif input_angka == 2:
            printSortedKaryawanByCriteria('ID Karyawan')
        elif input_angka == 3:
            printSortedKaryawanByCriteria('Tanggal Lahir')
        elif input_angka == 4:
            printSortedKaryawanByCriteria('Gender')
        elif input_angka == 5:
            printSortedKaryawanByCriteria('Jabatan')
        elif input_angka == 6:
            printSortedKaryawanByCriteria('Gaji')
        elif input_angka == 7:
            printSortedKaryawanByCriteria('Tanggal Bergabung')
        elif input_angka == 8:
            break
        else:
            print('Masukkan nomor yang valid.')

from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'id_ID')

# lambda digunakan untuk mengambil nilai 'Nama' dari setiap elemen karyawan (k) 
# dalam database_karyawan. Kemudian, nilai 'Nama' 
# ini digunakan sebagai dasar pengurutan data karyawan.
def sortKaryawanByCriteria(criteria, ascending=True):
    if criteria == 'Nama':
        key_function = lambda k: k['Nama']
    elif criteria == 'ID Karyawan':
        key_function = lambda k: k['ID Karyawan']
    elif criteria == 'Tanggal Lahir':
        key_function = lambda k: datetime.strptime(k['Tanggal Lahir'], '%d %B %Y')
    elif criteria == 'Gender':
        key_function = lambda k: k['Gender']
    elif criteria == 'Jabatan':
        key_function = lambda k: k['Jabatan']
    elif criteria == 'Gaji':
        key_function = lambda k: k['Gaji']
    elif criteria == 'Tanggal Bergabung':
        key_function = lambda k: datetime.strptime(k['Tanggal Bergabung'], '%d %B %Y')
    else:
        print("Kriteria pengurutan tidak valid.")
        return
    sorted_karyawan = sorted(database_karyawan, key=key_function, reverse=not ascending)
    return sorted_karyawan

def printSortedKaryawanByCriteria(criteria, ascending=True):
    sorted_karyawan = sortKaryawanByCriteria(criteria, ascending)
    
    if sorted_karyawan is None:
        return

    while True:
        print(f"Pilihan urutan berdasarkan {criteria}:")
        print("1. Ascending (A-Z)")
        print("2. Descending (Z-A)")
        print("3. Kembali ke Menu Urutkan Data Karyawan")
        input_angka = int(input("Masukkan nomor urutan: "))

        if input_angka == 1:
            ascending = True
        elif input_angka == 2:
            ascending = False
        elif input_angka == 3:
            return
        else:
            print("Masukkan nomor urutan yang valid.")
            continue

        sorted_karyawan = sortKaryawanByCriteria(criteria, ascending)
        print(f"\nData Karyawan yang Diurutkan berdasarkan {criteria}:")
        for karyawan in sorted_karyawan:
            print(f"Nama: {karyawan['Nama']}, ID Karyawan: {karyawan['ID Karyawan']}, Gender: {karyawan['Gender']}, Nomor HP: {karyawan['Nomor HP']}, Tanggal Lahir: {karyawan['Tanggal Lahir']}, Jabatan: {karyawan['Jabatan']}, Gaji: {karyawan['Gaji']}, Tanggal Bergabung: {karyawan['Tanggal Bergabung']}")
        print("=============================")

# Untuk menambahkan data yang baru dibuat ke dalam database_karyawan
def addKaryawan(karyawan):
    database_karyawan.append(karyawan)
    print(f"Data untuk {karyawan['Nama']} berhasil ditambahkan")

# Untuk mengisi data karyawan baru
def addKaryawanMenu():
    while True:
        nama = baca_input("Masukkan Nama Karyawan: ")
        if not nama.isalpha():
            print("Nama karyawan hanya mengandung huruf.")
        else:
            break

    while True:
        id_karyawan = baca_input("Masukkan ID Karyawan: ")
        if not id_karyawan.startswith('MIB'):
            print('ID Karyawan harus dimulai dengan MIB')
        else:
            for karyawan in database_karyawan:   
                if karyawan['ID Karyawan'] == id_karyawan:
                    print('ID Karyawan tersebut sudah ada dan tidak bisa digunakan untuk karyawan baru.')
                    break
            else:
                break

    while True:
        from datetime import datetime
        import locale
        locale.setlocale(locale.LC_TIME, 'id_ID')
        tanggal_lahir = baca_input("Masukkan Tanggal Lahir Karyawan: ")
        if tanggal_lahir == '':
            print("Harap masukkan tanggal lahir")
        else:
            try: 
                datetime.strptime(tanggal_lahir.capitalize(), '%d %B %Y')
                break
            except ValueError:
                print("Harap Masukkan tanggal lahir berupa format 'tanggal, bulan, dan tahun'")

    while True:
        gender = baca_input("Masukkan Gender Karyawan: ")
        if gender.lower() != "male" and gender.lower() != "female":
            print("Gender tidak valid! Gender yang valid hanya Male atau Female.")
        else:
            break

    while True:
        jabatan = baca_input("Masukkan Jabatan Karyawan: ")
        if not jabatan.isalpha():
            print("Jabatan hanya mengandung huruf")
        else:
            break

    while True:
        nomor_hp = baca_input("Masukkan Nomor HP Karyawan: ")
        if not nomor_hp.isdigit():
            print("Harap masukkan angka untuk nomor hp")
        else:
            break
        
    while True: 
        gaji = baca_input("Masukkan Gaji Karyawan: ")
        if not gaji.isdigit():
            print("Harap masukkan angka untuk gaji")
        else:
            break

    while True:
        tanggal_bergabung = baca_input("Masukkan Tanggal Bergabung Karyawan: ")
        if tanggal_bergabung == '':
            print("Harap Masukkan tanggal bergabung")
        else:
            try: 
                datetime.strptime(tanggal_bergabung, '%d %B %Y')
                break
            except ValueError:
                print("Harap Masukkan tanggal lahir berupa format 'tanggal, bulan, dan tahun'")

    return {
        'Nama': nama,
        'ID Karyawan': id_karyawan,
        'Tanggal Lahir': tanggal_lahir,
        'Gender': gender,
        'Jabatan': jabatan,
        'Gaji': gaji,
        'Nomor HP': nomor_hp,
        'Tanggal Bergabung': tanggal_bergabung,
    }

def updateDataKaryawan(id_karyawan):
    index = 0
    for karyawan in database_karyawan:
        if id_karyawan.upper() == karyawan['ID Karyawan']:
            print(f"==========({karyawan['ID Karyawan']})==========")
            for menu in menus:
                print(f"{menu}: {karyawan[menu]}")
            print('================================================')
            print("Data Karyawan apa yang ingin Anda ubah?:")
            print("1. Nama")
            print("2. Tanggal Lahir")
            print("3. Gender")
            print("4. Jabatan")
            print("5. Nomor HP")
            print("6. Gaji")
            print("7. Tanggal Bergabung")
            print()
            print("8. Back to Update Menu")
            input_menu = int(input("Masukkan nomor menu: "))
            if input_menu == 1:
                while True:
                    input_data = baca_input("Masukkan data baru untuk Nama: ")
                    if not input_data.isalpha():
                        print("Nama hanya boleh mengandung huruf.")
                    else:
                        karyawan['Nama'] = input_data
                        database_karyawan[index] = karyawan
                        print(f"Data karyawan untuk ID {id_karyawan} berhasil diubah. {menus[input_menu-1]} telah diupdate menjadi {input_data}")
                        break
            elif input_menu == 2:
                from datetime import datetime
                import locale
                locale.setlocale(locale.LC_TIME, 'id_ID')
                while True:
                    input_data = baca_input("Masukkan Tanggal Lahir Karyawan: ")
                    if input_data == '':
                        print("Harap masukkan tanggal lahir")
                    else:
                        try: 
                            datetime.strptime(input_data.capitalize(), '%d %B %Y')
                            karyawan['Tanggal Lahir'] = input_data
                            database_karyawan[index] = karyawan
                            print(f"Data karyawan untuk ID {id_karyawan} berhasil diubah. {menus[input_menu-1]} telah diupdate menjadi {input_data}")
                            break
                        except ValueError:
                            print("Harap Masukkan tanggal lahir berupa format 'tanggal, bulan, dan tahun'")
            elif input_menu == 3:
                while True:
                    input_data = baca_input("Masukkan Gender Karyawan: ")
                    if input_data.lower() != "male" and input_data.lower() != "female":
                        print("Gender tidak valid! Gender yang valid hanya Male atau Female.")
                    else:
                        karyawan['Gender'] = input_data
                        database_karyawan[index] = karyawan
                        print(f"Data karyawan untuk ID {id_karyawan} berhasil diubah. {menus[input_menu-1]} telah diupdate menjadi {input_data}")
                        break
            elif input_menu == 4:
                while True:
                    input_data = baca_input("Masukkan Jabatan Karyawan: ")
                    if not input_data.isalpha():
                        print("Jabatan hanya mengandung huruf")
                    else:
                        karyawan['Jabatan'] = input_data
                        database_karyawan[index] = karyawan
                        print(f"Data karyawan untuk ID {id_karyawan} berhasil diubah. {menus[input_menu-1]} telah diupdate menjadi {input_data}")
                        break
            elif input_menu == 5:
                while True:
                    input_data = baca_input("Masukkan Nomor HP Karyawan: ")
                    if not input_data.isdigit():
                        print("Harap masukkan angka untuk nomor hp")
                    else:
                        karyawan['Nomor HP'] = input_data
                        database_karyawan[index] = karyawan
                        print(f"Data karyawan untuk ID {id_karyawan} berhasil diubah. {menus[input_menu-1]} telah diupdate menjadi {input_data}")
                        break
            elif input_menu == 6:
                while True:
                    input_data = baca_input("Masukkan Gaji Karyawan: ")
                    if not input_data.isdigit():
                        print("Harap masukkan angka untuk gaji")
                    else:
                        karyawan['Gaji'] = input_data
                        database_karyawan[index] = karyawan
                        print(f"Data karyawan untuk ID {id_karyawan} berhasil diubah. {menus[input_menu-1]} telah diupdate menjadi {input_data}")
                        break
            elif input_menu == 7: 
                from datetime import datetime
                import locale
                locale.setlocale(locale.LC_TIME, 'id_ID')
                while True:
                    input_data = baca_input("Masukkan Tanggal Bergabung Karyawan: ")
                    if input_data == '':
                        print("Harap Masukkan tanggal bergabung")
                    else:
                        try: 
                            datetime.strptime(input_data, '%d %B %Y')
                            karyawan['Tanggal Bergabung'] = input_data
                            database_karyawan[index] = karyawan
                            print(f"Data karyawan untuk ID {id_karyawan} berhasil diubah. {menus[input_menu-1]} telah diupdate menjadi {input_data}")
                            break
                        except ValueError:
                            print("Harap Masukkan tanggal lahir berupa format 'tanggal, bulan, dan tahun'")   
            # if input_menu < 7 and input_menu >= 0:
            #     input_data = input(f"Masukkan data baru untuk {menus[input_menu]}: ")
            #     karyawan[menus[input_menu]] = input_data
            #     database_karyawan[index] = karyawan
            #     print(f"Data karyawan untuk ID {id_karyawan} berhasil diubah. {menus[input_menu]} telah diupdate menjadi {input_data}")
            elif input_menu == 8:
                update()
            else:
                print('Menu tidak tersedia.')
            return
        index += 1
    print('ID Karyawan tersebut tidak ditemukan.')

def deleteKaryawan(id_karyawan):
    index = 0
    for karyawan in database_karyawan:
        if id_karyawan.upper() == karyawan['ID Karyawan']:
            konfirmasi = input(f"Apakah benar {karyawan['Nama']} mau dihapus? Pilih y untuk hapus atau n untuk batalkan. (y/n): ")
            if konfirmasi.lower() == 'y':
                database_karyawan.pop(index)
                print(f"Data karyawan untuk {karyawan['Nama']} berhasil dihapus")
            return
        index += 1
    print('ID Karyawan tersebut tidak ditemukan.')

printMenu()