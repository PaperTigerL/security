from Crypto.Util.number import long_to_bytes

# 已知的值
n = 201354090531918389422241515534761536573
e = 2
c = 20442989381348880630046435751193745753


# 因数分解n以获得p和q
def factorize(n: object) -> object:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None


# 尝试因数分解n
factors = factorize(n)

if factors:
    p, q = factors
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)  # 计算d，即私钥的指数

    # 使用RSA的解密算法，计算明文m
    m = pow(c, d, n)

    # 将长整数m转换为字节串，获取flag
    flag = long_to_bytes(m)
    print('Decrypted flag:', flag.decode())
else:
    print('Failed to factorize n. RSA decryption is not possible.')
