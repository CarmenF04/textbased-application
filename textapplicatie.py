import time

def displayIntro():
    print("Welkom bij mijn beroepsopdracht")
    time.sleep(2)
    print("In dit verhaal ben jij een vluchteling uit Syrië")
    time.sleep(2)
    print("Je moet vluchten omdat de Taliban het land heeft overgenomen waardoor je nu niet meer veilig bent")
    time.sleep(2)
    print("Het verhaal kan goed uitpakken, maar het kan ook helemaal mis gaan")
    time.sleep(2)
    print("Succes en veel plezier!")
    vraag1()



def vraag1():
    vraag1 = input("""Je bent onderweg naar werk wanneer je oppeens pistool schoten hoort. Mensen beginnen in paniek te raken. Wat doe je?\n

    A) Je gaat naar werk
    B) Je gaat naar je familie \n""")
    if vraag1.lower() == "a":
        vraag2()
    elif vraag1.lower() == "b": 
        vraag5()

def vraag2():
    vraag2 = input("""\n Je rent zo snel mogelijk naar werk om daar te verstoppen.
   Je komt binnen en je ziet dat al je collega's zich verschuilen.
   Je vraagt wat er aan de hand is en ze zeggen dat de Taliban de stad binnen is gekomen. 
   \n Je raakt in paniek en denkt nu pas aan je familie! Zou het wel goed met ze gaan? \n

    A) Je gaat gelijk naar je familie toe
    B) Je blijft je verstoppen \n""") 
    if vraag2.lower() == "a":
        vraag3()
    elif vraag2.lower() == "b":
        vraag4()

def vraag3(): 
    vraag3 = input("""\n Je denkt niet na waardoor je naar buiten rent, zodra je naar buiten rent wordt je door je achterhoofd geschoten.

    A) Opnieuw beginnen 
    B) Terug naar vraag 2\n""")
    if vraag3.lower() == "a":
        vraag1() 
    elif vraag3.lower() == "b":
        vraag2()

def vraag4(): 
    vraag4 = input("""\n Na een paar uur verstoppen ben je het zat en besluit je toch naar je familie te gaan, je zegt vaarwel tegen je collega's en staat op het punt om ervandoor te gaan.
   Maar ineens twijfel je...

    A) Blijven
    B) Weggaan \n""") 
    if vraag4.lower() == "a":
       vraag6()
    elif vraag4.lower() == "b":
       vraag5()

def vraag5(): 
    vraag5 = input("""\n Je komt snel je huis binnen en je familie wist al gelijk wat er aan de hand was. We moesten vluchten.
   Je moet snel bedenken wat je mee gaat nemen.

    A) Eten 
    B) Nog meer eten  \n""") 
    if vraag5.lower() == "a":
       vraag7()
    elif vraag5.lower() == "b":
       vraag7()

def vraag6(): 
    vraag6 = input("""\n Na een tijd vallen mannen van de Taliban het pand binnen. Niemand komt er levend uit.

    A) Opnieuw beginnen. 
    B) Terug naar vraag 4 \n""") 
    if vraag6.lower() == "a":
       vraag1()
    elif vraag6.lower() == "b":
       vraag4()

def vraag7(): 
    vraag7 = input("""\n Eten is het belangerijkst, jij en je familie pakken snel de auto en gaan er van door. 
    Je laat het huis waar je bent opgegroeid achter.
    Na een paar uur komen jullie aan in Turkije, het plan is om vanuit daar naar Griekenland te gaan.
    Hoe ga je dat doen?

    A) Zwemmen 
    B) Boot \n""") 
    if vraag7.lower() == "a":
       vraag9()
    elif vraag7.lower() == "b":
       vraag8()

def vraag8(): 
    vraag8 = input("""\n De boot is de beste keuze, als je ging zwemmen zou je waarschijnlijk verdrinken.
    Je kwam aan bij de kust en je was niet de enige die van plan was om te vluchten.
    Je propte jezelf nog tussen alle mensen en toen begon de lange zee reis.
    Na een tijd begon te boot langzaam te zinken. Gedachtes schieten door je hoofd.

    A) Je gooit mensen van de boot af 
    B) Je neemt het risico en blijft rustig zitten \n""") 
    if vraag8.lower() == "a":
       vraag10()
    elif vraag8.lower() == "b":
       vraag11()

def vraag9(): 
    vraag9 = input("""\n Je vindt de boot te vol en besluit om te gaan zwemmen maar je wordt even later opgegeten door een haai.

    A) Opnieuw beginnen 
    B) Terug naar vraag 7 \n""") 
    if vraag9.lower() == "a":
       vraag1()
    elif vraag9.lower() == "b":
       vraag7()

def vraag10(): 
    vraag10 = input("""\n "Sorry" zeg je wanneer je mensen van de boot af begint te duwen. 
    Je had geen andere keus.
    Eenmaal aangekomen op het vasteland ging je richting Macedonië, vanuit daar moest je naar Servië.
    Hoe ga je daar heen?

    A) Trein 
    B) Lopend \n""") 
    if vraag10.lower() == "a":
       vraag12()
    elif vraag10.lower() == "b":
       vraag13()

def vraag11(): 
    vraag11 = input("""\n De boot begint vol met water te lopen en uiteindelijk zink je naar de bodem van de oceaan.

    A) Opnieuw beginnen 
    B) Terug naar vraag 8 \n""") 
    if vraag11.lower() == "a":
       vraag1()
    elif vraag11.lower() == "b":
       vraag8()

def vraag12(): 
    vraag12 = input("""\n Je pakt de trein richting Servië en vanuit daar ben je binnen een paar uur in Hongarije. 
    Wanneer je uit de trein stapt komt er een politie agent op je aflopen.
    De Hongaarse politie wil namelijk van iedereen een vingerafdruk hebben om te kijken wie er aankomt. 
    Het probleem is dat je daarna in Hongarije moet blijven. 
    Ren je het bos in om te verstoppen of blijf je voor de rest van je leven in Hongarije?

    A) Je rent het bos in 
    B) Je blijft in Hongarije \n""") 
    if vraag12.lower() == "a":
       vraag14()
    elif vraag12.lower() == "b":
       vraag15()

def vraag13(): 
    vraag13 = input("""\n Het lopen was te vermoeiend geworden. Je had geen drinken mee dus je bent uitedroogd.

    A) Opnieuw beginnen 
    B) Terug naar vraag 10 \n""") 
    if vraag13.lower() == "a":
       vraag1()
    elif vraag13.lower() == "b":
       vraag10()

def vraag14(): 
    vraag14 = input("""\n Je rent zo snel als je maar kan het bos in en je zoekt een schuil plaats. 
    Je hoort de politie agent roepen maar je blijft door rennen. Je rent diep het bos in en het begint al donker te worden.
    Je gaat zitten op de grond wanneer je ineens een hand op je schouder voelt. 
    Je draait je snel om en staat klaar om de man een hoek te geven wanneer hij zegt dat hij je kan helpen om in Boedapest te komen.

    A) Laat hem je helpen 
    B) Geef hem een klap \n""") 
    if vraag14.lower() == "a":
       vraag16()
    elif vraag14.lower() == "b":
       vraag17()

def vraag15(): 
    vraag15 = input("""\n Je hebt besloten om in Hongarije te blijven en hier je leven op te bouwen.

    A) Opnieuw beginnen 
    B) Terug naar vraag 12 \n""") 
    if vraag15.lower() == "a":
       vraag1()
    elif vraag15.lower() == "b":
       vraag12()

def vraag16(): 
    vraag16 = input("""\n Na ongeveer een week ben je met de hulp van de man die een smokkelaar bleek te zijn in Boedapest terecht gekomen.
   Blijf je hier of ga je toch nog door? 
    A) Je blijft hier
    B) Je gaat door \n""") 
    if vraag16.lower() == "a":
       vraag18()
    elif vraag16.lower() == "b":
       vraag19()

def vraag17(): 
    vraag17 = input("""\n Uit angst geef je de man een klap voor zijn hoofd waardoor hij op de grond neervalt en niet meer opstaat.
     Eigenlijk heb je geen flauw idee waar je nu heen moet en blijf je nog een maand lang door de bossen heen lopen.
    Uit he niets word je aangevallen door een beer en helaas heb je dat niet overleeft.

    A) Opnieuw beginnen 
    B) Terug naar vraag 14 \n""") 
    if vraag17.lower() == "a":
       vraag1()
    elif vraag17.lower() == "b":
       vraag14()

def vraag18(): 
    vraag18 = input("""\n Je hebt besloten om in Boedapest te blijven en hier je leven op te bouwen.

    A) Opnieuw beginnen 
    B) Terug naar vraag 16 \n""") 
    if vraag18.lower() == "a":
       vraag1()
    elif vraag18.lower() == "b":
       vraag16()

def vraag19(): 
    vraag15 = input("""\n Uiteindelijk kom je in een trein terecht richting Duitsland, waarna je nog diezelfde dag in München aankwam. 
    Blijf je in Duitsland of ga je toch naar Nederland?

    A) Duitsland
    B) Nederland\n""") 
    if vraag15.lower() == "a":
       vraag20()
    elif vraag15.lower() == "b":
       vraag21()

def vraag20(): 
    vraag18 = input("""\n Je hebt besloten om in Duitsland te blijven sinds het erg op Nederland lijkt.

    A) Opnieuw beginnen 
    B) Terug naar vraag 19 \n""") 
    if vraag18.lower() == "a":
       vraag1()
    elif vraag18.lower() == "b":
       vraag19()

def vraag21(): 
    vraag21 = input("""\n Je eindbestemming was tenslotte Nederland dus natuurlijk ga je door.
    Je pakt de trein naar Amsterdam Centraal en na uren lang reizen ben je er dan eindelijk. Je eindbestemming. 
    Ga je asiel aanvragen of blijf je door de stad heen lopen?  

    A) Asiel aanvragen 
    B) Door de stad blijven lopen \n""") 
    if vraag21.lower() == "a":
       vraag22()
    elif vraag21.lower() == "b":
       vraag23()

def vraag22(): 
    vraag22 = input("""\n Je gaat naar het dichtsbijzijnde politie bureau en vraagt papieren aan voor het asiel. 
    Je wordt toegelaten en je verblijft daar een aantal maanden.
    Je begint de taal al goed te begrijpen als je zo door gaat kan je je leven snel weer oppakken.
    Een paar jaar later heb je je leven weer opgepakt. 
    Je hebt een baan gekregen en je helpt nu andere vluchtelingen om hun leven verder te helpen. 

    Einde\n""")

def vraag23(): 
    vraag18 = input("""\n Je loopt door de mooie stad heen maar je wordt doodgereden door een auto.

    A) Opnieuw beginnen 
    B) Terug naar vraag 21 \n""") 
    if vraag18.lower() == "a":
       vraag1()
    elif vraag18.lower() == "b":
       vraag21()

def vraag24(): 
    vraag24 = input("""\n Wouw je hebt het einde van het verhaal bereikt! Wil je het nog een keer spelen of laat je het hierbij?
    
    A) Nog een keer!
    B) Een mooi einde \n""") 
    if vraag24.lower() == "a":
       vraag1()
    elif vraag24.lower() == "b":
       vraag19()


    
displayIntro()