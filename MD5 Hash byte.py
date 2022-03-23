import hashlib

hasil = hashlib.md5(b'hidayat')

print("Hasil dalam bentuk MD5 : ", end="")
print(hasil.digest())
