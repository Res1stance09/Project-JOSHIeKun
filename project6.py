import random
import string

def get_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punct = string.punctuation

    all_char = lowercase + uppercase + digits + punct

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punct)
    ]

    password += random.choices(all_char, k=length - 4)

    random.shuffle(password)

    return "".join(password)

print_password = 8
random_password = get_password(print_password)
print(f"Generate Password : {random_password} ")