import random


data = [0, 2, 3, 3, 3, 0, 7, 7, 7, 7, 0, 3]

for idn, item in enumerate(data):
    if not item:
        data.pop(idn)
        if item == 3:
            data.append(random.randint(0, 9))


print(data)


data = [1, 1]
example = enumerate(data)


print(next(example))

data.insert(0, 33)

print(next(example))

print(next(example))

print(next(example))