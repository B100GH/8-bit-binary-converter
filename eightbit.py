
def eightbit():
  print('--------')
  a = input()
  oof = a
  f = 0
  c = str(0)

  if a[0] == '1':
    if a[1] == '0':
     c = c + '1'
    if a[1] == '1':
      c = c + '0'
    if a[2] == '0':
      c = c + '1'
    if a[2] == '1':
      c = c + '0'
    if a[3] == '0':
      c = c + '1'
    if a[3] == '1':
      c = c + '0'
    if a[4] == '0':
      c = c + '1'
    if a[4] == '1':
      c = c + '0'
    if a[5] == '0':
      c = c + '1'
    if a[5] == '1':
      c = c + '0'
    if a[6] == '0':
      c = c + '1'
    if a[6] == '1':
      c = c + '0'
    if a[7] == '0':
      c = c + '1'
    if a[7] == '1':
      c = c + '0'

    a = c 
  print(c)

  if a[7] == '1':
    f = f + 1
  if a[6] == '1':
    f = f + 2
  if a[5] == '1':
    f = f + 4
  if a[4] == '1':
    f = f + 8
  if a[3] == '1':
    f = f + 16
  if a[2] == '1':
    f = f + 32
  if a[1] == '1':
    f = f + 64
  if oof[0] == '1':
   f = (f*-1)-1

  print(f)
