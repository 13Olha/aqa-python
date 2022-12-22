from random import randint

const_temp = 100_000

while True:

    var = int(input(" Fill number :"))

    if var == 1:
        print(f"initial value {var}")
        temp = var * const_temp
        data_string = f"new value {var + randint(0, 20 + 100)}"
        print(data_string)

    if var == 2:
        print(f"initial value {var}")
        temp = var * const_temp
        data_string = f"new value {var + randint(0, 20 + temp)}"
        print(data_string)

    if var == 3:
        print(f"initial value {var}")
        temp = var * const_temp
        data_string = f"new value {var + randint(0, 20) + temp}"
        print(data_string)

    if not var:
        break


print("end of program")
