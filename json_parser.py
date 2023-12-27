import sys
import json

def parse_JSON(filename):
    types = [True, False, None]
    try:
        with open(filename, 'r') as file:
            json_file = json.load(file)
            if isinstance(json_file, dict):
                for key, val in json_file.items():
                    if isinstance(key, str) and not isinstance(val, str):
                        if val in types or isinstance(val, int) or isinstance(val, float) or isinstance(val, dict) or isinstance(val, list):
                            print(f'{filename} is a valid json')
                            return 0
                    if not isinstance(key, str) and not isinstance(val, str):
                        raise ValueError("Key and value must be str")
        print(f'{filename} is a valid json')
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