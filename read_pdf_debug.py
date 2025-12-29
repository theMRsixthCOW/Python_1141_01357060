
import sys
import importlib.util

def check_install(package):
    if importlib.util.find_spec(package) is None:
        print(f"{package} not found")
        return False
    return True

try:
    from pypdf import PdfReader
    reader = PdfReader("d:\\py\\theMRsixthCOW\\Python HW12.pdf")
    print("--- PDF Content ---")
    for page in reader.pages:
        print(page.extract_text())
except ImportError:
    print("pypdf not installed, trying PyPDF2")
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader("d:\\py\\theMRsixthCOW\\Python HW12.pdf")
        print("--- PDF Content ---")
        for page in reader.pages:
            print(page.extract_text())
    except ImportError:
        print("PyPDF2 not installed")
