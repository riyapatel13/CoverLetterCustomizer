# CoverLetterCustomizer

This is a simple Python script that will customize cover letters for you. Given a cover letter template (in a txt format) and a list of companies to apply to (line-separated txt file), this script will create individual cover letters for each company and return a folder with all the letters in a PDF format.

## Installation and Setup

Before running this code, you will need to install some dependencies: [argparse](https://pypi.org/project/argparse/), [DateTime](https://pypi.org/project/DateTime/), [FPDF](https://pypi.org/project/fpdf/), and update os if necessary. See the links for installation instructions (in general, you can use ``` pip install <package>```). You will need to include a list of the companies you will be applying to in a .txt file with each company followed by a newline (see companies.txt for an example). In addition, you will need to have template of your cover letter saved as a .txt file with the following modifications:
 - Put [Date] wherever you want the date to go
 - Put [Company] wherever you want to insert the company name
 - Put [Full Name] wherever you want to fill in your name
 - Put [Position] wherever you want to insert the position you are applying for
 See sample_cover_letter_template.txt for an example (found at [this website](https://pyfpdf.readthedocs.io/en/latest/reference/FPDF/index.html)).

 ## Running Code

 Run the following:
 ```bash
    python3 cover_letter_customizer.py <companies_file> <template_path>
 ```
 - <companies_file>: .txt file containing line-separated list of companies
 - <template_path>: path to .txt file containing cover letter template

 On the command line, it will then ask you to type out your full name, position you're applying for, and the name of the folder to store the cover letters. After that, there will be a message indicating that the cover letters have been written.

