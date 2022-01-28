from eightbit import eightbit
from decimal import decimal 

b = 1

d = input('''
- - - - - - MENU - - - - - -
  1 -  Decimal to Binary
  2 -  Binary to Decimal

''')
if d == '1':
  decimal()

if d == '2':
  while b == 1:
    eightbit()
    a = input('Run Again? y or n -- ')
    if a == 'y':
      print()
    else:
      b = 2