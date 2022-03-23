import hashlib

str = "Hidayat"

hasil = hashlib.md5(str.encode())

print("Hasil dalam bentuk MD5 :", end="")
print(hasil.hexdigest())
