#Loops with Lists

# First we create a list
topics = ["Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision"]

# Using for loop through the list 
print("--- Course Syllabus ---")
for topic in topics:
    print(f"Learning: {topic}")

# Now while loop to count down
print("\n--- Countdown to Launch ---")
count = 5
while count > 0:
    print(count)
    count -= 1

