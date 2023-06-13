def reverse_number(number: int):
    num = number
    reverse_num = 0
    while num != 0:
        num_mod = num % 10
        reverse_num = (reverse_num * 10) + num_mod
        num = num // 10
    return reverse_num


def check_palindrome(number: int):
    reverse = reverse_number(number)
    if number == reverse:
        return "Palindrome"
    else:
        return "Not a Palindrome"


if __name__ == "__main__":
    print(check_palindrome(number=121))

# git add learn_maths/02_reverse_number.py learn_maths/02_reverse_number.png
# git commit - m "added reverse_number files"
# git push origin learn_mathsD
