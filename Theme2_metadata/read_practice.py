import json

with open("paper_metadata.json" , "r") as f:
    saved_data = json.load(f)
    print(saved_data["author"])