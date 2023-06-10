def calculate_armstrong_value(number: int):
    num = number
    num_length = len(str(num))
    armstrong_number = 0
    while num != 0:
        remainder = num % 10
        armstrong_number += remainder ** num_length
        num = num // 10
    return armstrong_number


def check_armstrong_number(number):
    armstrong_number = calculate_armstrong_value(number)
    if number == armstrong_number:
        return "Armstrong number"
    else:
        return "Not a Armstrong number"


if __name__ == "__main__":
    print(check_armstrong_number(number=1634))
