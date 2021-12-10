class yemektarifuygulama :
    def tarifEKLE(self) :
        tarifIsmi = input("Tarıf ismi : ")
        tarif.append(tarifIsmi)
        while True :
            tarifSayisi = input('Tarif Ekle(Tarifiniz Sonlandıysa "-1" giriniz.) : ')
            if tarifSayisi == "-1" :
                tarifler_listesi.append(tarif)
                tarif.append("\n")
                break
            else :
                tarif.append(tarifSayisi)


    def goster(self) :
        number = len(tarifler_listesi)
        print("Tüm Tarifler")
        for adim in tarif :
                print(adim)




def main_menu() :
    while True :
        print("\nYeni Tarif Ekle : 1\nTarifleri Goster : 2\nSonlandır : 3 ")
        secim = input("Yapmak İstediğiniz İşlem Rakamını Giriniz : ")
        islem = yemektarifuygulama()
        if secim == "1" :
            islem.tarifEKLE()
        elif secim == "2" :
            islem.goster()
        elif secim == "3" :
            exit(0)
        else :
            print("Hatalı Tuşlama1")



tarifler_listesi = []
tarif = []

main_menu()