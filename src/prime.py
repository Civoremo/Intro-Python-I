# Program to check if entered number is prime

number = int(input('Enter Number: '))
k = 0
for i in range(2, number//2+1):
    if(number % i == 0):
        k = k+1
if(k <= 0):
    print('Number is prime')
else:
    print('Not a prime number')
