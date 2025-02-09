import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if length < 1:
        print("Password length must be at least 1.")
        return ""
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = generate_password(length, use_digits, use_special)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
