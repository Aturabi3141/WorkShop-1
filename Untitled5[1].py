#!/usr/bin/env python
# coding: utf-8

# In[18]:


from math import sqrt

x = 16

y = sqrt (x)
print(y)

a = int(input("Bir sayı giriniz: "))

b = sqrt(a)
print(b)


# In[25]:


from random import random


# In[26]:


print(print(4))


# In[29]:


import os
dir(os)


# In[32]:


def selamla():
    ders = input("Bir sayı giriniz: ")
    print("Merhaba Arkadaslar...")
    print("Nasılsınız?")
    
selamla()
type(selamla)


# In[35]:


def faktoriyel(sayi):
    faktoriyel = 1
    if (sayi == 1 or sayi == 0):
        print("Faktöriyel", faktoriyel)
    else:
        while (sayi >= 1 ):
            faktoriyel *= sayi
            sayi -=1
            print("Faktöriyel", faktoriyel)
faktoriyel(6)


# In[37]:


def uclecarp(a):
    print("1. FONKSİYON ÇALIŞTI")
    return a * 3
def ikiyletopla(a):
    print("2. Fonksiyon Çalıştı")
    return a + 2
def dordebol(a):
    print("3. Fonsiyon çalıştı")
    return a/4

print(dordebol(ikiyletopla(uclecarp(6))))


# In[39]:


def selamla(isim = "İsimsiz"):
    print("Selam", isim)
selamla("Ali")
selamla()


# In[40]:


def bilgilerigoster(ad = "Bilgi Yok", soyad = "Bilgi Yok", telefon = "Bilgi Yok"):
    print("Adınız, ",ad,"Soadınız, ",soyad, "Numaranız, ",telefon)
bilgilerigoster("Ayetullah","Turabi",5468464474)


# In[47]:


def toplama(*parametreler):
    toplam = 0
    for i in parametreler:
        toplam += i
    return toplam
toplama(1,2,3,4,5,6,7,8,9,10)


# In[46]:





# In[ ]:




