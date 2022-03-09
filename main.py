import random
import string

if __name__ == '__main__':
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    chars = lower + upper + digits + symbols
    password_len = int(input("Enter password length: "))
    password = "".join(random.sample(chars, password_len))
    print(f"Password is {password}")