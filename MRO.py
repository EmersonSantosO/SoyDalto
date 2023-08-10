class A():
    pass


class B(A):
    pass


class C(A):
    pass


class D(C, A):
    pass


class E(D, B):
    pass


class F(B, A):
    pass


class G(E, F):
    pass


print(G.mro())
