from algemene_functies import mijn_functie_2

#vraag 5
def aanbieding_1 (smaak, prijs, korting):
    korting = "{:.2f}".format (korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."
    return uitvoer

print (aanbieding_1 ("aardbei", 4, (4.00* (1-0.1))))

#vraag 6 en 7
def inkomsten_totaal_2 (totaal, btw):
	totaal = sum (inkomsten)
	bedrag = totaal * btw
	uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
	return uitvoer

inkomsten = [220, 430, 125, 160, 205, 90, 345]

print (inkomsten_totaal_2 (inkomsten, 0.09))

#vraag 8
def laag_en_hoog (mijn_lijst):
     opbrengst = max (mijn_lijst), min (mijn_lijst)
     return opbrengst
     
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

print (laag_en_hoog (mijn_lijst))

#vraag 9 en 10
def gemiddelde (mijn_lijst):
    berekening = (sum(mijn_lijst))/len (mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten van deze week zijn {berekening} euro."
    return uitvoer
   
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

print (gemiddelde (mijn_lijst))

#vraag 11
def meervoudig (invoer_lijst):
     invoer_lijst = laag_en_hoog (invoer_lijst)
     return invoer_lijst

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]

print (meervoudig (invoer_lijst))

#vraag 12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9]

print (combinatie (invoer_lijst_2))