import random
import string

def generate_password(length):
    # Define the character set to the use of the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # passowrd generator a random
    password = " ".join(random.choice(characters) for i in range(length))

    return password

def main():
    try:
        length = int(input("Enter the desire length of the password: "))
        if length <= 0:
            print(" please enter the correrct integer for the password .")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
     
    # Generate the password
    password = generate_password(length)
    
     # Display the genertated password.
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
