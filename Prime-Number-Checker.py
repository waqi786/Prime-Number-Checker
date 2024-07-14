def check_prime(n):
    is_prime = True
    for i in range(2,n):
        if n%i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not prime number")

n = int(input("Enter a number here: "))
check_prime(n)