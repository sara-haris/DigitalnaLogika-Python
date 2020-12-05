""" print("Hello World")
print("Hello")
ime=input("Unesite vase ime: " )
print("Zdravo",ime)
ime2=(print(2>1))
broj1=15
broj2=int(input("Unesite broj:"))
print("Zbir je: ", broj1+broj2) """


""" 
print("Hello World") #Drugi komentar hahhaahhha
pozdrav="Hello World"
print(pozdrav)
print(type(pozdrav))
ime=input("Unesite vase ime: ")
print ('Zdravo',ime)
broj=int(input('Unesite neki broj:'))
print('Unijeli ste broj',broj)
broj2=5
print(bin(broj2)) """

#Zadatak 1
""" godine=int(input("MOlim vas unesite vase godine:"))
mjeseci=godine*12
print('Vase godine su jednake',mjeseci,"mjeseci") """
#Zadatak 2
""" kilometri=int(input('Molim vas unesite kilometre: '))
metara=kilometri*1000
print('Uneseni kilometri iznose:',metara,'metara') """
#Zadatak 3
""" broj=int(input('Unesite broj: '))
kvadrat=broj*broj
print('Broj kvadriran iznosi: ',kvadrat) """
#Zadatak 4
""" broj1=int(input('Unesite broj: '))
broj2=int(input('Unesite drugi broj: '))
sabiranje=broj1+broj2
oduzimanje=broj1-broj2
mnozenje=broj1*broj2
dijeljenje=broj1/broj2
print('Vasa dva broja sabrana iznose: ',sabiranje)
print('Vasa dva broj oduzeta iznose: ',oduzimanje)
print('Vasa dva broja pomnozena iznose: ',mnozenje)
print("Vasa dva broja podijlenjena iznose: ",dijeljenje)
 """
 #Zadatak 5
""" broj=124
print("Broj u heksa. iznosi: ",hex(broj))
print("Broj u okta. iznosi: ",oct(broj))
print("Broj u bina. iznosi: ",bin(broj)) """
#Zadatak 6
""" cijenabezpdv=124
Pdv=0.17
pdv=cijenabezpdv*Pdv
sapdv=cijenabezpdv+pdv
print('Cijena sa PDV-om iznosi: ',sapdv)
ueurima=cijenabezpdv*2
print('Cijena u knjige u eurima iznosi: ',ueurima)
rate=cijenabezpdv*0.05
uratama=cijenabezpdv+rate
print('Cijena placanjem u ratama iznosi: ',uratama)
gotovina=cijenabezpdv*0.15
ugotovini=cijenabezpdv-gotovina
print('Cijena placena gotovinom iznosi: ',ugotovini)
 """
#Zadatak 7
""" tempC=int(input('Unesite temperaturu u Celzijusima: '))
tempF=tempC * 9/5.0 + 32
print("Temperatura u Fahrenheitima je: ",tempF) """

#NOVI SAT VJEZBI
""" a=3
b=3
if (a>b):#Pazi indentation!!! 
    print("Blueface baby")
elif (a==b): 
     print("Ne moze")  
else :
    print('Aight')    
 """
""" string="Jasamhhhhh Haris i imam 19 godina"
print('Prvo slovo je: ',string[0])
print('Duzina vase recenice je: ',len(string))
print('Prvih pet slova su: ',string[0:5])
print('Prvih pet slova sa razmakom od dva su: ',string[0:5:2])

if string.isalpha: 
    print("Vasa recenica je sva od slova!")
else: 
      print("Vasa recenica ima i brojeve/karaktere u sebi!")     """
################################# Neke vjezbe ########################################################
""" temperatura=float(input('Unesite temperaturu: '))
tempF=temperatura*9/5 +32
if temperatura<15:
    print("Hladno je vani,obucite se slojevito!")
    print("Unesena temperatura u Farenhajtima iznosi: ",tempF)
else:
    print("Vani je toplo!")
    print("Unesena temperatura u Farenhajtima iznosi: ",tempF)
 """
""" broj=int(input("Molim vas unesite jedan broj: "))
if broj==0:
    print("Broj je nula! ")
elif broj>0:
    print("Broj",broj,"je veci od nule")    
else:
     print("Broj",broj,"je manji od nule")   """
    
""" string="Danas je lijep dan"
if string.isalpha:
    print('Da')
else:
    print('Ne')
print("Indeks pojavljivanja danas je: ",string.index('Danas'))
print("Vasa recenica sa zamjenom prve rijeci glasi: ",string.replace('Danas','Sutra')) """

""" string="1234567"
print('Slova od ind 3 do 6 su: ',string[3:7])#Trazi  se indeks zato je do 7
 """
#Zadatak jedan:
""" broj=int(input("Molim vas unesite jedan broj: "))
if broj%2==0:
    print("Uneseni broj je paran!")
else:
    print("Uneseni broj je neparan!")     """
#Zadatak dva:
""" a=int(input("Molim vas unesite prvi broj: "))
b=int(input("Molim vas unesite drugi broj: "))
znak=input("Molim vas unesite +,-,* ili /, ovisno sta zelite da uradite sa brojevima: ")
if znak=='+':
    print("Zbir je: ",a+b)
elif znak=='-':
    print("Razlika je: ",a-b)
elif znak=='*':
    print("Proizvod je: ",a*b)
else:
    if b!=0:
      print("Kolicnik je: ",a/b)
    else:
        print("Ne moze se dijeliti sa nulom!")   """
#Zadatak tri:
""" cijenaArtikla=int(input("Molim vas unesite cijenu artikla: "))
kolicinaArtikla=int(input("Molim vas unesite kolicinu artikla: "))
racun=cijenaArtikla*kolicinaArtikla
nacinPlacanja=input("Molim vas unesite nacin placanja (g za gotovinu/k za karticu: ")
if 'k' in nacinPlacanja:
    racun=racun+racun*0.15
    print("Obzirom da placate karticom iznos vam se uvecava za 15% te on sada iznosi: ",racun)
elif 'g'in nacinPlacanja:
    racun=racun-racun*0.5
    print("Obzirom da placate gotovinom iznos vam je umanjen za 5% te on sada iznosi: ",racun)
else:
    print("NISTE UNIJELI KOREKTAN KARAKTER ZA PLACANJE!!!") """
#Zadatak cetiri:
""" metara=int(input("Molim vas unesite broj metara stana: "))
kvadrat=metara*2
cijenaKvadrata=0
cijenaStana=0
PedesMkv=25*2
OsamMkv=40*2
if kvadrat<PedesMkv:
    cijenaKvadrata=2000
    cijenaStana=kvadrat*cijenaKvadrata
    print("Cijena stana unesenih velicina iznosi: ",cijenaStana)
elif kvadrat>=PedesMkv and kvadrat<=OsamMkv:
    cijenaKvadrata=1800
    cijenaStana=cijenaKvadrata*kvadrat
    print("Cijena stana unesenih velicina iznosi: ",cijenaStana)
else:
    cijenaKvadrata=1500
    cijenaStana=cijenaKvadrata*kvadrat
    print("Cijena stana unesenih velicina iznosi: ",cijenaStana)
 """

############################# NOVA NASTAVA ###########################################################
""" string="Ababababababababa"
print('indeksi od tri do sest su:', string[3:7])#Kljucna rijec INDEKSI
print("Prva tri karaktera su: ",string[0:3])#Kljucna rijec KARAKTERI
 """
 #Zadatak sa ulaznicama za kino:
""" godine=int(input("Molim vas unesite vase godine: "))
vrijeme=int(input("Molim vas unesite vrijeme: "))
cijena=10

if (godine<18 and vrijeme<12):
    cijena=cijena-cijena*0.3
    print('Vasa cijena je umanjena za 30 posto i iznosi: ', cijena,"KM")
elif(godine<18 and vrijeme>12):
    cijena=cijena-cijena*0.1
    print('Vasa cijena je umanjena za 10 posto i iznosi: ',cijena, "KM" )
elif (godine>65 and vrijeme<12):
     cijena=cijena-cijena*0.5
     print('Vasa cijena je umanjena za 50 posto i iznosi: ',cijena,"KM" )
elif (godine>65 and vrijeme>12):
     cijena=cijena-cijena*0.3
     print('Vasa cijena je umanjena za 30 posto i iznosi: ',cijena,"KM" )
else:
    print("Cijena za vas je regularna i iznosi: ",cijena,'KM')  """
###########################################################################################################

 #Zadatak sa unosom A,B,c i D i program treba da kaze za koje kombinacije ce biti 0 ili 1 na izlazu\
 #ako je  uslov da je 1 samo ako su dva,tri ili cetiri ulaza 1!
A=int(input("Molim vas unesite ulaz A:"))
B=int(input("Molim vas unesite ulaz B: "))
C=int(input("Molim vas unesite ulaz C: "))
D=int(input("Molim vas unesite ulaz D: "))
F=0

if(A==0 and B==0 and C==0 and D==0) or (A==0 and B==0 and C==0 and D==1) or (A==0 and B==0 and C==1 and D==0) or (A==0 and B==1 and C==0 and D==0) or (A==1 and B==0 and C==0 and D==0):
      print("Vrijednost na izlazu je: ",F)
else:
    F=1
    print("Vrijednost na izlazu je: ",F)

#############################################################################################################


