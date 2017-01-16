__author__ = 'Cameron Pickle'


def sum_divisors(number):
    i = 2
    sum_divs = 1
    while i < number:
        if number % i == 0:
            sum_divs += i
        i += 1
    return sum_divs


def perfect_number(number):
    if sum_divisors(number) > number:
        return "Abundant"
    elif sum_divisors(number) == number:
        return "Perfect"
    elif sum_divisors(number) < number:
        return "Deficient"

num_string = input("Input you number: ")
num = int(num_string)

print("Your number is ", perfect_number(num))