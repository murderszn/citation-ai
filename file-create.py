import os
import re

def extract_and_save_html(file_path):
    try:
        # Read the content of the input file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"File content length: {len(content)}")  # Debug print

        # Define the output directory
        output_directory = os.path.dirname(file_path)
        print(f"Output directory: {output_directory}")  # Debug print

        # Modified regex pattern to be more flexible with whitespace
        html_blocks = re.findall(r'###\s*(.*?)\s*\n\s*```html\s*\n(.*?)\n\s*```', content, re.DOTALL)
        
        # Debug print
        print(f"Found {len(html_blocks)} HTML blocks")

        if not html_blocks:
            print("No HTML blocks found in the file.")
            print("Content sample:", content[:200])  # Show start of file for debugging
            return

        # Save each HTML block as a separate file
        for page_title, html_content in html_blocks:
            # Create a valid filename from the page title
            filename = f"{page_title.lower().replace(' ', '_').replace('/', '_')}.html"
            output_file_path = os.path.join(output_directory, filename)

            # Write the HTML content to the file
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(html_content)
            print(f"Generated file: {output_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path to the file containing HTML sections
    input_file_path = r"C:\Users\jjohn\Desktop\Web Page\ai-workflow\output.txt"

    # Run the extraction and file generation
    extract_and_save_html(input_file_path)
