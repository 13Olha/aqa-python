from random import randint

print("start")

var = 123
const_temp = 100
data = []

def print_random():
    # print(f"initial value {var}")
    temp = var * const_temp
    data_string = f"new value {var + randint(0, 20 + temp)}"
    data.append(data_string)
    # print(data_string)
    return f"initial value {var} , {data_string}"


var_1 = print_random

print(f"{data=}")

# print(f"{var_1=}")

print("the end")




from random import randint


VAR = 123
CONST_TEMP = 100
data = []


def print_random(value, additional_var=12, var=VAR) -> tuple or None:
    """
    This function generate some values

    """
    temp = var * additional_var
    data_string = f"new value {var + randint(0, 20 + temp)}"
    data.append(data_string)
    for ni in range(10):
        print(f"iteration {ni}")
        for i in range(10):
            print(f"second iteration {i} {ni}")
            if additional_var == i:
                return
    print(data, value)
    return f"initial value {var} , {data_string} {additional_var=}", value




v = print_random

