# List Large Files

A simple Python script to list all files in a directory (and its subdirectories) that are larger than 1MB.

## Usage

1. **Clone or download this script.**
2. Run the script from the command line:

    ```bash
    python list_large_files.py <directory_path>
    ```

    - Replace `<directory_path>` with the path of the directory you want to scan.

## Example

```bash
python list_large_files.py /path/to/your/directory
```

This will output all files larger than 1MB found in `/path/to/your/directory` and its subdirectories, showing their full path and size in MB.

## Notes

- You can change the size threshold by editing the `size_threshold_mb` argument in the script.
- Handles inaccessible files gracefully and prints an error message if a file cannot be accessed.

## Requirements

- Python 3.x

No external dependencies required.
