from CircularStack import CircularStack

def info_circular_stack(circular: CircularStack)->None:
    print(f'[INFO] Ukuran: {circular.ukuran}')
    print(f'[INFO] Index Depan: {circular.get_depan()}')
    print(f'[INFO] Index Belakang: {circular.get_belakang()}')
    print(f'[INFO] Counter: {circular.counter}')
    print(f'[INFO]: {circular.koleksi}')

def info_menu()->None:
    print(f'[INFO]: 1. Tambah data')
    print(f'[INFO]: 2. Kurang data')
    print(f'[INFO]: 3. Lihat puncak')
    print(f'[INFO]: 4. Bersihkan data')
    print(f'[INFO]: 5. Exit')

def main():
    ukuran_koleksi = 0
    # Disable input user for initialize front
    # mulai = 0
    menu = 0

    while True:
        try:
            ukuran_koleksi = int(input(f'[INPUT]: Masukan ukuran koleksi: '))
            if ukuran_koleksi.is_integer() is True:
                break
        except ValueError:
            print(f'[ERROR]: Input salah')

    # Disable input user for initialize front
    # while True:
    #     try:
    #         while True:
    #             mulai = int(input(f'[INPUT]: Masukan insialiasi mulai: '))
    #             if mulai <= ukuran_koleksi:
    #                 break
    #
    #         if mulai.is_integer() is True:
    #             break
    #     except ValueError:
    #         print(f'[ERROR]: Input salah')

    cs: CircularStack = CircularStack(ukuran_koleksi)

    while True:
        print(f'=======================')
        info_circular_stack(cs)
        print(f'=======================')

        info_menu()

        menu = input(f'[INPUT]: Masukan pilihan menu: ')

        match menu:
            case '1':
                data = input(f'[INPUT]: Masukan data: ')
                cs.tambah(data)
            case '2':
                cs.kurang()
            case '3':
                cs.puncak()
            case '4':
                cs.hapus_semua()
            case '5':
                break

if __name__ == '__main__':
    main()