import os

def show_directory_structure(start_path, indent=0):
    """Recursively prints the directory structure."""
    for item in os.listdir(start_path):
        item_path = os.path.join(start_path, item)
        print('  ' * indent + '|-- ' + item)
        if os.path.isdir(item_path):
            show_directory_structure(item_path, indent + 1)

# Provide the correct path to your project folder
project_path = r'Your folder path'  # Replace with your actual project path
print(f"|-- {os.path.basename(project_path)}/")
show_directory_structure(project_path)