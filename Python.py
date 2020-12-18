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
""" A=int(input("Molim vas unesite ulaz A:"))
B=int(input("Molim vas unesite ulaz B: "))
C=int(input("Molim vas unesite ulaz C: "))
D=int(input("Molim vas unesite ulaz D: "))
F=0

if(A==0 and B==0 and C==0 and D==0) or (A==0 and B==0 and C==0 and D==1) or (A==0 and B==0 and C==1 and D==0) or (A==0 and B==1 and C==0 and D==0) or (A==1 and B==0 and C==0 and D==0):
      print("Vrijednost na izlazu je: ",F)
else:
    F=1
    print("Vrijednost na izlazu je: ",F) """

#############################################################################################################

################################ NOVA NASTAVA################################################################
""" broj=0
while broj<10:
    broj+=1
    print(broj,end=',')# end='' sa time odvajas  vodoravno
 """
 ##################################################################
""" broj=0
while broj!=5:
    broj=int(input("Unesite neki broj: "))
    if broj==5:
        print("Svaka cast pogodili ste ")
    else:
        print("Pokusajte ponovo!")  """   
####################################################################
""" n=int(input('Unesite broj: '))
suma=0
brojac=0
while brojac<=n:
    suma+=brojac
    brojac+=1
print("Suma je : ",suma) """
####################################################################
""" suma=0
brojac=1
x=10
while brojac<=x:
    suma+=brojac
    brojac+=1
    if brojac==7:
        break
    
print("Suma  od 0 do 7 je: ",suma) """

###################################################
""" for i in range (1,11):
    if(i%2==0):
     print (i)
 """
######################################
""" for i in "Fakultet informacijskih tehnologija":
    print(i)
 """
 #######################Zadaci#############################
""" broj=0
while broj<7:
    broj+=1
    print(broj,end=';')
 """
 ######################################
""" broj=int(input("MOlim vas unesite broj: "))
while  ((broj>=1 or broj<=10) and broj!=5): #Stavljas za uslov rang brojeva od 1 do 10 i da je razlicit od 5
    print("Broj nije pogodjen, ponovo !")
    broj=int(input("MOlim vas unesite broj: "))
    
print("Bravo pogodili ste broj!")
 """
 ##################################################

""" brojac=1
suma=0
n=int(input('Unesi broj '))
while brojac<=n: # Mora biti <= uneseni broj jer treba i njega zbrojiti
    suma=suma+brojac
    brojac+=1
print('Suma brojeva do unesenog broja je: ',suma) """
#######################################################
""" string="Hello World"
brojac=1
while brojac<=5:
    print(string)
    brojac+=1
 """
 ##################################
""" n=int(input("unesi broj:" ))
brojac=1
while brojac<=n:
    print(brojac*brojac)
    brojac+=1
     """
###################################
""" granica=10
brojac=1
suma=0
while brojac<=granica:
    if(brojac%2==0):
        suma+=brojac
    brojac+=1#brojac moras incrementirat u while indentationu!   
print("Suma svih parnih brojeva je: ",suma)
 """
""" broj=11
brojac=1
while brojac<=10:
    broj-=1# Broj je u pocetku 11 jer ga ovdje smanji odmah a prije ga nije ispisao
    print(broj)
    brojac+=1 """
####################################################
""" granica=10
suma=0
brojac=1
while brojac<=granica:
    suma+=brojac
    brojac+=1
    if(brojac==7):#Suma ne uzme onaj element kojem je brojac jednak!
        suma+=brojac#Ako zelim da ubrojim i 7!
        break
print("Suma je: ",suma) """
###################################################
""" for i in range(1,11):
    print(i,end=',') """
###################################################
""" for i in range (1,11):
    if i%2!=0:
        print(i)
    if i==7:
        break """
###################################################
""" for i in range(1,11):
    if i!=7:
        print(i) """
###################################################
""" for i in range(1,6):
    print("FIT")
    
 """
####################################################
""" x=int(input("Molim vas unesite koliko puta zelite da se ispise FIT": ))
for i in range (x):#Pocetni ili start parametar se ommita!
    print("FIT")

     """
######################################################
""" string="Ja sam Haris i imam 19 godina"
for i in string:
    print (i) """

#######################################################
""" string="FIT"
for i in string:
    if i=='T':
        break
    print(i)    """
#######################################################
""" suma=0
for i in range(5,-1,-1): #Posto se unazad treba brojac kretati  stepen pomaka moramo staviti na -1
    suma+=i
print("Suma brojeva je: ",suma)
 """

#############################################################
""" suma=0
for i in range (1,11):
    if i%2!=0:
        suma+=i
print(suma)   

suma=0
for i in range (1,6):
    if i%2!=0:
        suma+=i
print(suma)     """    
########################################################
""" for i in range(1,11):
    if(i%2==0):
        print("Parni br su: ",i,end='; ')
    print("Kvadrati su: ",i**2,end='; ')
    if(i%5==0):
        print("Brojevi djeljivi sa 5 su:",i,end='; ') """
###############################################################
""" string=input("Molim vas unesite receniu koju zelite da ispisete: ")
broj=int(input("MOlim vas unesite koliko  broj ponavljanja: " ))
for i in range(broj):
    print(string) """
###############################################################
""" x=int(input("Molim vas unesite broj starta: "))
y=int(input("Molim vas unesite broj gornje granice: "))
for  i in range(x,y):
      print(i*y) """
###############################################################
""" x=int(input("Unesite broj redova: "))
y=int(input("Unesite broj kolona: "))
znak=input("Unesite znak kojim zelite ispuniti crtez: ")

for i in range(x):
    for j in range(y):
        print(znak,end=' ')
    print() """

################################################################
""" string="FIT"
for i in range(5):
    print("* ",end=" ")
    for j in string:
        print(j)
    print("* ") """
###########################################NOVA NASTAVA###################################
""" ime=input("Unesite ime molim vas: ")
def pozdrav (ime):
    print ('Dobro jutro',ime)
pozdrav(ime) """
#################################################
""" broj=int(input("Molim vas unesite broj: "))
def parnost(broj):
    if(broj%2==0):
        print("Broj je paran!")
    else:
      print("Broj nije paran")
parnost(broj) """
####################################################
""" a=int(input("Unesite prvi broj: "))
b=int(input("Unesite drugi  broj: ")) 
def mnozenje(a,b):
    print("Proizvod je: ",a*b)
for i in range(1,4):
    a=int(input("Unesite prvi broj: "))
    b=int(input("Unesite drugi  broj: "))
    mnozenje(a,b)  """
####################################################
""" def funkcija1():
    x=15
    print("Broj u fijije: ",x)
x=20
funkcija1()
print("Izvan fije je: ",x) """
#####################################################
""" def kvadrat(a):
    return a*a
print(kvadrat(5)) """
######################################################
""" a=int(input("Unesi br:"))
b=int(input("Unesi br:"))
c=int(input("Unesi br:"))
def artm(a,b,c):
    return (a+b+c)/3
print(artm(a,b,c)) """
###################################################
""" n=int(input("Unesite broj: "))
def zbir(n):
    zbir=0
    for i in range(1,n+1):
        #Ako ovdje deklar zbir on se stalno na nulu stavlja!!!
        zbir=zbir+i
    return zbir
print("Zbir je:",zbir(n)) """
#####################################################################
""" x=int(input("Molim vas unesite broj: "))
def pozorneg(x):
    if(x<0):
        print("Broj",x," je  negativan")
    elif (x==0):
        print("Broj",x," je nula (0)")
    else:
        print("Broj",x," je pozitivan")
pozorneg(x); """
##################################################################
""" def zbir():
    zbir=0#Ovdje deklar varijablu!!!
    for i in range(1,11):
        zbir+=i
    return zbir# returnas poslije fora UVIJEK!
print("Suma je:",zbir()) """
################################################################
""" for i in range(4):
    print("*"*5)#Printas za svaki red 5 zvjezdica """
################################################################
""" string="FIT"
n=int(input("Molim vas unesite broj redova: "))
for i in range (n):
    print("*"*5)
    for j in string:
        print(j,) """
######################################################################
""" for g in range(5):
    for h in range(4):
        print("*",end=" ")
    print() """
######################################################################
""" a=int(input("Molim vas unesite prvi broj: "))
b=int(input("Molim vas unesite drugi broj: "))
znak=input("MOlim vas unesite operaciju")
def kalkulator(a,b,znak):
    if znak=='+':
        return a+b
    elif znak=='-':
        return a-b
    elif znak=='*':
        return a*b
    elif znak=='/':
        if(b!=0):
            return a/b
        else:
            return print("Ne moze se dijeliti sa 0!")
    else:
        return print("Neispravan simbol operacije!!!")
print("Unijeli ste broj",a," i broj ",b," sa operacijom ",znak,"gdje je rezultat: ",kalkulator(a,b,znak)) """
##############################################################################################################
""" print("IGRAC 1")
a=int(input("Unesi broj za pogadjanje: "))
print("IGRAC 2")
b=int(input("Pokusaj pogoditi broj od IGRAC 1 "))

def igra(a,b):
    brojac=1
    while b!=a:
        print("Netacno,probaj opet")
        b=int(input("Pokusaj pogoditi broj od IGRAC 1 "))
        brojac+=1
    return print("Bravo pogodili ste broj od IGRAC 1, trebalo vam je ",brojac," pokusaja")
igra(a,b) """
#############################################################################################
""" cijenaArtikla=int(input("Molim vas unesite cijenu datog proizvoda: "))
kolicina=int(input("Molim vas unesite kolicinu artikala koje ste kupili: "))


def popust(cijenaArtikla,kolicina):
    racun=cijenaArtikla*kolicina
    znak=input("Unesite 'k' za placanje karticom ili 'g' za placanje gotovinom:")
    if znak=='k':
        racun=racun+racun*0.15
        return print("Na vas konacni iznos se dodaje 15% te vas racun iznosi:",racun)
    elif znak=='g':
        racun=racun-racun*0.5
        return print("Ostvarujete popust od 5%, a vas racun iznosi: ",racun)
    else:
        return print("Pogresan unos nacina placanja! Vas normalan racun je: ",racun)
popust(cijenaArtikla,kolicina) """

string="balaala"
for i in string:# Ako je "string" onda ce taj string gledati kao s t r i n g , a ako je string onda je b a l .... 
    print(i)



