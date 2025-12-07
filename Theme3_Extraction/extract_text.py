import fitz 

def extract_raw_text():
    filename = "sample.pdf"

    try:
        doc = fitz.open(filename)
        print(f"Opened successfully:{filename}")

        page = doc.load_page(0)
        text = page.get_text()

        print("--Extracted text below--")
        print(text)
        print("------------------")
    
    except Exception as e:
        print(f"Error:{e}")

if __name__ == "__main__":
    extract_raw_text()