class Books:
    def __init__(self, bookName, writerName, numberPages, isbn):
        self.bookName = bookName
        self.writerName = writerName
        self.numberPages = numberPages
        self.isbn = isbn

    # kitap isimlerini yazdırmak için
    def __str__(self):
        return f"Kitap Adı: {self.bookName}, Yazar: {self.writerName}, Sayfa Sayısı: {self.numberPages}, ISBN: {self.isbn}"

