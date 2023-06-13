def print_divisors(number: int):
    factors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if (number // i) != i:
                factors.append(number // i)
    return sorted(factors)


if __name__ == "__main__":
    print(print_divisors(number=36))
