#Prime
#This program will print out all the prime numbers up to a given number.

def main():
  print("This program will find all the primes up to a given number.")

  x = input("Enter a number: ")
  topNumber = x+1
  isPrime = [True]*topNumber

  for i in range(2,topNumber):
    if isPrime[i]:
      for j in range(i**2,topNumber,i):
        isPrime[j] = False

      print i,

main()

