# texty, zadání
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

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
garpike and stingray are also present.'''
]

oddelovac = "-" * 40
users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}

# pozdrav programu a vyžádání vstupu od uživatele (1,2)
print(oddelovac)
print("Welcome to the app. Please log in:")
USERNAME = input("USERNAME: ")
PASSWORD = input("PASSWORD: ")
print(oddelovac)

# zjistíme zda údaje odpovídají někomu z uživatelů (3)
if PASSWORD != users.get(USERNAME):
    print("Wrong username or password.")
    print("The app is closing.")
    exit()
else:
    print(f"Welcome to the app {USERNAME}")
    print("We have", len(TEXTS), "texts to be analyzed.")
    print(oddelovac)

# necháme vybrat uživatele mezi texty, pokud uživatel vybere takové číslo textu,
# které není v zadání, program jej upozorní a skončí(4)
text_number = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

if str(text_number).isnumeric() == False:
    print("You didn´t put in a number.")
    exit()
elif int(text_number) not in range(len(TEXTS)+1):
    print("You put in a wrong number.")
    exit()
else:
    print(oddelovac)

# Pro vybraný text spočítá následující statistiky:(5)
#- počet slov,
#- počet slov začínajících velkým písmenem,
#- počet slov psaných velkými písmeny,
#- počet slov psaných malými písmeny,
#- počet čísel (ne cifer),
#- sumu všech čísel (ne cifer) v textu.

# rozdělení textu na list a zjistění počtu slov
text_list = list(TEXTS[int(text_number)-1].split())
words_count = len(text_list)

# vytvoření proměných, podmínky
words_title = []
words_upper = []
words_lower = []
words_number = []
words_sum = 0
for word in text_list:
    if word.istitle():
        words_title.append(word)
    elif word.isupper():
        words_upper.append(word)
    elif word.islower():
        words_lower.append(word)
    elif word.isnumeric():
        words_number.append(word)
        words_sum += int(word)

# výpis odpovědí
print(f"""There are {words_count} words in the selected text.
There are {len(words_title)} titlecase words.
There are {len(words_upper)} uppercase words.
There are {len(words_lower)} lowercase words.
There are {len(words_number)} numeric strings.
The sum of all the numbers {words_sum}.""")
print(oddelovac)

# Program zobrazí jednoduchý sloupcový graf,
# který bude reprezentovat četnost různých délek slov v textu.

graf = {}
for word in text_list:
    word = word.strip(",.!?")
    graf[len(word)] = graf.setdefault(len(word), 0) + 1

# vypsání grafu

print("LEN|", "OCCURENCES".center(max(graf.values())), "|NR.")
print(oddelovac)

for x in range(min(graf.keys()), max(graf.keys())+1):
    if x not in graf:
        continue
    else:
        print(str(x).rjust(3) + "|" + "*" * int(graf[x]) + "|".rjust(max(graf.values()) + 3 - graf.get(x)) + str(graf[x]))


