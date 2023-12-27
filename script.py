import sys
import json

def parse_JSON(filename):
    try:
        with open(filename, 'r') as file:
            json_file = json.load(file)
        print(f'{filename} is a vilid json')
        return 0
    except json.JSONDecodeError as err:
        print(f'Error parsing {filename}: {err}')
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)  # Exit code 1 for incorrect usage

    file_path = sys.argv[1]
    exit_code = parse_JSON(file_path)
    sys.exit(exit_code)