print("Tere maailm")
#1
#nimi=input("Mis on sinu nimi?") #comment
#vanus=int(input("kui vana sa oled?")) #float()->2.5
#print("Tere tulemast!" +nimi+". Sa oled"+str(vanus)+" aastat vana")
#print("Tere tulemast!" ,nimi,". Sa oled",vanus,"aastat vana")
#print("Tere tulemast! {0} Sa oled {1} aastat vana".format(nimi, vanus))
#print("muutuja vanus=",vanus,",tüüp on",type(vanus))
#2
#vanus = 18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_käib_koolis = True
#print("muutuja vanus=",vanus,",tüüp on",type(vanus))
#print("muutuja vanus=",eesnimi,",tüüp on",type(eesnimi))
#print("muutuja vanus=",pikkus,",tüüp on",type(pikkus))
#print("muutuja vanus=",kas_käib_koolis,",tüüp on",type(kas_käib_koolis))

#3
from random import *
kokku=randint(10,100)
print("kokku",kokku)
mitu=int(input("Mitu kommi tahad võtta?"))
kokku-=mitu
print("Nüüd laua peal on",kokku,"kommi")