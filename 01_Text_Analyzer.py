
# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Artur Boyko
# email: boykoartur@gmail.com
# discord: ?

def line(what = '-', much = 79):
    return print(
        what * much
        )

line()
print('$ python projekt1.py')

users = {
    'bob': '123', 
    'ann': 'pass123', 
    'mike': 'password123', 
    'liz': 'pass123'
}

line()
login = input(
    '<-- username: '
)
password = input(
    '<-- password: '
)

if password == users.get(login):
    line()
    print(
        f'---> !!! Welcome {login.title()} !!!'
    )
else:
    line()
    print(
    '!!! Attention !!!', 
    ' -> username <-', 
    '(or)', 
    ' -> password <-', 
    '-> isn\'t True! <-', 
    sep='\n'
    )
    line()
    exit()

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
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

line()
print(
    f'-> Today, we have 3 texts to be analyzed:'
    )

line()
for x in TEXTS:
    print(
        f"''' {x[:30]}... '''"
    )

line()
text_num = input(
    f'<-- Pls, enter the number from 1 to 3: '
)

while text_num.isdigit() == False:
    line()
    print(
        f'-> Only NUMBER from -> 1 to 3 <- PLS!'
    )
    line()
    exit()

while int(text_num) not in range(1, 4):
    line()
    print(
        f'-> Today ONLY from -> 1 to 3 <- PLS!'
    )
    line()
    exit()

text = TEXTS[int(text_num) - 1]

spl_text = text.split()


line()
print(
    f'-> Počet slov: {len(spl_text)}'
)


line()
ps_zvp = sum(
    1 for x in spl_text if x[0].istitle()
)
print(
    f'-> Počet slov začínajících velkým písmenem: {ps_zvp}'
)


line()
ps_pvp = sum(
    1 for x in spl_text if x.isalpha() and x.isupper()
)
print(
    f'-> Počet slov psaných velkými písmeny: {ps_pvp}'
)


line()
ps_pm = sum(
    1 for x in spl_text if x.islower()
)
print(
    f'-> Počet slov psaných malými písmeny: {ps_pm}'
)


line()
p_cisel = 0
sum_cisel = 0
for x in spl_text:
    if x.isdigit():
        p_cisel += 1
        sum_cisel += int(x)
print(
    f'-> Počet čísel: {p_cisel}'
)


line()
print(
    f'-> Suma všech čísel v textu: {sum_cisel}'
)


len_slov = []
for x in spl_text:
    mnoz = 0
    for i in x:
        if i.isdigit() or i.isalpha():
            mnoz += 1
    len_slov.append(mnoz)

print(len_slov)

jme_mnoz = {}
for x in len_slov:
    if x not in jme_mnoz: 
        jme_mnoz[x] = 1
    else:
        jme_mnoz[x] += 1

print(jme_mnoz)

sort_jme_mnoz = sorted(jme_mnoz)

max_len = max(jme_mnoz.values())

print(max_len)

line()
print(
    f'LEN|  OCCURENCES  |NR.'
)
line()

for x in sort_jme_mnoz:
    if x < 10:
        print(f'  {x}|{("*" * jme_mnoz.get(x)):<{max_len + 1}}|{str(jme_mnoz.get(x))}')
    else: 
        print(f' {str(x)}|{("*" * jme_mnoz.get(x)):<{max_len + 1}}|{str(jme_mnoz.get(x))}')