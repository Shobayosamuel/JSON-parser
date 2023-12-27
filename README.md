# JSON Parser

This is a simple command-line JSON parser written in Python that validates and parses JSON files. The parser checks for a basic JSON object containing string keys and string values.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Shobayosamuel/JSON-parser.git
    ```

2. Navigate to the project directory:

    ```bash
    cd JSON-parser
    ```

### Usage

To use the JSON parser, run the `json_parser.py` script with the path to the JSON file as a command-line argument:

```bash
python json_parser.py path/to/your/file.json
```

### Test
```
python json_parser.py tests/step2/valid.json
Output: File 'tests/step2/valid.json' is a valid JSON with string keys and values.
```