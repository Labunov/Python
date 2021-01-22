class A:
    name = 'Bob'
    sex = 'men'
class B(A):
    age = 100

class C(B):
    pass

class D:
    name = 'Таня'
    age =18
    sex = 'w'

class Z(D,C):
    pass

print (Z.name)
c = C()
print (c.name)
