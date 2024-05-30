from PIL import Image
from itertools import cycle
# 解密函数
def xor(data, key):
    return bytearray(a ^ b for a, b in zip(data, cycle(key)))

# 从已知的加密文件头部提取的信息
encrypted_header = bytearray([0x89, 0x50, 0x4E, 0x4A, 0x44, 0x42, 0x5E, 0x58])

# 正确的PNG文件头
png_header = bytearray([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

# 计算密钥
key = xor(encrypted_header, png_header)
print("推测的密钥(16进制):", key.hex())

# 现在，我们可以尝试用这个密钥来解密整个文件
with open('enc.txt', 'rb') as file:
    encrypted_data = file.read()

# 使用计算出的密钥解密数据
decrypted_data = xor(encrypted_data, key)

# 检查PNG头是否正确解密
if decrypted_data.startswith(png_header):
    print("密钥正确，文件头部已正确解密。")
    with open('original.png', 'wb') as output_file:
        output_file.write(decrypted_data)
else:
    print("密钥错误或文件不是PNG格式。")