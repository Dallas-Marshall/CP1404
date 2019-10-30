"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        get_fixed_filename(filename)
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # Split filename from .txt identifier
    separated_name = filename.split('.')
    # Break separated_name into its characters in a list
    separated_name_letters = [letter for letter in separated_name[0]]
    # Ensure letters following a space are capitalised.
    fixed_name = ""
    for i, letter in enumerate(separated_name_letters):
        if letter.isupper():
            fixed_name += letter
        elif separated_name_letters[i - 1] == " ":
            fixed_name += letter.upper()
        else:
            fixed_name += letter
    separated_name[0] = fixed_name
    # TODO cannot figure out how to handle (_Hillsong)
    new_name = ""
    for i, character in enumerate(separated_name[0]):
        # Remove spaces will be replaced with underscore in next step
        if character == " ":
            new_name += ""
        elif character.isupper():
            # Only add underscore before if the capital letter is not the first letter
            if i > 0:
                new_name += "_{}".format(character)
            else:
                new_name += character
        else:
            new_name += character
    return new_name + ".txt"


main()
