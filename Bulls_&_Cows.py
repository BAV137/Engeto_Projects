
print('-> Hello everybody!')


numbers = list(range(0, 10))
print(numbers)


import random
random.shuffle(numbers)
print(numbers)


secret = numbers[:4]
print(secret)


if secret[0] == 0:
    secret[0], secret[1] = secret [1], secret[0]
print(secret)


sec = []
for x in secret: 
    sec.append(str(x))
print(sec)


secret = ''.join(sec)
print(secret)


print(
    '-> Enter four different numbers from 0 to 9 pls.', 
    '-> The number can\'t start "0".', 
    sep='\n'
)


user_num = input(
    '<-- number: '
)
print(user_num)


while user_num.isdigit() == False: 
    print(
        '-> Only numbers pls.'
    )
    exit()

while len(user_num) != 4: 
    print(
        '-> The number more/less than 4 numbers.'
    )
    exit()

while user_num[0] == '0': 
    print(
        '-> The number can\'t start from "0".'
    )
    exit()

u_n = set(user_num)
while len(u_n) != 4: 
    print(
        '-> Enter four DIFFERENT numbers pls.'
    )
    exit()

bulls = 0
cows = 0
index = 0

for x in user_num: 
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