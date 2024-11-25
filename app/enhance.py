import openai

def initialize_openai(api_key):
    """
    Initializes OpenAI API with the provided API key.
    
    Args:
        api_key (str): Your OpenAI API key.
    """
    openai.api_key = api_key


def rewrite_cv_section(cv_text, missing_keywords, job_description):
    """
    Uses the LLM to rewrite or add sections to the CV to address missing keywords.
    
    Args:
        cv_text (str): Original CV text.
        missing_keywords (list): List of missing keywords to incorporate.
        job_description (str): Job description text for context.

    Returns:
        str: Enhanced CV text.
    """
    # Define the prompt for the LLM
    prompt = (
        f"Your task is to help improve a CV by integrating the following keywords: {', '.join(missing_keywords)}.\n"
        f"Here is the original CV:\n{cv_text}\n\n"
        f"And here is the job description for context:\n{job_description}\n\n"
        "Rewrite or add new sections to the CV that incorporate the missing keywords naturally and professionally."
    )
    
    try:
        # Query the LLM
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the desired LLM model
            messages=[
                {"role": "system", "content": "You are an expert in professional CV enhancement."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,  # Adjust based on expected response length
            temperature=0.7,  # Controls creativity; adjust as needed
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        raise RuntimeError(f"Error interacting with the LLM: {e}")


def generate_final_cv(cv_text, enhanced_sections):
    """
    Combines the original CV with the enhanced sections.
    
    Args:
        cv_text (str): Original CV text.
        enhanced_sections (str): Text with rewritten or added sections.

    Returns:
        str: Final enhanced CV text.
    """
    return f"{cv_text}\n\n### Enhanced Sections ###\n{enhanced_sections}"
