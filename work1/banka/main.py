#Hesap sınıfı: Hesap sahibinin adı, hesap numarası, bakiye bilgilerini içermeli. 
# para_yatir(miktar), para_cek(miktar), bakiye_goster() metodları olmalı.
#Encapsulation uygulanmalı (__bakiye private olmalı).

class Hesap:

    def __init__(self, isim, hesap_no, bakiye):
        self.isim = isim
        self.hesap_no = hesap_no
        self.__bakiye = bakiye  #private
    
    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.__bakiye} TL")
        else:
            print("Geçersiz miktar!") #Kullanıcı pozitif bir miktar yatırırsa bakiye artırılır,eğer negatif bir değer girilirse hata mesajı verilir.

    def para_cek(self, miktar):
        if 0 < miktar <= self.__bakiye:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.__bakiye} TL")
        else:
            print("Yetersiz bakiye.") #Eğer kullanıcı sınırlar içinde para çekmek isterse işlem yapılır,çekilecek miktar bakiyeden büyükse veya negatifse, hata mesajı verilir.

    def bakiye_goster(self):
        print(f"Hesap Sahibi: {self.isim}, Bakiye: {self.__bakiye} TL") #Güncel bakiye ekrana yazdırılır.

class VadesizHesap(Hesap):

    def __init__(self, isim, hesap_no, bakiye):
        super().__init__(isim, hesap_no, bakiye)  # Miras alınan sınıfın constructor'ını çağırıyoruz

class VadeliHesap(Hesap):
    def __init__(self, isim, hesap_no, bakiye, faiz_orani):
        super().__init__(isim, hesap_no, bakiye)
        self.faiz_orani = faiz_orani #superinit → Hesap sınıfındaki isim, hesap_no ve bakiye değişkenlerini miras alır, faiz_orani değişkeni yeni bir özellik
    
    def faiz_hesapla(self):
        faiz_miktari = self._Hesap__bakiye * self.faiz_orani / 100
        print(f"Faiz getirisi: {faiz_miktari} TL") #private nedeniyle self.__bakiye değişkeni doğrudan kullanılamaz self._Hesap__bakiye ile üst sınıftaki private değişkene erişiyoruz.

    def para_cek(self, miktar):
        ceza_orani = 0.02  # %2 ceza, Polymorphism (Çok Biçimlilik) için para_cek() metodu VadeliHesap içinde özelleştirilmeli.
        ceza = miktar * ceza_orani
        toplam_cekim = miktar + ceza

        if 0 < toplam_cekim <= self._Hesap__bakiye:
            self._Hesap__bakiye -= toplam_cekim
            print(f"{miktar} TL çekildi, {ceza} TL ceza kesildi. Kalan bakiye: {self._Hesap__bakiye} TL")
        else:
            print("Yetersiz bakiye veya geçersiz miktar!") #Vadeli hesaplardan para çekildiğinde %2 ceza uygulanır, çekilmek istenen tutara %2 ceza eklenir, eğer yeterli bakiye varsa ceza ile birlikte para çekilir,bakiye yetersizse, hata mesajı verilir.


# Vadesiz hesap açalım
hesap1 = VadesizHesap("Ali", "12345", 5000)
hesap1.bakiye_goster()
hesap1.para_yatir(2000)
hesap1.para_cek(1500)
hesap1.bakiye_goster()

# Vadeli hesap açalım
vadeli_hesap = VadeliHesap("Mehmet", "67890", 10000, 5)
vadeli_hesap.bakiye_goster()
vadeli_hesap.faiz_hesapla()
vadeli_hesap.para_cek(2000)  # Ceza uygulanacak
vadeli_hesap.bakiye_goster()

