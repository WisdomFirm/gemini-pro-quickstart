import os
import google.generativeai as genai
from dotenv import load_dotenv  # <--- เพิ่มบรรทัดนี้

# Load environment variables from a .env file (if present)
load_dotenv() # <--- และเพิ่มบรรทัดนี้ก่อนเรียก os.environ

def generate_content(prompt, model_name='gemini-pro'):
 
    """
    Generates content using the specified Google Gemini model.

    Args:
        prompt (str): The prompt to send to the model.
        model_name (str, optional): The name of the model to use. Defaults to 'gemini-pro'.

    Returns:
        str: The generated text content, or an error message if something went wrong.
    """
    
    # Get API Key from environment variable for security
    api_key = os.environ.get('GOOGLE_API_KEY')
    
    if not api_key:
        return "Error: GOOGLE_API_KEY environment variable not set. Please set it before running."

    # Configure the library with your API key
    genai.configure(api_key=api_key)

    try:
        # Initialize the model
        model = genai.GenerativeModel(model_name)

        # Generate content
        response = model.generate_content(prompt)
        
        # Check for valid response text
        if response.text:
             return response.text
        else:
             return "Error: The model did not return any text."

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    
    # Example usage
    user_prompt = "Write a short, inspirational quote about learning and technology."

    print("--- Generating content with Gemini Pro ---")
    print(f"\nPrompt: {user_prompt}\n")
    
    generated_response = generate_content(user_prompt)

    print("Response:")
    print(generated_response)
    print("\n------------------------------------------")
