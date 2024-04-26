
print('Hello everybody!')


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



print(
    '-> Enter four different numbers from 0 to 9 pls.', 
    '-> The number can\'t start "0" ...', 
    sep='\n'
)
user_num = input(
    '<-- number: '
)
print(user_num)


