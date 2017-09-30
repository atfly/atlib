

def primes(n):
  
  if n < 2:  return []

  if n == 2: return [2]
 
  s = range(3, n, 2)
 
  mroot = n ** 0.5

  half = len(s)

  i = 0

  m = 3

#www.iplaypy.com

  while m <= mroot:

    if s[i]:
      j = (m * m - 3)//2
      s[j] = 0

      while j < half:
        s[j] = 0
        j += m

    i = i + 1

    m = 2 * i + 3

  return [2]+[x for x in s if x]

