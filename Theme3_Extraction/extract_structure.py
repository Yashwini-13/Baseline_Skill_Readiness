import fitz  # PyMuPDF
from collections import Counter

def analyze_pdf_structure(filename):
    doc = fitz.open(filename)
    
    # 1. GATHER FONT SIZES
    # We need to know what "Normal" looks like before we can find "Big"
    font_counts = Counter()
    
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:  # Loop through text blocks
            if "lines" in b:
                for line in b["lines"]:
                    for span in line["spans"]:
                        # Round size to nearest integer to avoid 11.999 vs 12.0
                        size = round(span["size"])
                        font_counts[size] += 1

    # The most common size is usually the "Body Text"
    common_size = font_counts.most_common(1)[0][0]
    print(f"📊 ANALYSIS: The body text is Size {common_size}")
    print(f"--------------------------------------------------")

    # 2. EXTRACT BASED ON RULES
    headings = []
    captions = []
    
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for line in b["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        size = round(span["size"])
                        
                        if len(text) < 3: continue # Skip junk
                        
                        # RULE A: HEADINGS (Bigger than body text)
                        if size > common_size:
                            headings.append(f"Page {page_num+1}: {text} (Size {size})")
                            
                        # RULE B: CAPTIONS (Starts with 'Fig' or 'Table')
                        elif text.startswith("Fig") or text.startswith("Table"):
                            captions.append(f"Page {page_num+1}: {text}")

    # 3. REPORT
    print("\n🔹 FOUND HEADINGS:")
    for h in headings:
        print(h)
        
    print("\n🔹 FOUND CAPTIONS:")
    for c in captions:
        print(c)

if __name__ == "__main__":
    analyze_pdf_structure("sample.pdf")