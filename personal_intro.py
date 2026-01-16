# Personal Introduction Program
# This program asks for user details and displays a friendly welcome message.

def main():
    print(" Welcome ")
    print("Please answer a few questions to get started:\n")

    # Taking inputs from the user
    name = input("What is your name? ")
    age = input("How old are you? ")
    hobby = input("What is your favorite hobby? ")
    location = input("Where are you from? ")

    # Displaying the friendly welcome message using f-strings
    print(f"\n Welcome, {name}! ")
    print(f"It's great to know that you are {age} years old.")
    print(f"Your hobby of '{hobby}' sounds amazing, especially for someone from {location}!")
    print("\nThank you for sharing! Happy coding!")

if __name__ == "__main__":
    main()