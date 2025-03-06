import random
import string

n=int(input("Enter the desired length of password : "))

def generate_password(length=n):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(f"Generated Password with length {n} is :", generate_password())
