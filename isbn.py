# https://dodona.be/nl/courses/4195/series/46782/activities/182880102



t = 0
getalreeks = 0
controle = 0

while t < 10:
    invoer = int(input("Geef een getal tussen 0 en 9: ")) 

    if invoer > 9 or invoer < 0:
        print('Foute invoer')
        break
    t += 1

    if t == 10:
        controle = invoer 

    else:
        getalreeks += invoer * t  

if t == 10:  
    if getalreeks % 11 == controle:
        print('OK')
    else:
        print("FOUT")
