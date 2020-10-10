class A:
    def __init__(self):
        print('begin')
        self.a1()
        self.a2()
        self.a3()

    def a1(self):
        print('a1')
        print('a1')

    def a2(self):
        print('a2')

    def a3(self):
        print('a3')


a = A()

# begin
# a1
# a1
# a2
# a3


class B(A):
    def __init__(self):
        super(B, self).__init__()

    def a2(self):
        print('a2')
        print('a2')


b = B()

# begin
# a1
# a1
# a2
# a2
# a3


class C(A):
    def __init__(self):
        super(C, self).__init__()

    def a3(self):
        print('a3')
        print('a3')


c = C()

# begin
# a1
# a1
# a2
# a3
# a3


class D(B, C):
    def __init__(self):
        super(D, self).__init__()


d = D()

# begin
# a1
# a1
# a2
# a2
# a3
# a3


class E(A):
    def __init__(self):
        super(E, self).__init__()
        self.x = 1

    def a2(self):
        print('a2')
        print('a2')
        self.x = 2

    def a3(self):
        print('a3')
        print('a3')
        self.x = 3


e = E()
print(e.x)
e.a2()
print(e.x)
# begin
# a1
# a1
# a2
# a2
# a3
# a3
# 1
# a2
# a2
# 2
