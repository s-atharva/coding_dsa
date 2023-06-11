def count_factors(number: int):
    count = 0
    list_of_factors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            # print(i)
            list_of_factors.append(i)
            if number // i != i:
                # print(number // i)
                list_of_factors.append(number // i)
    return len(list_of_factors)


def check_prime(number: int):
    number_of_factors = count_factors(number)
    number_for_prime = 2
    if number_of_factors == number_for_prime:
        return "Prime"
    else:
        return "Not a Prime"


if __name__ == "__main__":
    print(check_prime(number=23))
