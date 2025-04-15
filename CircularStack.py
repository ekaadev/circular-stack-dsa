class CircularStack:
    def __init__(self, ukuran: int, mulai: int)->None:
        self.ukuran = ukuran
        self.koleksi = [None] * ukuran
        self.depan = mulai - 1
        self.belakang = self.depan
        self.counter = 0

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

    def puncak(self)->None:
        if self.counter == 0:
            print('[INFO]: Stack Empty')
        else:
            print('[INFO] Puncak: ', self.koleksi[self.belakang - 1])

    def hapus_semua(self)->None:
        if self.counter == 0:
            print('[INFO]: Stack Empty')
        else:
            for i in range(1, self.counter + 1):
                self.kurang()
            print('[INFO]: Clear Stack')

    def get_depan(self)->int:
        return self.depan

    def get_belakang(self)->int:
        return self.belakang
