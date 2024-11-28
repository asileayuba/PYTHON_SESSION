def read_and_write_file():
    try:
        # Prompt the user for the input filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Ask for the output filename
        output_filename = input("Enter the name of the file to write to: ")

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file you specified does not exist. Please try again.")
    except IOError:
        print("Error: An error occurred while reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_write_file()
