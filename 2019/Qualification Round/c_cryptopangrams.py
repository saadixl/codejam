# I GOT RE ON THIS ONE
alphas = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_prime_tuple(product, primes):
    for m in primes:
        for n in primes:
            if m != n and m*n == product:
                return (m,n)

def gen_primes(n):
    primes = []
    for i in range(2,n):
        if all(i%j!=0 for j in range(2,i)):
            primes.append(i)
    return primes

t = input()
for i in range(int(t)):
    l1 = input()
    line_1 = l1.split(' ')
    l2 = input()
    prime_products = l2.split(' ')
    n = int(line_1[0])
    message_len = int(line_1[1])
    primes = gen_primes(n+1)
    flag = 0
    first_prime = None
    second_prime = None
    result = []
    for product in prime_products:
        flag = flag + 1
        if flag == 1:
            prime_tuple = get_prime_tuple(int(product), primes)
            first_prime = prime_tuple[0]
            second_prime = prime_tuple[1]
            possible_n = int(int(prime_products[1]) / int(first_prime));
            if possible_n in primes:
                temp = first_prime
                first_prime = second_prime
                second_prime = temp
            result.append(int(first_prime))
            result.append(int(second_prime))
        else:
            first_prime = int(product)/second_prime
            second_prime = first_prime
            result.append(int(first_prime))
    original_result = result.copy()
    result = list(set(result))
    result.sort()
    message = ""
    for item in original_result:
        char_index = result.index(item)
        message += alphas[char_index]
    print("Case #"+str(i+1)+": "+message)
