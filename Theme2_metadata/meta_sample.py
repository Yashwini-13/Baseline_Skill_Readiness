import json 

paper_metadata = {
    "title": "Learning Path",
    "author": "Yashwini",
    "year": 2025,
    "page_count": 12,
    "is_published": True,
}

with open("paper_metadata.json","w") as f:
    json.dump(paper_metadata , f , indent=4)