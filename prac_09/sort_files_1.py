"""Do from scratch exercise part 1 for prac_09."""
import os
import shutil


def main():
    """Sort files into subdirectories for each extension."""
    # Set working directory to new directory downloaded.
    os.chdir("FilesToSort")

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        # Get extension name
        extension_name = filename.split('.')[-1]
        # Try make a new directory with that name
        try:
            os.mkdir(extension_name)
        except FileExistsError:
            pass
        # Move files from current location to new location
        shutil.move(filename, extension_name)


main()
