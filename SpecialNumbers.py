def reverse(s): 
  str = "" 
  for i in s:
    str = i + str
  return str

def is_polyndrome(s):
    if s == "":
        return False
    return str(s) == reverse(str(s))

def get_longest_polyndrome(l):
    long_polyndrome = ""
    for item in l:
        if is_polyndrome(item):
            long_polyndrome = long_polyndrome if len(long_polyndrome) > len(str(item)) else len(str(item))
    return long_polyndrome


def digital_root(n):
    if n <= 9:
        return n
    else:
        sum = 0
        for i in str(n):
            sum = int(i) + sum
        return digital_root(sum)

def is_magic_number(n):
    return digital_root(n) == 1

