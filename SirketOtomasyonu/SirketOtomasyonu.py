# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# İliskisel veritabanı kullanmadan txt (metin belgelerini)kullanıyoruz.
# .py dosyasını olusturduktan sonra calısanlar.txt, butce.txt dosyaları açıyoruz.
# butce.txt dosyasına toplam bütce yazılmalıdır. Şirket başlangıcta bütceyi belirlemeli.
class Sirket():

#__init__ fonksiyonu objemi türettigim anda çalısan fonksiyon  
    def __init__(self,ad): #ad : parametre
        self.ad = ad #obje referansıma ad degişkenime eşitlerim
        self.calisma = True  #Sınırsız bir döngüye girmek istersek        
# Self sınıf icerisinde metotlara, parametrelere ulasmak icin sıklıkla kullanılır.        
    def program(self):
        secim = self.menuSecim()
# Burada if elif yapısını kullanmamıza gerek yok çünkü secenekler birbirinden bagımsızdır, o yüzden if kullanmamızda bir sakınca yok.       
        if secim == 1:
            self.calısanEkle()
        if secim == 2:
            self.calısanCıkar()
        if secim == 3:
            ay_yil_secim = input("Yıllık bazda görmek ister misiniz?(e/h)") #evet/hayır
            if ay_yil_secim == "e":
                self.verilecekMaasGoster(hesap="y") # hesap parametresine y degerini göndeririz.
            else:
                self.verilecekMaasGoster() # Baska bir deger için defaul olara bıraktık.
        if secim == 4:
            self.maaslariVer()
       
            
    
    def menuSecim(self):
        secim = int(input("****{} Yazılım gelistirmeye hos geldiniz ****\n\n1-Calısan Ekle\n2-Calısan Cıkar\n3-Veriler Maas Goster\n4-Maaslari Ver\n\nSeciminizi giriniz:" .format(self.ad)))
        while secim < 1 or secim > 4:
            secim = int(input("Lütfen 1 - 4 arasında belirtilen seceneklerden birini giriniz :"))
        return secim
    
    def calısanEkle(self):
        id = 1
        ad = input("Calısanın adını giriniz: ")
        soyad = input("Calısanın soyadını giriniz: ")
        yas = input("Calısanın yasını giriniz: ")
        cinsiyet = input("Calısanın cinsiyetini giriniz: ")
        maas = input("Calısanın maasını giriniz: ")
 
#open fonksiyonu dosya acmak ve dosyada işlemler yapmak için kullanılır.
        with open("calısanlar.txt","r") as dosya:
            calısanListesi = dosya.readlines()
        
        if len(calısanListesi) == 0:
            id = 1
        else:
# r dosya içerigini baştan itibaren okumak için, w yazdırmak için kullanılır.
            with open("calısanlar.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1
                #Buradaki -1 listenin sonunu, sıfırde 0. indexden basladıgını belirtir.
                # Ekledigim her deger +1 sonraki sıarasına eklenecek.
# a+ dosyaların sonunda degişiklik yapmak için kullanılır.         
        with open("calısanlar.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n" .format(id,ad,soyad,yas,cinsiyet,maas))
            
    
    def calısanCıkar(self):
        with open("calısanlar.txt","r") as dosya:
            calısanlar = dosya.readlines()
## g gösterime girecek calısanlar anlamında       
        gCalısanlar = []
        for calısan in calısanlar:
            # stringi parcalıyoruz(calısanlar listemiz daha düzgün görünmesi için), split bölümlendirme fonksiyonu.
            gCalısanlar.append(" " .join(calısan[:-1].split("-"))) #Pythonda join() metodu string tipi elemanı dizinin elemanları ile birleştirir.
        for calısan in gCalısanlar:
            print(calısan)
# Bu metod, karakter dizilerini biçimlendirme işlemlerinde kullanılmaktadır.           
        secim = int(input("Lütfen cıkarnak istediginiz calısanın numarasını giriniz(1-{}:".format(len(gCalısanlar))))
        while secim < 1 or secim > len(gCalısanlar):
            secim = int(input("Lütfen (1-{}) arasında numara giriniz: ".format(len(gCalısanlar))))
        
        calısanlar.pop(secim - 1)
# Burada (-1) örn. 4 sayısını girdiginde 3. indeks anlamında.
        
        sayac = 1
        
        dCalısanlar = []    

        for calısan in calısanlar:
            dCalısanlar.append(str(sayac) + ")" + calısan.split(")")[1])
            sayac += 1
            
        with open("calısanlar.txt" , "w") as dosya:
            dosya.writelines(dCalısanlar)
            
    
    def verilecekMaasGoster(self,hesap = "a"):
      # hesap: a ise aylık, y ise yillik
        with open ("calısanlar.txt","r") as dosya:
            calısanlar = dosya.readlines()
            
        maaslar = []
        
        for calısan in calısanlar:
     # Buradaki -1 , calısanlar listesindeki elemanın bilgilerini split yaptıgımızda en son deger maas degeridir. Son degeri -1 seklinde gösteriririz.
            maaslar.append(int(calısan.split("-")[-1]))
        if hesap == "a": #default durumunda aylık maası bize gösterir.
        
            print("Bu ay toplam vermeniz gereken maas: {}" .format(sum(maaslar)))
        else:
            print("Bu yıl toplam vermeniz gereken maas: {}" .format(sum(maaslar)*12))

            
            
    def maaslariVer(self):
        with open ("calısanlar.txt","r") as dosya:
            calısanlar = dosya.readlines()
            
        maaslar = []
        
        for calısan in calısanlar:
            maaslar.append(int(calısan.split("-")[-1]))
            
        toplamMaas = sum(maaslar)
        
## Bütceden maasi alma
        with open("butce.txt","r") as dosya:
            tbutce = int(dosya.readlines()[0])
            
        tbutce = tbutce - toplamMaas
        
        with open("butce.txt","w") as dosya:
            
            dosya.write(str(tbutce))      


sirket = Sirket("Zeynep Soft!!")

while sirket.calisma:
    sirket.program()
