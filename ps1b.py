n, B = list(map(int, input().strip().split()))
sum_p = 0
low = 0
high = 10000

if n > 0 and B >= 0:

  for i in range(1,n+1):
    if i%2 != 0:
      p = 3**i + 1
    else:
      p = 2**i + 1
    sum_p += p**(n-i)

  guess = (low+high)/2
  while high-low > 1:
    if guess*sum_p >= B:
      high = guess
    elif guess*sum_p < B:
      low = guess
    guess = (low+high)/2


  if (int(low)+1)*sum_p > B and int(low)+1 <= 10000:
    T = int(low)+1 
  elif (int(low)+2)*sum_p > B and int(low)+2 <= 10000:
    T = int(low)+2  
  else:
    T = -1
    
else:
  T = -1

print(T)