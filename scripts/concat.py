import os
import sys
import pyperclip

ignored_folders = ["venv", "migrations", ".git", ".idea", "__pycache__", '.vscode','.idea']

# Function to create a directory tree structure as a string
def create_directory_tree(directory_path, prefix=""):
    tree_str = ""
    for root, dirs, files in os.walk(directory_path):
        # Skip the "venv" directory
        dirs[:] = [d for d in dirs if d not in ignored_folders]
        
        # Display the current directory in the tree
        level = root.replace(directory_path, "").count(os.sep)
        indent = ' ' * 4 * level
        tree_str += f"{indent}{os.path.basename(root)}/\n"
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            tree_str += f"{sub_indent}{f}\n"
    return tree_str

def concatenate_files_in_directory(directory_path):
    giant_string = ""

    # Traverse the directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        # Skip the "venv" directory
        dirs[:] = [d for d in dirs if d not in ignored_folders]

        for file_name in files:
            # Skip image files
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.DS_Store', '.pyc', 'ipynb')):
                print(f"Skipping file: {file_name}")
                continue

            if file_name == ".DS_Store":
                continue

            file_path = os.path.join(root, file_name)
            # Prepend the directory structure to the file name in the string
            relative_path = os.path.relpath(file_path, directory_path)
            print(f"Processing file: {relative_path}")
            giant_string += f"##################################\n"
            giant_string += f"### File: {relative_path}\n"
            giant_string += f"##################################\n"
            try:
                # Append file contents to the giant string
                with open(file_path, 'r', encoding='utf-8') as file:
                    contents = file.read()
                    giant_string += contents + "\n\n"  # Add an extra newline for separation
            except Exception as e:
                # Handle exceptions for reading files
                print(f"Could not read file {file_path}: {e}")
    return giant_string

# Check if a directory path is passed as a command-line argument
directory_path = sys.argv[1] if len(sys.argv) > 1 else "."

# Set the output file path to be in the same directory
output_file_path = os.path.join(directory_path, "code.txt")

# Delete code.txt if it exists
if os.path.exists(output_file_path):
    os.remove(output_file_path)
    print(f"{output_file_path} deleted.")

# Create the directory tree diagram
directory_tree = create_directory_tree(directory_path)

# Get the concatenated result string
result_string = concatenate_files_in_directory(directory_path)

# Save the directory tree and concatenated file contents to a file named "code.txt"
if result_string.strip():  # Check if the string is not empty
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        # Write the directory tree first
        output_file.write("### Directory Tree Structure ###\n")
        output_file.write(directory_tree)
        output_file.write("\n### Concatenated Files Content ###\n\n")
        # Write the concatenated file contents
        output_file.write(result_string)
    print(f"Giant string saved to {output_file_path}")
    
    # Read the saved file and copy its contents to the clipboard
    with open(output_file_path, "r", encoding="utf-8") as output_file:
        file_contents = output_file.read()
        pyperclip.copy(file_contents)
        print(f"Contents of {output_file_path} copied to clipboard")
else:
    print("No files were processed, code.txt was not written.")
