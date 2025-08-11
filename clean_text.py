# clean_text.py

# Extracts license information from English-Turkish sentence pairs in the file.
# Extracts only the first two columns and creates a new clean file.

data_path = "tur.txt"

cleaned_lines = []

with open(data_path, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) >= 2:
            cleaned_lines.append(parts[0] + "\t" + parts[1])

with open("tur_clean.txt", "w", encoding="utf-8") as f:
    for line in cleaned_lines:
        f.write(line + "\n")

print("The file was successfully cleaned and saved as 'tur_clean.txt'.")
