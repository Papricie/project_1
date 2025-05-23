
# HLAVIČKA PROJEKTU
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Patricie Hermanová
email: patriciehermanova@gmail.com
"""

# ZADÁNÍ PROJEKTU

# Analyzované texty
TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.
    ''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    ''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.
    '''
]

# Registrovaní uživatelé - vytvořit si slovník
"""
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""

# UŽIVATELSKÝ VSTUP
# A/ uživatel se přihlásí jménem a heslem
# B/ vybere číslo mezi 1 a 3, pokud vybere číslo, které NENÍ V ZADÁNÍ, 
#    program jej upozorní a skončí
# C/ pokud uživatel zadá JINÝ vstup NEŽ ČÍSLO, 
#    program jej rovněž upozorní a skončí

# ANALÝZA:
# počet slov
# počet slov začínajících velkým písmenem
# počet slov psaných velkými písmeny
# počet slov psaných malými písmeny
# počet čísel (ne cifer)
# sumu všech čísel (ne cifer) v textu

# VÝSTUP
# A/ slovní analýza s výsledky
# B/ sloupcový graf, který bude reprezentovat četnost různých délek slov, např:

# 7| * 1
# 8| *********** 11
# 9| *************** 15
#10| ********* 9
#11| ********** 10

# Oddělovač
oddelovac = "-" * 50

###################################### KÓD ####################################

# Slovník se jmény a hesly
registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Zadaní jména a hesla uživatelem
zadane_jmeno = input("Zadej uživatelské jméno: ")
zadane_heslo = input("Zadej heslo: ")

print(oddelovac)
#------------------------------------------------------------------------------

# Ověření uživatele
spravne_jmeno = zadane_jmeno in registrovani_uzivatele
spravne_heslo = registrovani_uzivatele.get(zadane_jmeno) == zadane_heslo

if spravne_jmeno and spravne_heslo:
    print("Vítej v mém analyzátoru textu,", zadane_jmeno + "!")
else:
    print("Neregistrovaný uživatel, ukončuji program.")
    quit()

print(oddelovac)
#------------------------------------------------------------------------------

# Výběr textu
text_cislo = input("Teď vyber číslo textu mezi 1 a 3: ")
if text_cislo.isdigit():
    text_cislo = int(text_cislo)
    if 1 <= text_cislo <= 3:
        vybrany_text = TEXTS[text_cislo - 1] # 2 POKUS - vytvoření proměnné
        
        print(oddelovac)
        
        print("Vybraný text:\n" + vybrany_text) # 2p - proměnná vybrany_text 

        print(oddelovac)
#------------------------------------------------------------------------------

# Analýza textu - 2 pokus nachystané proměnné pro interpunkci a hledaná slova
        interpunkce = ",.():?!*+-/=" # lepší čistění
        pocet_slov = 0
        psano_velkymi = 0
        zacinajici_velkym = 0
        psano_malymi = 0
        pocet_cisel = 0
        suma_cisel = 0

        for slovo in vybrany_text.split(): # 2p pouze jeden for cyklus
            ciste = slovo.strip(interpunkce)
            if not ciste:
                continue

            pocet_slov += 1

            if ciste.isupper():
                psano_velkymi += 1
            elif ciste.islower():
                psano_malymi +=1
            elif ciste[0].isupper() and ciste.isalpha():
                zacinajici_velkym += 1

            if ciste.isdigit():
                pocet_cisel += 1
                suma_cisel += int(ciste)

# Výsledky - 2p vypsání s novými proměnnými
        print("Analýza textu:\n")
        print("Počet slov v textu:", pocet_slov)
        print("Počet slov začínající velkým písmenem:", zacinajici_velkym)
        print("Počet slov psáno velkými písmeny:", psano_velkymi)
        print("Počet slov psáno malými písmeny:", psano_malymi)
        print(f"Počet čísel: {pocet_cisel}")
        print(f"Suma všech čísel: {suma_cisel}")

    else:
        print("Toto číslo rozhodně není mezi 1 a 3, ukončuji program")
        quit()
else:
    print("Zadaný vstup rozhodně není číslo, ukončuji program")
    quit()

print(oddelovac)
#------------------------------------------------------------------------------

# Graf s délkou slov - 2p použití proměnné interpunkce
slova = [slovo.strip(interpunkce) for slovo in vybrany_text.split() 
         if slovo.strip(interpunkce)]  

delky_slov = [len(slovo) for slovo in slova]

delky_pocet = {}
for delka in delky_slov:
    if delka in delky_pocet:
        delky_pocet[delka] += 1
    else:
        delky_pocet[delka] = 1

delky_pocet = dict(sorted(delky_pocet.items()))

# Výpis hvězdičkového grafu pro délky slov
print("Hvězdičkový graf pro délky a výskyt slov:\n")
print("|  Délka  |  Výskyt  |\n")
for delka, vyskyt in delky_pocet.items():
    print(f"| {delka} znaků |{'*' * vyskyt} | {vyskyt}x |")

print(oddelovac)
#------------------------------------------------------------------------------

print("Díky za vyzkoušení mého analyzátoru,", zadane_jmeno + "!")

print(oddelovac)
#------------------------------------------------------------------------------
    