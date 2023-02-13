class A:

    def __init__(self, value):
        self.value_a = 20
    a_property = 1


class B:
    b_property = 2


class C (A, B):
    def __init__(self, value):
        super().__init__(value + 10)
        self.value = value
    c_property = 3


inst = C(10)


print(inst.a_property, inst.c_property, inst.b_property, inst.value, inst.value_a)
