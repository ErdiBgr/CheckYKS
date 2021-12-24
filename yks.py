import datetime #Datime kütüphanesini projeye dahil ettik
from selenium import webdriver #Selenium kütüphanesinden webdriver modülünü projeye dahil ettik.

while True: #Bir döngü başlatıyoruz.
	an = datetime.datetime.now() #Şuan ki geçerli zaman bilgilerini aldık
	saat = str(an.hour) #saat değişkenine şuan ki saati atadık

	if saat != "0": #Eğer saat gece 12'yi göstermiyorsa;
		continue #Döngüye tekrar devam etmesini sağladık.
	else: #Eğer gece 12'yi gösteriyorsa;
		break #Döngünün içerisinden çıkıp aşağıdaki kodlara çalışmasını sağladık.

browser_path = "\chromedriver.exe" #Chrome sürücüsünün dosya yolunu browser_path değişkenine atadık.

browser = webdriver.Chrome(browser_path) #Burda browser değişkenine browser_path'de atadığımız dosya yolunu çalıştırmasını istedik.
browser.get("https://sonuc.osym.gov.tr/") #.get() fonksiyonu ile ÖSYM'nin sonuçları açıkladığı siteye yönlendirdik.

cmbSinavTipi = browser.find_element_by_xpath('//*[@id="cmbSinavTipi"]/option[17]') #Karşımıza çıkan Sınav Tipi açılır menüsünden YKS'yi bulmasını sağladık.
btnBul = browser.find_element_by_xpath('//*[@id="btnBul"]') #Daha sonra "BUL" butonunu yerini tespit etmesini sağladık

cmbSinavTipi.click() #Açılır menünden bulunan YKS'ye tıklanmasını sağladık.
btnBul.click() #Tespit edilen bul butonuna tıklanmasını sağladık.

if browser.title == "ÖSYM Sonuç Açıklama Sistemi": #Eğer sitenin başlığı "ÖSYM Sonuç Açıklama Sistemi" ise;
	link = browser.find_element_by_link_text('2019 YKS Sonuçları') #"2019 YKS Sonuçları" yazan linki bulmasını istedik.
	link.click()#Ve ona tıklanmasını sağladık.

	tc = browser.find_element_by_id('tc') #Karşımıza çıkan formdaki "TC NO" metin kutusunun yerini tespit ettik.
	sifre = browser.find_element_by_id('sifre')#Karşımıza çıkan formdaki "Şifre" metin kutusunu yerini tespit ettik.
	btng = browser.find_element_by_id('btng')#Karşımıza çıkan formdaki "Gönder" butonunun yerini tespit ettik.

	tc.send_keys('TC KİMLİK NO')#Tespit ettiğimiz "TC NO" metin kutusuna değer gönderdik.
	sifre.send_keys('ÖSYM PAROLA*')#Tespit ettiğimiz "Şifre" metin kutusuna değer gönderdik.
	btng.click()#Tespit ettiğimiz "Gönder" butonuna tıklanmasını sağladık.
