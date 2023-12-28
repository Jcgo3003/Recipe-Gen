import sys
import re

def remove_timestamps(input_file):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        file_content = file.read()

    # Define the timestamp pattern using regex
    timestamp_pattern = r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}'

    # Replace the timestamp patterns with an empty string
    cleaned_content = re.sub(timestamp_pattern, '', file_content)

    # Reading lines
    lines = cleaned_content.splitlines()

    # Remove duplicates
    unique_lines = []

    for line in lines:
        if line not in unique_lines:
            unique_lines.append(line)

    # Create the output .txt file with the same name
    output_file = input_file[:-3] + 'txt'

    # Write the updated contents back to the file
    with open(output_file, 'w') as file:
        for line in unique_lines:
            file.write(str(line) + '\n')
    print(output_file)

if __name__ == '__main__':
    # Check if the input file is provided
    if len(sys.argv) < 2:
        print("Please provide the input file path.")
        print("Usage: python script.py input_file.str")
        sys.exit(1)

    # Get the input file from command line arguments
    input_file = sys.argv[1]

    # Call the remove_timestamps function with the provided file path
    remove_timestamps(input_file)
    # remove_duplicates(input_file)
    
