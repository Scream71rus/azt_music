import os
from pbkdf2 import PBKDF2

password = "qwe123"

salt = 'fa8d5e095b12a0c5a3f81a54cdc03215'
password123 = '4197a9131b8f6f6d63f9d0ec0638c031'

hash_password = PBKDF2(password, salt).hexread(16)

print(hash_password == password123)