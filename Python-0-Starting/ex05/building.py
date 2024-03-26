import sys


def main():
     """
    Count the occurrences of different character types in a given text input.

    If provided with a command-line argument, counts the occurrences of character types in the argument string.
    If more than one argument is provided to the program, to programm print an AssertionError.
    If None or nothing is provided, the user is prompted to provide a string.
    
    Character types counted:
    - Upper letters
    - Lower letters
    - Punctuation marks
    - Spaces
    - Digits
    
    Prints the total number of characters in the input and the counts of each character type.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) < 2:
            try:
                user_input = input("What is the text to count?\n")
            except EOFError:
                pass
        else:
            user_input = sys.argv[1]

        user_input += '\n'
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        punct_sum = sum(1 for char in user_input if char in punctuation)

        sums = {
            'upper letters': sum(1 for char in user_input if char.isupper()),
            'lower letters': sum(1 for char in user_input if char.islower()),
            'punctuation marks': punct_sum,
            'spaces': sum(1 for char in user_input if char.isspace()),
            'digits': sum(1 for char in user_input if char.isdigit())
        }

        print(f"The text contains {len(user_input)} characters:")
        for char_type, count in sums.items():
            print(f"{count}: {count}")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
