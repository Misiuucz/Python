##for i in range(1,11):
#How input works
#First input set up a length of the list of numbers to check
#Every next input will be a number to check
##############################
#
# This function checks if a number is a prime number. If it is, it will return string "YES". Otherwise it will return "NO"

def isPrime(a):
    if(a <= 1):
        return(str(a) + ' is not a prime number')
    for i in range(2,a):
        if (a % i == 0):
            return (str(a) + ' is not a prime number')
    return(str(a) + ' is a prime number')

###############################

a = input('How many numbers you want to check? - ')
a = int(a)

NumArray = []

for i in range(0,a):
    b = input("Insert "+str(i+1)+ " number: ")
    NumArray.append(b)

for i in range(0,a):
    print(isPrime(int(NumArray[i])))
