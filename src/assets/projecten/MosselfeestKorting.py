#Inlezen van variabelen en constanten
MOSSELEN =20
KONHAP = 10
DRANK = 2
IJS = 3

#inlezen van waarden
Amos=int(input(  'Geef het aantal mosselen:  '))
Akh=int(input(   'Geef het aantal koninghap: '))
Adrank=int(input('Geef het aantal drank:     '))
Aijs=int(input(  'Geef het aantal ijsjes:    '))


#Totaal berekenen
Bmos = Amos*MOSSELEN
Bkh = Akh*KONHAP
Bdrank = Adrank * DRANK
Bijs = Aijs * IJS
tebetalen= Bmos+Bkh+Bdrank+Bijs



#Controle
if Amos >= 2:
  if tebetalen >= 150:
    kort150 = 20
    bedragP = tebetalen-kort150
    print('Totaal zonder korting',   tebetalen)
    print('Je korting', kort150)
    print('Totaal', bedragP)
  elif tebetalen >= 100:
    kort100 = 10
    bedragP = tebetalen-kort100
    print('Totaal zonder korting',   tebetalen)
    print('Je korting', kort100)
    print('Totaal', bedragP) 
  elif tebetalen >= 50:
    kort50 = 5
    bedragP = tebetalen-kort50
    print('Totaal zonder korting',   tebetalen)
    print('Je korting', kort50)
    print('Totaal', bedragP)
  else:
   kort0 = 0
   bedragP = tebetalen - kort0
   print('Totaal zonder korting',   tebetalen)
   print('Je korting', kort0)
   print('Totaal', bedragP)
else:
    bedragP = tebetalen
    print('Total',                  bedragP)
    
#Inlezen van waardes
print('Uw Totaal =', tebetalen,'$')
ontvangen=int(input('Geef het ontvangen bedrag terug:  '))
bedrag = ontvangen-tebetalen    

if (bedrag < 0):
    teweinigbetaald = tebetalen -ontvangen
    print('Uw heeft', teweinigbetaald ,' te weinig betaald: ')
    ontvangen=int(input('Geef het ontvangen bedrag terug:  '))
    bedrag = ontvangen-tebetalen

print(20*'*')
print('*'+18*' '+'*')
print(f'* {"tebetalen":12}{tebetalen:>4} *')
print(f'* {"ontvangen":12}{ontvangen:>4} *')
print(f'* {"Geef terug":12}{bedrag:>4} *')
print('*'+18*' '+'*')

aantal100 = bedrag // 100
rest = bedrag % 100
aantal50 = rest // 50
rest = rest % 50
aantal20 = rest // 20
rest = rest % 20
aantal10 = rest // 10
rest = rest % 10
aantal5 = rest // 5
rest = rest % 5
aantal2 = rest // 2
rest = rest % 2
aantal1 = rest // 1
rest = rest % 1

print(f'* {"100€":^7} -  {aantal100:^2}    *')
print(f'* {"50€":^7} -  {aantal50:^2}    *')
print(f'* {"20€":^7} -  {aantal20:^2}    *')
print(f'* {"10€":^7} -  {aantal10:^2}    *')
print(f'* {"5€":^7} -  {aantal5:^2}    *')
print(f'* {"2€":^7} -  {aantal2:^2}    *')
print(f'* {"1€":^7} -  {aantal1:^2}    *')
print('*'+18*' '+'*')
print(20*'*')