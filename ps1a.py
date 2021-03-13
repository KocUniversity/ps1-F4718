n, B = list(map(int, input().strip().split()))
T = 1
sum_p = 0

if n > 0 and B >= 0:

  for i in range(1,n+1):
    if i%2 != 0:
      p = 3**i + 1
    else:
      p = 2**i + 1
    sum_p += p**(n-i)
    
  while T*sum_p <= B:
    T += 1
    if T > 10000:
      break

  if T <= 10000:
    T = T
  else:
    T = -1

else:
  T = -1

print(T)