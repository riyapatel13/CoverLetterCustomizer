import argparse
import PyPDF2
from datetime import date
from fpdf import FPDF
import os

def list_companies(input_file):
    companies = []
    with open(input_file,"r") as text:
        lines = text.readlines()
    
    for line in lines:
        companies.append(line.strip())
  
    return companies

# didn't know how to change the encoding for PDF to latin-1, so it wasn't recognizing certain characters
'''
def pdf_to_string(template_path):
    pdfFileObj = open(template_path, 'rb') 
    template_pdf = PdfFileReader(pdfFileObj)
    template_text = ""

    for page in template_pdf.pages:
        template_text += page.extractText()

    pdfFileObj.close()
    return template_text
'''

# needs to be latin-1 format
def txt_to_string(template_path):
    with open(template_path, 'rb') as fh:
        txt = fh.read().decode('latin-1')
    return txt

def date_str():
    cur_date = date.today()
    months = [None, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    date_str = f"{months[cur_date.month]} {cur_date.day}, {cur_date.year}"
    return date_str

# if newline, return None. else create directory if it doesn't exist
def setup_dir(dir_name):
    print(dir_name)
    if dir_name == '': 
        dir_name = None
    else:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
    return dir_name

# customizes pdf and returns path to cover letter
def customize_pdf(template, date, company, name, position, cover_letter_dir):
    # customize string
    template = template.replace("[Date]", date)
    template = template.replace("[Company]", company)
    template = template.replace("[Full Name]", name)
    template = template.replace("[Position]", position)
    # write to pdf
    pdf = FPDF('P','in','Letter')
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(0, 0.25, template)

    if cover_letter_dir != None:
        cover_letter_name = f'{cover_letter_dir}/{company}_cover_letter.pdf'
    else: cover_letter_name = f'{company}_cover_letter.pdf'

    pdf.output(cover_letter_name, 'F').encode("latin-1")

    return cover_letter_name

def merge_pdf(letter_path, resume_path, cover_letter_dir):
    merger = PyPDF2.PdfFileMerger()
    merger.append(letter_path)
    merger.append(resume_path)

    # naming the file
    if cover_letter_dir != None:
        file_name = f'{cover_letter_dir}/{company}_cover_letter_resume_merged.pdf'
    else: file_name = f'{company}_cover_letter_resume_merged.pdf'

    merger.write(file_name)
    merger.close()


if __name__ == "__main__":
    
    argparser = argparse.ArgumentParser(description = "Cover Letter Customizer - Given a list of companies you want to apply to (line-separated txt file) and a cover letter template (txt), this file will create a folder with customized cover letters for each company.")
    argparser.add_argument("template_path",
                        type=str,
                        help="path to txt of the template")
    argparser.add_argument("--companies_file",
                        type=str,
                        default=None,
                        help="optional txt file containing company names (line-separated)")

    # collecting info
    args = argparser.parse_args()
    cur_date = date_str()
    tem = txt_to_string(args.template_path)
    name = input("Please enter your FULL NAME:\n")
    position = input("Please enter the position you are applying for:\n")
    # additional input for single letter
    if args.companies_file is None:
        company = input("Please enter company you are applying to:\n")

    cover_letter_dir = input("Please enter a folder name to save all the cover letters (Optional - hit Enter for no folder):\n")
    cover_letter_dir = setup_dir(cover_letter_dir)
    merge = input("Would you like to merge your cover letter with your resume (Y/N)?\n")

    if merge == 'Y': merge = True
    else: merge = False

    if merge:
        resume_path = input("Type in the relative path of your resume:\n")

    if args.companies_file is None:
        cover_letter_path = customize_pdf(tem, cur_date, company, name, position, cover_letter_dir)
        print(cover_letter_path)
        print(resume_path)
        if merge:
            merge_pdf(cover_letter_path, resume_path, cover_letter_dir)
    else:
        companies = list_companies(args.companies_file)
        for company in companies:
            cover_letter_path = customize_pdf(tem, cur_date, company, name, position, cover_letter_dir)
            if merge:
                merge_pdf(cover_letter_path, resume_path, cover_letter_dir)
    
    
    if cover_letter_dir == None:
        print(f"Your customized cover letter(s) are saved in the current folder")
    else: 
        print(f"Your customized cover letter(s) are saved in the folder {cover_letter_dir}")
    if merge:
        print("Your merged letter is stored in the same folder.")
