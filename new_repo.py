import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

selection = input("Ekrani temizlemek icin x tusunua basin :")
asil_selection = selection.lower()

if asil_selection == "x":
    print("Ekraniniz siliniyor" )
    time.sleep(2)
    cls()
else:
    print("Uygulamadan cikiliyor")
    time.sleep(1)
