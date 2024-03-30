def gcd(a, b):
    x, y = a, b
    while y != 0:
        # r = x % y
        # x = y
        # y = r
        x, y = y, x % y
    return x


def gcd_rec(a, b):
    if b == 0:
        return a
    return gcd_rec(b, a % b)


print(gcd(287, 91))
