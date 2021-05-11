users = {"1234":{"name": "Jack" , "password":"e456", "balance":"3400"}, #Mini Database (Dictionary)
         "1347":{"name":"Gerrald", "password":"r321", "balance":"6700"}}
print("Gelecek Bankasına Hoşgeldiniz!")

cusNo= input("Hesap Numaranızı Giriniz: ")
cusPw= input("Şifrenizi Giriniz: ")

if  cusNo not in users: # Database'de Böyle Bir Kullanıcı Kayıtlı mı Diye Kontrol Edilir!
    print("Kullanıcı Bulunamadı! Tekrar Deneyin!")
else:
    if cusPw == users[cusNo]["password"]:
        print("Giriş Başarılı, Hoşgeldiniz")
        opt= input("Lütfen İşlem Seçiniz: 1-Para Çek, 2-Para Yatır , 3-Para Gönder :       ")

        if int(opt) == 1:      #Para Çekme İşlemleri
            value1= input("Miktar Giriniz: ")
            value1=int(value1)
            users[cusNo]["balance"]= int(users[cusNo]["balance"])
            users[cusNo]["balance"]  = users[cusNo]["balance"] - value1
            print("Hesapta Kalan Miktar(TL):")
            print(users[cusNo]["balance"])
        elif int(opt) == 2 :   #Para Yatırma İşlemler
            value2 = input("Miktar Giriniz: ")
            value2 = int(value2)
            users[cusNo]["balance"] = int(users[cusNo]["balance"])
            users[cusNo]["balance"] = users[cusNo]["balance"] + value2
            print("Hesaptaki Para Miktar(TL):")
            print(users[cusNo]["balance"])
        elif int(opt) == 3: #Para Gönderme İşlemleri
            value3 = input("Göndermek İstediğiniz Miktarı Girin: ")
            if value3 > users[cusNo]["balance"]:
                print("Bakiyeniz Yetersiz!")#Gönderilmek İstenen Miktar Balance Değerinden Fazla İse Kullanıcıyı Uyar.
            else:
                sendNo = input("IBAN Numarası Giriniz: ")
                if sendNo in users:
                    value3 = int(value3)
                    users[cusNo]["balance"]=int(users[cusNo]["balance"])
                    users[sendNo]["balance"]=int(users[sendNo]["balance"])
                    users[cusNo]["balance"] = users[cusNo]["balance"] - value3
                    users[sendNo]["balance"] = users[sendNo]["balance"] + value3
                    print("Hesabınızda Kalan Miktar(TL):")
                    print(users[cusNo]["balance"])
                    print("Gönderilen Hesabın :")
                    print("İsim :")
                    print(users[sendNo]["name"])
                    print("Gönderdğiniz Miktar: ", value3)
                    print("Gönderilen Hesaptaki Toplam Para: ")
                    print(users[sendNo]["balance"])
                else:
                    print("Geçersiz IBAN no'su!")








    else:
        print("Giriş Başarısız!")