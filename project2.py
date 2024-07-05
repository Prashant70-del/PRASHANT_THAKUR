import random
import string

def generate_password(length):
    # Define The character set to the use for the password.
    characters= string.ascii_letters + string.digits + string.punctuation
    # passowrd generator a random
    password= "".join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length= int(input("enter the desired length of the password"))
        if length <= 0:
            raise ValueError("password length must be greater than 0")
          # Generate the password
        password= generate_password(length)

        # Display the genertated password.
        print(f"Generated password:", {password})
    except ValueError as e:
        print(f"error:{e}")

if __name__ == "__main__":
    main()