
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
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
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

# Registrovaní uživatelé
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

bob = "123"
ann = "pass123"
mike = "password123"
liz = "pass123"

# Jiné
cara = "-" * 35

# TODO
# počet slov
# počet slov začínajících velkým písmenem
# počet slov psaných velkými písmeny
# počet slov psaných malými písmeny
# počet čísel (ne cifer)
# sumu všech čísel (ne cifer) v textu

# pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí
# pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí

# výstupem bude jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu 
# například takto:

# 7| * 1
# 8| *********** 11
# 9| *************** 15
#10| ********* 9
#11| ********** 10

# KÓD

text_cislo = int(input("Vyber číslo textu mezi 1 a 3: "))

print(cara)

if 1 <= text_cislo <= 3:
    text_vypis = TEXTS[text_cislo -1]
    print("Vybrali jste tento text:\n"+ text_vypis)
else:
    print("Číslo " + str(text_cislo) + " není mezi čísly 1 a 3, ukončuji program")
    quit()

print(cara)






