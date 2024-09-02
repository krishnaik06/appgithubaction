import os

def generate_readme():


     # Sample content generation
    content = """# My Python Project

This README file is automatically generated.

## Modules

Below are the available modules in this project:

"""
   # Iterate through Python files in the `src` directory
    for root, dirs, files in os.walk('src'):
        for file in files:
            if file.endswith('.py'):
                module_name = file[:-3]
                content += f"- **{module_name}**: Module description goes here.\n"

    content += "\n## Usage\n\nInstructions on how to use the modules."

    # Write the generated content to README.md
    with open('README.md', 'w') as readme_file:
        readme_file.write(content)

if __name__ == "__main__":
    generate_readme()