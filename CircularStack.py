import random

class CircularStack:

    """
    Constructor of CircularStack
    @attribute ukuran, ukuran dari sebuah stack
    @attribute koleski, kumpulan koleksi atau data dari sebuah stack
    @attribute depan, referensi ke data yang paling awal
    @attribute belakang, referensi ke data yang paling akhir
    @attribute counter, variable penghitung untuk penanda
    @attribute pilihan, nilai pilihan dari sebuah random
    """
    def __init__(self, ukuran: int)->None:
        self.ukuran = ukuran
        self.koleksi = [None] * ukuran
        self.depan = random.randint(1, ukuran) - 1
        self.belakang = self.depan
        self.counter = 0
        self.pilihan = self.depan + 1

    """
    @method tambah, untuk menambagkan data
    @:param data, data yang ingin ditambahkan
    """
    def tambah(self, data)->None:
        if self.counter == self.ukuran:
            print('[INFO]: Stack Full')
        else:
            if self.belakang < self.ukuran:
                self.koleksi[self.belakang] = data
                self.counter += 1
                self.belakang += 1
            else:
                self.belakang = 0
                self.koleksi[self.belakang] = data
                self.counter += 1
                self.belakang += 1

    """
    @method kurang, untuk mengurangi data
    """
    def kurang(self)->None:
        if self.counter == 0:
            print('[INFO]: Stack Empty')
        else:
            if self.belakang == 0:
                self.belakang = self.ukuran
                self.koleksi[self.belakang - 1] = None
                self.counter -= 1
                self.belakang -= 1
            else:
                self.koleksi[self.belakang - 1] = None
                self.counter -= 1
                self.belakang -= 1

    """ 
    @method puncak, untuk melihat data yang paling akhir pada sebuah stack
    """
    def puncak(self)->None:
        if self.counter == 0:
            print('[INFO]: Stack Empty')
        else:
            print('[INFO] Puncak: ', self.koleksi[self.belakang - 1])

    """ 
    @method hapus_semua, untuk mengahapus semua data dan kembali seperti semula
    """
    def hapus_semua(self)->None:
        if self.counter == 0:
            print('[INFO]: Stack Empty')
        else:
            for i in range(1, self.counter + 1):
                self.kurang()
            print('[INFO]: Clear Stack')

    """
    @method get_depan, getter method yang digunakan untuk mendapatkan nilai dari attribute depan
    """
    def get_depan(self)->int:
        return self.depan

    """
    @method get_belakang, getter method yang digunakan untuk mendapatkan nilai dari attribute belakang
    """
    def get_belakang(self)->int:
        return self.belakang
