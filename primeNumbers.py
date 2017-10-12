def primeNumbers(n):
  isPrime = []
  if isinstance(n, (list, dict)):
    raise TypeError("Number should be an integer") 
  else:
    for num in range(2,n + 1):
     
     if num > 1:
         for i in range(2,num):
             if (num % i) == 0:
                 break
         else:
             isPrime.append(num)
    return isPrime

primeNumbers(9)