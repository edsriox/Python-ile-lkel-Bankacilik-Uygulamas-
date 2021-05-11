users = {"1234":{"name": "Jack" , "password":"e456", "balance":"3400"},
         "1347":{"name":"Gerrald", "password":"r321", "balance":"6700"}}
print("Gelecek Bankasına Hoşgeldiniz!")

cusNo= input("Hesap Numaranızı Giriniz: ")
cusPw= input("Şifrenizi Giriniz: ")

if  cusNo not in users:
    print("Kullanıcı Bulunamadı! Tekrar Deneyin!")
else:
    if cusPw == users[cusNo]["password"]:
        print("Giriş Başarılı, Hoşgeldiniz")
        opt= input("Lütfen İşlem Seçiniz: 1-Para Çek, 2-Para Yatır:       ")

        if int(opt) == 1:
            value1= input("Miktar Giriniz: ")
            value1=int(value1)
            users[cusNo]["balance"]= int(users[cusNo]["balance"])
            users[cusNo]["balance"]  = users[cusNo]["balance"] - value1
            print("Hesapta Kalan Miktar(TL):")
            print(users[cusNo]["balance"])
        elif int(opt) == 2 :
            value2 = input("Miktar Giriniz: ")
            value2 = int(value2)
            users[cusNo]["balance"] = int(users[cusNo]["balance"])
            users[cusNo]["balance"] = users[cusNo]["balance"] + value2
            print("Hesaptaki Para Miktar(TL):")
            print(users[cusNo]["balance"])








    else:
        print("Giriş Başarısız!")