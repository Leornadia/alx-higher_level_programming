#!/usr/bin/python3

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <content>")
    else:
        file_path, content = sys.argv[1], sys.argv[2]
        write_to_file(file_path, content)

