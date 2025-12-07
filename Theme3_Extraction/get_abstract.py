import fitz  # PyMuPDF

def cut_out_abstract():
    filename = "sample.pdf"
    
    try:
        # 1. Get the raw text (Just like before)
        doc = fitz.open(filename)
        page = doc.load_page(0)
        raw_text = page.get_text()
        
        # 2. Find the Markers
        # We look for "Abstract" to start the cut
        start_marker = "Abstract"
        # We look for "1." or "Introduction" to stop the cut
        end_marker = "Introduction"
        
        start_index = raw_text.find(start_marker)
        end_index = raw_text.find(end_marker)
        
        # 3. Validation (Did we find them?)
        if start_index == -1 or end_index == -1:
            print("❌ Could not find markers. The PDF text might look different than expected.")
            return

        # 4. The Surgery (Slicing)
        # We capture from start_index up to end_index
        abstract_content = raw_text[start_index : end_index]
        
        # 5. Clean and Print
        print("\n--- 🎯 THE SURGICAL EXTRACTION ---")
        print(abstract_content.strip()) # .strip() removes extra whitespace
        print("----------------------------------")
        
        # 6. Save it
        with open("abstract_only.txt", "w") as f:
            f.write(abstract_content.strip())
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    cut_out_abstract()