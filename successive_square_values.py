powers = [0, 4, 6, 7, 9]
print("k 52^(2^k) mod 1917")
for i in powers:
    print(i, pow(52, (2**i)) % 1917)
