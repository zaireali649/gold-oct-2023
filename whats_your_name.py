def print_full_name(first: str, last: str) -> None:
    """
    Print a greeting message with the full name.

    Args:
        first (str): The first name.
        last (str): The last name.
    """
    # Print a formatted greeting message using the provided first and last names
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    # Read user input for the first name and store it in 'first_name'
    first_name = input("Enter your first name: ")
    
    # Read user input for the last name and store it in 'last_name'
    last_name = input("Enter your last name: ")
    
    # Call the 'print_full_name' function with 'first_name' and 'last_name'
    # to print a greeting message
    print_full_name(first_name, last_name)
