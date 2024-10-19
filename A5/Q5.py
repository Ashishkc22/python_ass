def reverse_file_content():
    with open('input.txt', 'r') as infile:
        content = infile.read()
    with open('reversed.txt', 'w') as outfile:
        outfile.write(content[::-1])

reverse_file_content()