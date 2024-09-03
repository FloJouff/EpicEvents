from argon2 import PasswordHasher

ph = PasswordHasher()


password = "adminpassword"

hash_password = ph.hash(password)

print(hash_password)
