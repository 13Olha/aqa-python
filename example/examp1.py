def print_first_name(first_name):
    print(first_name)


def print_last_name(last_name):
    print(last_name)


def print_full_name(first_name, last_name):
    print_first_name(first_name)
    print_last_name(last_name)


print_full_name('John', 'Doe')


def sum_two_numbers(num1, num2):
    return num1 + num2


def sum_multiply_by_two(sum_func, num1, num2):
    def wrapper():
        return sum_func(num1, num2) * 2
    return wrapper()


print(sum_multiply_by_two(sum_two_numbers, 1, 2))