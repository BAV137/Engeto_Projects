
def line(what, much): 
    return print(
        what * much
    )

hello = '|     5\'_^)>: WELCOME :<(-_^7     |'
too = f'{('|    _^_>: TO :<_^_     |'):^{len(hello)}}'
bulls_cows = f'{('| BUUULS | >X-X-X-X< | COOOWS |'):^{len(hello)}}'



line('-', len(hello))
print(hello)

line('-', len(hello))
print(too)

line('-', len(hello))
print(bulls_cows)

line('-', len(hello))
print(len(hello))