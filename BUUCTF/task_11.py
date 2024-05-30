from Crypto.Util.number import *
import gmpy2
from flag import flag

def gen_prime(number):
    p = getPrime(number//2)
    q = getPrime(number//2)
    return p, q

m = bytes_to_long(flag.encode())
p, q = gen_prime(1024)

n = p * q
e = 65537
d = gmpy2.invert(e, (p-1) * (q-1))

ciphertext = pow(m, e, n)
decrypted_message = pow(ciphertext, d, n)

# 将解密后的明文转换为字节并解码
decrypted_flag = long_to_bytes(decrypted_message).decode()

print("Decrypted flag:", decrypted_flag)