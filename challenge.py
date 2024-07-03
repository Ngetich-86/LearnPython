def is_prime_no(num):
    if num <2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
        return True
def display_prime():
    for num in range(1,251):
        if is_prime_no(num):
            print(num)
display_prime()