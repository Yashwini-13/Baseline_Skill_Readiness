with open("sample.txt", "r") as file:
    text = file.read()

#Split into words
words = text.split()

# This is a list comprehension - a quick loop inside a list
clean_words = [word.strip(".,!?") for word in words]

#  Sort by length (Big to Small) reverse
sorted_words = sorted(clean_words, key=len, reverse=True)

#Slice the list to get the first 5
top_5 = sorted_words[:5]

print("Top 5 Longest Words:")
for w in top_5:
    print(w)
