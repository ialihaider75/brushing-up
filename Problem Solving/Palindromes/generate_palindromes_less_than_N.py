def generate_palindromes(i, is_odd):
    if (is_odd):
        n = i // 10
    else:
        n = i
    while(n > 0):
        i = i * 10 + (n % 10)
        n = n // 10
    return i
    
for k in range(2):    
    i = 1
    while(generate_palindromes(i, k%2) < 100000):
        print(generate_palindromes(i,k%2))
        i += 1
    