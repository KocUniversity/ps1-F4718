# sum_p = 0
# num_of_iterations = 0
# B=int(input("give a B: "))
# n=int(input("give an n: "))
# for i in range(1,n+1):
#   if i%2 != 0:
#     p = (3**i)+1
#   else:
#     p = (2**i)+1
#   sum_p += p**(n-i)
#   num_of_iterations += 1

# print(B/sum_p)

# T = int(B/sum_p)+1
# print(T)
# print("Number of iterations is:",num_of_iterations)

###########################################################

# B = 11830000
# # 11828817
# n = 5
# T = 0
# sum_p = 0

# for i in range(1,n+1):
#   if i%2 != 0:
#     p = 3**i + 1
#   if i%2 == 0:
#     p = 2**i + 1
#   sum_p += p**(n-i)



# while T*sum_p < B:
#   T += 1
#   if T > 10000:
#     break

# if T <= 10000:
#   print("T minimum is equal to:",T)
# else:
  # print("NOT FOUND")

###########################################################

# B = 589999
# n = 4
# sum_p = 0
# low = 0
# high = 10000

# for i in range(1,n+1):
#   if i%2 != 0:
#     p = 3**i + 1
#   else:
#     p = 2**i + 1
#   sum_p += p**(n-i)

# guess = (low+high)/2
# while high-low > 1:
#   if guess*sum_p >= B:
#     high = guess
#   elif guess*sum_p < B:
#     low = guess
#   guess = (low+high)/2


# if (int(low)+1)*sum_p > B:
#   T = int(low)+1
#   print("T minimum is equal to:",T)
# elif (int(low)+2)*sum_p > B:
#   T = int(low)+2
#   print("T minimum is equal to:",T)
# else:
#   print("SORRY, T IS GREATER THAN 10000!")



  
