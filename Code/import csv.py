filename = "text.txt"

# Load file content
with open(filename, "r") as f:
    file_content = f.read()

# Replace whitespace with single comma
file_content = ",".join(file_content.split())

# Write updated content back to file
with open(filename, "w") as f:
    f.write(file_content)