def reverse_number(number: int):
    num = number
    reverse_num = 0
    while num != 0:
        num_mod = num % 10
        reverse_num = (reverse_num * 10) + num_mod
        num = num // 10
    print(reverse_num)


if __name__ == "__main__":
    reverse_number(number=12345)
