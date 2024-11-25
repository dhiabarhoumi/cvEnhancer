from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

def render_template(cv_data, template_file="cv_template.html"):
    """
    Renders the CV template with provided data.

    Args:
        cv_data (dict): Dictionary containing the CV content (e.g., sections, skills).
        template_file (str): The HTML template file name.

    Returns:
        str: Rendered HTML content as a string.
    """
    try:
        # Set up the Jinja2 environment
        template_dir = os.path.join(os.path.dirname(__file__), "templates")
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_file)

        # Render the template with the provided data
        return template.render(cv_data)
    except Exception as e:
        raise RuntimeError(f"Error rendering template: {e}")


def generate_pdf(html_content, output_file="updated_cv.pdf"):
    """
    Converts rendered HTML content into a PDF.

    Args:
        html_content (str): Rendered HTML content.
        output_file (str): File name for the generated PDF.

    Returns:
        str: Path to the generated PDF.
    """
    try:
        # Generate the PDF using WeasyPrint
        HTML(string=html_content).write_pdf(output_file)
        return output_file
    except Exception as e:
        raise RuntimeError(f"Error generating PDF: {e}")


def create_updated_cv(cv_data, output_file="updated_cv.pdf"):
    """
    Combines rendering and PDF generation to create the final CV.

    Args:
        cv_data (dict): Dictionary containing the CV content.
        output_file (str): File name for the generated PDF.

    Returns:
        str: Path to the generated PDF.
    """
    # Render the CV template
    html_content = render_template(cv_data)

    # Generate the PDF
    pdf_path = generate_pdf(html_content, output_file)
    return pdf_path
