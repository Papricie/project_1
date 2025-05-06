
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

# Oddělovač
oddelovac = "-" * 50

# UŽIVATELSKÝ VSTUP
# A/ uživatel se přihlásí jménem a heslem
# B/ vybere číslo mezi 1 a 3, pokud vybere číslo, které NENÍ V ZADÁNÍ, program jej upozorní a skončí
# C/ pokud uživatel zadá JINÝ vstup NEŽ ČÍSLO, program jej rovněž upozorní a skončí

# ANALÝZA:
# počet slov
# počet slov začínajících velkým písmenem
# počet slov psaných velkými písmeny
# počet slov psaných malými písmeny
# počet čísel (ne cifer)
# sumu všech čísel (ne cifer) v textu

# VÝSTUP
# sloupcový graf, který bude reprezentovat četnost různých délek slov v textu, např:

# 7| * 1
# 8| *********** 11
# 9| *************** 15
#10| ********* 9
#11| ********** 10


################ KÓD ################

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


# Ověření uživatele
if zadane_jmeno in registrovani_uzivatele and registrovani_uzivatele[zadane_jmeno] == zadane_heslo:
    print("Vítej v mém analyzátoru textu,", zadane_jmeno + "!")
else:
    print("Neregistrovaný uživatel, ukončuji program.")
    quit()


print(oddelovac)


# Výběr textu
text_cislo = input("Teď vyber číslo textu mezi 1 a 3: ")
if text_cislo.isdigit():
    text_cislo = int(text_cislo)
    if 1 <= text_cislo <= 3:
        text_vypis = TEXTS[text_cislo -1]
        

        print(oddelovac)
        
        
        print("Vybraný text:\n"+ text_vypis)
        

        print(oddelovac)

 # Analýza textu       
        pocet_slov = [slovo.strip(",.()") 
                      for slovo in TEXTS[text_cislo -1].split() 
                      if slovo.strip(",.()")]
        
        psano_velkymi = []
        for slovo in TEXTS[text_cislo -1].split():
            ciste = slovo.strip(",.()")
            if ciste.isupper():
                psano_velkymi.append(ciste)
        
        zacinajici_velkym = []
        for slovo in TEXTS[text_cislo -1].split():
            ciste = slovo.strip(",.()")
            if ciste[0].isupper() and ciste.isalpha():
                zacinajici_velkym.append(ciste)
        
        psano_malymi = []
        for slovo in TEXTS[text_cislo -1].split():
            ciste = slovo.strip(",.()")
            if ciste.islower():
                psano_malymi.append(ciste)
        
        pocet_cisel = 0
        for slovo in TEXTS[text_cislo -1].split():
            if slovo.isdigit():
                pocet_cisel += 1
        
        suma_cisel = 0
        for slovo in TEXTS[text_cislo -1].split():
            if slovo.isdigit():
                suma_cisel += int(slovo)
# Výsledky
        print("Analýza textu:\n")
        print("Počet slov v textu:", len(pocet_slov))
        print("Počet slov začínající velkým písmenem:", len(zacinajici_velkym))
        print("Počet slov psáno velkými písmeny: ", len(psano_velkymi))
        print("Počet slov psáno malými písmeny: ", len(psano_malymi))
        print(f"Počet čísel: {pocet_cisel}")
        print(f"Suma všech čísel: {suma_cisel}")    
    
    else:
        print("Toto číslo rozhodně není mezi 1 a 3, ukončuji program")
        quit()
else:
    print(str(text_cislo) + " rozhodně není číslo, ukončuji program")
    quit()


print(oddelovac)

# Graf s délkou slov
slova = [slovo.strip(",.()") for slovo in TEXTS[text_cislo -1].split() if slovo.strip(",.()")]

delky_slov = [len(slovo) for slovo in slova]

delky_pocet = {}
for delka in delky_slov:
    if delka in delky_pocet:
        delky_pocet[delka] += 1
    else:
        delky_pocet[delka] = 1

# Výpis hvězdičkového grafu pro délky slov
print("Hvězdičkový graf pro délky a výskyt slov:\n")
print("| Délka?  " "| Výskyt? |\n")
for delka, vyskyt in delky_pocet.items():
    print(f"| {delka} znaků |{' *' * vyskyt} | {vyskyt}x |")
    