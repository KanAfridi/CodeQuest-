import os

# Print the name of the project folder and its contents recursively
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



# To only open sub folders
def show_directory_structure(start_path):
    """Prints the immediate contents of the directory and one level deeper."""
    for item in os.listdir(start_path):
        item_path = os.path.join(start_path, item)
        print('|-- ' + item)
        if os.path.isdir(item_path):
            # List contents of the subdirectory
            for sub_item in os.listdir(item_path):
                print('  |-- ' + sub_item)

# Provide the correct path to your project folder
project_path = r'E:\documents\commited projects\Machine Learning\House-Price-Prediction-ML-Model\price-prediction-prac'  # Replace with your actual project path
print(f"|-- {os.path.basename(project_path)}/")
show_directory_structure(project_path)
