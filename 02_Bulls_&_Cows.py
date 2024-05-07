
def line(what = '-', much = 79): 
    return print(
        what * much
    )

nums = list(
    range(0, 10)
)

import random
random.shuffle(nums)

if nums[0] != 0:
    sec = nums[:4]
else:
    sec = nums[1:5]

secret = list()

for i in sec:
    secret.append(
        str(i)
    )
secret = ''.join(
    secret
)


while True: 

    cislo = input(
        '<-- numbers: '
    )

    if cislo.isdigit() is False: 
        print(
            '-> Only numbers pls'
        )
        continue

    elif len(cislo) != 4: 
        print(
            '-> Four(4) numbers pls'
        )
        continue

    elif cislo[0] == '0': 
        print(
            '-> The number can\'t start >0<...'
        )
        continue

    elif len(set(cislo)) != 4: 
        print(
            '-> Four(4) different numbers pls'
        )
        continue

    break

bulls = 0
cows = 0
index = 0

for x in cislo: 
    if x in secret and x == secret[index]:
        bulls += 1
    elif x in secret and x != secret[index]: 
        cows += 1
    index += 1

if bulls == 0 and cows == 0:
    print(
        '-> Sorry, u dont tip any numbers :('
    )
elif bulls == 4:
    print(
        'Congrat! U WON!'
    )
else:
    print(
        f'Bulls: {bulls} / Cows: {cows}'
    )