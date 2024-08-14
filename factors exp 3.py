def factors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result
def nth_factor(num, n):
    factor_list = factors(num)
    num_factors = len(factor_list)
    print(f"Number of factors of {num}: {num_factors}")
    if n <= num_factors:
        print(f"The {n}th factor of {num} is:{factor_list[n - 1]}")
    else:
        print(f"The number {num} has only {num_factors}n th factors.")
given_number = 100
n = 4
nth_factor(given_number, n)
