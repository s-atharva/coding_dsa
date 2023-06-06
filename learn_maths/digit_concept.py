def print_digits(number: int):
    num = number
    while num != 0:
        number_mod = num % 10
        num = num // 10
        print(number_mod)


if __name__ == "__main__":
    print_digits(number=12345)
