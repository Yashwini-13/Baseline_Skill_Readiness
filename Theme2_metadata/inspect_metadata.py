import json 

paper_facts = {
    "title": "Mineralogy and geochemistry of iron tailings from Yeshan iron Deposit",
    "filename": "Sample paper.pdf",
    "authors": [
        "Gang Yang", 
        "Quanmin Xie", 
        "Yidi Li", 
        "Ranjith Kumar Easwaran",
        "Fang Liu",
        "Mei Yang"
    ],
    "keywords": [
        "tailings wastes", 
        "mineralogy", 
        "geochemistry", 
        "spatial distribution", 
        "potential utilization"
    ],
    "year": 2023, 
    "page_count": 15,
    "doi": "N/A",
    "license": "Copyright (Assumed)",
    "subject": "Geology / Mining Engineering",
    "is_verified": True
}

op_filename = "output.json"

with open(op_filename , "w") as f:
    json.dump(paper_facts,f,indent=4)

print("Saved to",op_filename)