headings = 0
figures = 0
tables = 0

with open("sample.txt", "r") as file:
    for line in file:
        clean_line = line.lower().strip() # what lower will do is change every word to lower 

        if clean_line.startswith("heading"):
            headings += 1
        if clean_line.startswith("figure"):
            figures += 1
        if clean_line.startswith("table"):
            tables += 1

print(f"Headings: {headings}")
print(f"Figures: {figures}")
print(f"Tables: {tables}")
 