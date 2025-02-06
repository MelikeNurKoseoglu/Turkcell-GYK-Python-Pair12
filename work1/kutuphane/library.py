from books import Books

class Library:
    def __init__(self):
        self.books = []  # kitapları tutmak için liste

    def kitap_ekle(self, book):
        if any(b.isbn == book.isbn for b in self.books):
            raise Exception(f"Hata: {book.isbn} ISBN numaralı kitap zaten kütüphanede mevcut!") # hata fırlatılır ve işlem iptal edilir.
        else:
            self.books.append(book)
            print(f"{book.bookName} kitabı kütüphaneye eklendi.")

    def kitap_sil(self, isbn):
        for kitap in self.books:
            if kitap.isbn == isbn:
                self.books.remove(kitap)
                print(f"{kitap.bookName} kitabı kütüphaneden silindi.")
                return
        raise Exception(f"Hata: {isbn} ISBN numaralı kitap kütüphanede bulunamadı!")

    def kitaplari_goster(self):
        if not self.books:
            print("Kütüphanede kitap bulunmamaktadır.")
        else:
            print("Kütüphanedeki Kitaplar:")
            for kitap in self.books:
                print(kitap)


library = Library()

print("****")
try:
    kitap1 = Books("Kitap1", "Yazar1", 200, "123456789")
    library.kitap_ekle(kitap1)
except Exception as e:
    print(f"Hata: {e}")

print("****")
try:
    kitap2 = Books("Kitap2", "Yazar2", 150, "987654321")
    library.kitap_ekle(kitap2)
except Exception as e:
    print(f"Hata: {e}")

print("****")
try:
    kitap3 = Books("Kitap1", "Yazar1", 200, "123456789")
    library.kitap_ekle(kitap3)  # Aynı ISBN olduğu için hata verecek
except Exception as e:
    print(f"Hata: {e}")

print("****")
library.kitaplari_goster()

print("****")
try:
    library.kitap_sil("123456789")
except Exception as e:
    print(f"Hata: {e}")

print("****")
try:
    library.kitap_sil("000000000")  # Bulunamayan kitap için hata verecek
except Exception as e:
    print(f"Hata: {e}")  # Hata olsa bile program devam edecek

print("****")
library.kitaplari_goster()

print("Program sonlandırıldı.")
