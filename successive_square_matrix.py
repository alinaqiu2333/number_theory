import numpy as np


def matrix_mod_n(F, n):
    m00 = F[0][0] % n
    m01 = F[0][1] % n
    m10 = F[1][0] % n
    m11 = F[1][1] % n
    m = np.array([[m00, m01], [m10, m11]])
    return m


def f_power_mod_n(k, n):
    print("calculate x to the power of", k, "mod", n)
    x = np.array([[1, 1], [1, 0]])
    f = x
    for i in range(k-1):
        f = f.dot(x)
        f = matrix_mod_n(f, n)
    return f


def f_power_k(k):
    print("calculate x to the power of", k)
    x = np.array([[1, 1], [1, 0]])
    f = x
    for i in range(k-1):
        print(f)
        f = f.dot(x)
    return f

power = [1, 2, 4, 8, 16, 32, 64, 128, 256]
print("k     x^k")
# for i in power:
#     print(i, f_power_k(i))
x_pow_2 = np.array([[1, 1], [1, 0]]).dot(np.array([[1, 1], [1, 0]]))
x_pow_4 = x_pow_2.dot(x_pow_2)
x_pow_8 = x_pow_4.dot(x_pow_4)
x_pow_16 = x_pow_8.dot(x_pow_8)
x_pow_32 = x_pow_16.dot(x_pow_16)
x_pow_64 = x_pow_32.dot(x_pow_32)
x_pow_128 = x_pow_64.dot(x_pow_64)
x_pow_256 = x_pow_128.dot(x_pow_128)
x_pow_300 = x_pow_256.dot(x_pow_32).dot(x_pow_8).dot(x_pow_4)
print(2,x_pow_2, x_pow_4, x_pow_8, x_pow_16, x_pow_32, x_pow_64, x_pow_128, x_pow_256 % 300, x_pow_300 % 300)


