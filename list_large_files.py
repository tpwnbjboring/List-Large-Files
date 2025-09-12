import os

def list_large_files(directory, size_threshold_mb=1):
    size_threshold_bytes = size_threshold_mb * 1024 * 1024
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                filesize = os.path.getsize(filepath)
                if filesize > size_threshold_bytes:
                    print(f"{filepath} - {filesize / (1024 * 1024):.2f} MB")
            except OSError as e:
                print(f"Error accessing {filepath}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python list_large_files.py <directory>")
    else:
        list_large_files(sys.argv[1])
