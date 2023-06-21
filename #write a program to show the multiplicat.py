#write a program to show the multiplication table of first 20 prime numbers using for loop.

def is_prime(number):
    if number <2:
        return False
    for i in range(2,int(number/2)+1):
        if number%i ==0:
            return False
    return True    

count=0
number=1
prime_list=[]
while count<20:
    if is_prime(number):
        prime_list.append(number) 