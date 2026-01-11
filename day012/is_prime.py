# You need to write a function called is_prime() 
# that checks whether if the number passed into it 
# is a prime number or not (only divisibly by 1 and itself).  
# It should return True or False.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True