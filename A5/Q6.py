def copy_file_content():
    source_file = input("Enter the source file name: ")
    dest_file = input("Enter the destination file name: ")
    
    with open(source_file, 'r') as src:
        content = src.read()
    
    with open(dest_file, 'w') as dest:
        dest.write(content)
    
    print(f"Copied content from {source_file} to {dest_file}.")