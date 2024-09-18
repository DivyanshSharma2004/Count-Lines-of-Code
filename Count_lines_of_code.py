import os

def count_lines(directory, extensions):
    # Initialize dictionaries to hold counts for each extension and each file
    total_lines = {ext: 0 for ext in extensions}
    file_counts = {ext: {} for ext in extensions}
    
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file has one of the specified extensions
            for ext in extensions:
                if file.endswith(ext):
                    file_path = os.path.join(root, file)
                    # Count lines in the file
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        line_count = sum(1 for line in f)
                        total_lines[ext] += line_count
                        file_counts[ext][file_path] = line_count
    
    return total_lines, file_counts

# Corrected paths with escaped backslashes or raw strings
directory2 = r'Your File Path Here'
extensions = ['.html', '.css', '.js', '.java', '.py','.json','.txt']  # List of file extensions to count

# Count lines and print results
total_lines, file_counts = count_lines(directory2, extensions)

print(f"Total lines of code in project:")
for ext in extensions:
    print(f"\n{ext} files:")
    if ext in total_lines:
        print(f"Total lines: {total_lines[ext]}")
        for file_path, count in file_counts[ext].items():
            print(f"{file_path}: {count} lines")
    else:
        print("No files found.")