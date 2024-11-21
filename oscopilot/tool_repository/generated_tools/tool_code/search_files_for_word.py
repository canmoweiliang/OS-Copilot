def search_files_for_word(directory, word):
    """
    Search through each text file in the specified directory to check if they contain the specified word.
    List all file names that match this criterion.

    Args:
    directory (str): The path to the directory containing the text files.
    word (str): The word to search for in the text files.

    Returns:
    list: A list of filenames where the word is found.
    """
    import os

    # List to hold filenames that contain the specified word
    matching_files = []

    # Iterate through files in the specified directory
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file and has a .txt extension
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Check if the word is in the file content
                if word in content:
                    matching_files.append(filename)

    return matching_files