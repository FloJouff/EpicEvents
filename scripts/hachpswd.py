from argon2 import PasswordHasher

ph = PasswordHasher()


password = "erineetnathan"

hash_password = ph.hash(password)

print(hash_password)
