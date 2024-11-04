"""
python script to generate readme.md file based on these folder and their code
"""

import os
import re

FILE_NAME = "main.go"

def extract_number(folder_name):
    # Extracts the leading number from a folder name; defaults to 0 if no number is found.
    match = re.match(r'^(\d+)', folder_name)
    return int(match.group()) if match else float('inf')  # Non-numeric folders, if any, go last.

def append_hello_files_to_markdown(base_folder, markdown_file):
    # Clear existing content or create the file with prewritten text
    prewritten_text = "# Prewritten Content\nThis is the prewritten content in the markdown file."
    
    # Overwrite the markdown file with the prewritten text
    with open(markdown_file, 'w') as md_file:
        md_file.write(prewritten_text + "\n\n# Collected" + " " +FILE_NAME + " " + "Files Content\n")

    # List and sort the subfolders numerically
    subfolders = sorted(
        [f.path for f in os.scandir(base_folder) if f.is_dir()],
        key=lambda x: extract_number(os.path.basename(x))
    )
   

     # Traverse each sorted subfolder
    for subfolder in subfolders:
        go_file_path = os.path.join(subfolder, FILE_NAME)
        
        # Check if hello.txt exists in the subfolder
        if os.path.isfile(go_file_path):        
            # Read content of each hello.txt
            with open(go_file_path, 'r') as go_file:
                go_content = go_file.read()
                
            # Append content to the markdown file with a section header for each file
#             <details close>
# <summary><h2 style="display:inline;" id="toc">Table of Contents</h2></summary>

# [TOC]

# <small><i>Table of contents generated with <a href='https://github.com/luciopaiva/markdown-toc' target="_blank"><strong style="color: #3191ff; border-bottom: 2px solid #3191ff; border-radius: 0 0 2px 2px;"> markdown-toc</strong></a></i></small>
# </details>
            with open(markdown_file, 'a') as md_file:
                md_file.write(f"<details close>\n")
                md_file.write(f"<summary> { os.path.basename(subfolder) } </summary>\n")
                md_file.write(f"\n<h3 align=\"center\"> ⚡ {os.path.basename(subfolder)} </h3>\n")
                # md_file.write(f"<summary><h3> { os.path.basename(subfolder) } </h3></summary>\n")
                # md_file.write(f"\n<details close style=\" width: 100%; margin: 0 auto; padding: 6px 6px; background: #22272e; margin-bottom: 0.5rem; box-shadow: 0 0.1rem 1rem -0.5rem rgba(0, 0, 0, 0.4); border-radius: 5px; display: block; overflow-x: auto; \">\n")
                # md_file.write(f"\n## {os.path.basename(subfolder)}\n")
                # md_file.write(f"<summary><h2 style=\"display: inline; padding: 1rem; display: block; background: #22272e; padding-left: 2.2rem; position: relative; cursor: pointer; \"> { os.path.basename(subfolder) }</h2></summary>\n")
                
                md_file.write("\n" + "```go\n" + go_content + "```\n")
                md_file.write(f"</details>\n")
    
    print("Markdown file has been created or updated with content from hello.txt files.")



# Usage
base_folder = "./"  # The folder containing subfolders with main.go files+
markdown_file = "./README.md"  # The markdown file with prewritten text
append_hello_files_to_markdown(base_folder, markdown_file)
