"""Do from scratch exercise part 2 for prac_09."""
import os
import shutil


def main():
    """Sort files into subdirectories for each extension based on user preference."""
    # The following dictionary will allow us to map extensions to the destination folder names
    extension_name_to_directory_name = {}

    # Set working directory
    os.chdir("FilesToSort")

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        # Get extension name
        extension_name = filename.split('.')[-1]

        # If not already asked, ask user what directory that they want files with this extension in
        if extension_name not in extension_name_to_directory_name:
            directory_name = input("What category would you like to sort {} files into? ".format(extension_name))

            # Create dictionary entry linking users directory name to the current extension
            extension_name_to_directory_name[extension_name] = directory_name

            # Try make directory for the file
            try:
                os.mkdir(directory_name)
            except FileExistsError:
                pass

        # Move files from current location to new location
        shutil.move(filename, extension_name_to_directory_name[extension_name])


main()
