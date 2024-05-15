import numpy as np
import pandas as pd
import seaborn as sns
from abc import ABC , abstractclassmethod

class Genel():
    def __init__(self):
        self.FirstName = ''
        self.LastName = ''
        self.Adress = ''


#YONETIM DEPARTMANI
class Yonetim(Genel):
    def __init__(self):
        self.bolum = ''
        self.gorev = ''
        self.deneyim_yili = 0
        self.pozisyon = ''
        self.yonetim_deneyim_yili = 0
        self.yabanci_diller = []

Yonetim_liste = []        

Sirac = Yonetim()
Sirac.FirstName = 'Mahmut Sirac'
Sirac.LastName = 'Ozcelik'
Sirac.Adress = 'Suriye'
Sirac.gorev = 'Yazilimci'
Sirac.bolum = 'Yazilim Muhendisi'
Sirac.pozisyon = 'Ceo'
Sirac.deneyim_yili = 15
Sirac.yonetim_deneyim_yili = 12
Sirac.yabanci_diller.append('Rusca')
Sirac.yabanci_diller.append('Almanca')
Sirac.yabanci_diller.append('Fransizca')
Sirac.yabanci_diller.append('Isponyolca')
Yonetim_liste.append(Sirac)

Oguz = Yonetim()
Oguz.FirstName = 'Oguzhan'
Oguz.LastName = 'Gun'
Oguz.Adress = 'Istanbul'
Oguz.gorev = 'Veri Bilimci'
Oguz.pozisyon = 'Yapay Zeka Muduru'
Oguz.bolum = 'Bilgisayar Muhendisi'
Oguz.deneyim_yili = 15
Oguz.yonetim_deneyim_yili = 8
Oguz.yabanci_diller.append('Rusca')
Oguz.yabanci_diller.append('Almanca')
Oguz.yabanci_diller.append('Japonca')
Oguz.yabanci_diller.append('Korece')
Yonetim_liste.append(Oguz)

Sivri = Yonetim()
Sivri.FirstName = 'Ahmet Samet'
Sivri.LastName = 'Sivri'
Sivri.Adress = 'Basaksehir'
Sivri.gorev = 'Robot Mekanizmalari'
Sivri.pozisyon = 'Robot AR-GE Muduru'
Sivri.deneyim_yili = 15
Sivri.yonetim_deneyim_yili = 12
Sivri.yabanci_diller.append('Rusca')
Sivri.yabanci_diller.append('Almanca')
Sivri.yabanci_diller.append('Cince')
Sivri.yabanci_diller.append('Arapca')
Yonetim_liste.append(Sivri)

for i in Yonetim_liste:
    print('***Yonetim***')
    print("\n") 
    print('Adi:',i.FirstName)
    print("Soyadı:", i.LastName)
    print("Adresi:", i.Adress)
    print('Departmani:',i.pozisyon)
    print("Bölümü:", i.bolum)
    print("Deneyim Yılı:", i.deneyim_yili)
    print('Yonetim Deneyim Yılı', i.yonetim_deneyim_yili)
    print("Yabanci Diller:", ", ".join(i.yabanci_diller))
    print("Görevi:", i.gorev)     
    print("\n")        

#IT DEPARTMANI
class IT(Genel):
    def __init__(self):
        self.bolum = ''
        self.python = 'evet'
        self.deneyim_yili=0
        self.bildigi_diller=[]
        self.gorev = ''     
        
IT_liste = []
        


Sirac = IT()
Sirac.bildigi_diller
Sirac.bildigi_diller.append('Python')
Sirac.deneyim_yili = 15
Sirac.python = 'Ekspert'
Sirac.bolum = 'Yazilim Muhendisi'
Sirac.FirstName = 'Mahmut Sirac'
Sirac.LastName = 'Ozcelik'
Sirac.Adress = 'Suriye'
Sirac.gorev = 'Ceo , Yazilimci'
IT_liste.append(Sirac)


Oguz = IT()
Oguz.bildigi_diller.append('Python')
Oguz.deneyim_yili = 15
Oguz.python = 'Ekspert'
Oguz.bolum = 'Bilgisayar Muhendisi'
Oguz.FirstName = 'Oguzhan'
Oguz.LastName = 'Gun'
Oguz.Adress = 'Istanbul'
Oguz.gorev = 'Veri Bilimci'
IT_liste.append(Oguz)

Sivri = IT()
Sivri.bildigi_diller.append('Python')
Sivri.deneyim_yili = 15
Sivri.python = 'Ekspert'
Sivri.bolum = 'Mekatronik Muhendisligi'
Sivri.FirstName = 'Ahmet Samet'
Sivri.LastName = 'Sivri'
Sivri.Adress = 'Basaksehir'
Sivri.gorev =  'Robot Mekanizmalari'
IT_liste.append(Sivri)

for i in IT_liste:
    print('##IT##')
    print("\n") 
    print('Adi:',i.FirstName)
    print("Soyadı:", i.LastName)
    print("Adresi:", i.Adress)
    print("Bölümü:", i.bolum)
    print("Deneyim Yılı:", i.deneyim_yili)
    print("Bildiği Diller:", ", ".join(i.bildigi_diller))
    print("Görevi:", i.gorev)     
    print('Python Tecrubesi:', i.python)
    print("\n")
    
    
    
#PERSONEL DEPARTMANI 
class Personel(Genel):
    def __init__(self):
        self.Deneyim_yili = 0
        self.Gorev = ''
        self.Bolum = ''
        self.Calisma_Saati = 0

Personel_liste = []

Asci = Personel()
Asci.FirstName = 'Ayse'
Asci.LastName = 'Abla'
Asci.Adress = 'Hadimkoy'
Asci.Deneyim_yili = 24
Asci.Gorev = 'Asci'
Asci.Calisma_Saati = 6
Asci.Bolum = 'Gastronomi'
Personel_liste.append(Asci)

Temizlikci = Personel()
Temizlikci.FirstName = 'Fatma'
Temizlikci.LastName = 'Abla'
Temizlikci.Adress = 'Hadimkoy'
Temizlikci.Deneyim_yili = 9
Temizlikci.Gorev = 'Temizlikci'
Temizlikci.Calisma_Saati = 6
Temizlikci.Bolum = 'Temizlik'
Personel_liste.append(Temizlikci)  
      
for i in Personel_liste:
    print('~Personel~')
    print("\n") 
    print('Personel Listesi')
    print('Adi:',i.FirstName)
    print("Soyadı:", i.LastName)
    print("Adresi:", i.Adress)
    print("Bölümü:", i.Bolum)
    print("Deneyim Yılı:", i.Deneyim_yili)
    print("Görevi:", i.Gorev)     
    print("\n")
    
#Sirketin kilavuzu
sirket = pd.DataFrame({'Yonetim':{'Ceo':'Sirac',
                                  'YZ Muduru':'Oguz',
                                  'Ro Muduru':'Sivri'},
                      'IT Departmani':{'Yazilim':'Sirac',
                                    'Veri Bilimci':'Oguz',
                                    'Robot Mekanizmalari':'Sivri'},
                      'Personel':{'Asci':'Ayse',
                                  'Temizlikci':'Fatma'}})
sirket.fillna(0,inplace = True)
sirket

maaslar = np.array([100000,100000,100000,60000,60000,60000,25000,25000])
maaslar_re=maaslar.reshape(8,1)
maaslar_df = pd.DataFrame(maaslar_re,columns=['Maaslar'])
maaslar_df

sirket['Maaslar'] = maaslar_df['Maaslar'].values
print(sirket)





















