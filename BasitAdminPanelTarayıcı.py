import requests

admin_panel_uzantıları=open("AdminPanelUzantıları.txt",mode="r").readlines()
site=input("Başında http:// ve Sonunda / Şeklinde Site Adresini Giriniz: ")

for i in admin_panel_uzantıları:
    req=requests.get(site+i.replace("\n",""))

    if req.status_code==200:
        print("Admin Panel Bulundu! ", req.url)
    else:
        print("Admin Panel Bulunamadı...", req.url)