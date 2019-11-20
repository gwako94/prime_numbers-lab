def primeNumbers(n):
  # n integer 
  isPrime = []
  if not isinstance(n, int):
    raise TypeError('Input should be an integer')
  for num in range(2, n + 1):
    for i in range(2, num):
      if num % i == 0:
        break
    else:
      isPrime.append(num) 
  return isPrime

