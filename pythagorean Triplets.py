def find_pythagorean_triplets(n):
    triplets = []
    for a in range(1, n):
        for b in range(a, n):
            c_squared = a*2 + b*2
            c = int(c_squared**0.5)
            if c**2 == c_squared and c <= n:
                triplets.append((a, b, c))
    return triplets
n = 10
triplets = find_pythagorean_triplets(n)
print("pythagorean triplets:",triplets)
