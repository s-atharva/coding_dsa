def gcd(number_1, number_2):
    for i in range(min(number_1, number_2), 1, -1):
        if number_1 % i == 0 and number_2 % i == 0:
            print(i)
            break


if __name__ == "__main__":
    gcd(number_1=30, number_2=20)
