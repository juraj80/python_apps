def main():
    count = 0
    for n in print_primes(1000000):
        count += 1
#        print(n, end = ', ')
#    print(prime(21))
    print(count)

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def print_primes(num):
    for i in range (2,num):
        if prime(i):
            yield i

if __name__ == '__main__':
    main()