from argon2 import PasswordHasher

ph = PasswordHasher()


password = "your admin password"

hash_password = ph.hash(password)

print(hash_password)
