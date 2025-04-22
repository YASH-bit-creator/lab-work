with open(source_path, "rb") as src_file:#source_path is the relative path to the source file
    content = src_file.read()

with open(destination_path, "wb") as dst_file:
    dst_file.write(content)
print(f"File copied from '{source_path}' to '{destination_path}'")