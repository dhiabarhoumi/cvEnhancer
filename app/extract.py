import os
from PyPDF2 import PdfReader
from pylatexenc.latex2text import LatexNodes2Text

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.
    
    Args:
        file_path (str): Path to the PDF file.
        
    Returns:
        str: Extracted text from the PDF.
    """
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        raise RuntimeError(f"Error reading PDF file: {e}")


def extract_text_from_latex(file_path):
    """
    Extracts text from a LaTeX file.
    
    Args:
        file_path (str): Path to the LaTeX file.
        
    Returns:
        str: Extracted plain text from the LaTeX content.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            latex_code = f.read()
        latex_text = LatexNodes2Text().latex_to_text(latex_code)
        return latex_text
    except Exception as e:
        raise RuntimeError(f"Error reading LaTeX file: {e}")


def read_job_description(file_path):
    """
    Reads the job description from a text or PDF file.
    
    Args:
        file_path (str): Path to the job description file.
        
    Returns:
        str: The job description as plain text.
    """
    try:
        file_extension = os.path.splitext(file_path)[-1].lower()
        if file_extension == '.pdf':
            return extract_text_from_pdf(file_path)
        elif file_extension in ['.txt', '.md']:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            raise ValueError("Unsupported file format for job description. Use .pdf, .txt, or .md.")
    except Exception as e:
        raise RuntimeError(f"Error reading job description file: {e}")
