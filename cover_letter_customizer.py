import argparse
from PyPDF2 import PdfFileReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from pathlib import Path
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
    pdf.output(f'{cover_letter_dir}/{company}_cover_letter.pdf', 'F').encode("latin-1")

    return
   
if __name__ == "__main__":
    
    argparser = argparse.ArgumentParser(description = "Cover Letter Customizer - Given a list of companies you want to apply to (line-separated txt file) and a cover letter template (txt), this file will create a folder with customized cover letters for each company.")
    argparser.add_argument("companies_file",
                        type=str,
                        help="txt file containing company names (line-separated)")
    argparser.add_argument("template_path",
                        type=str,
                        help="path to txt of the template")

    args = argparser.parse_args()
    companies = list_companies(args.companies_file)
    cur_date = date_str()
    
    tem = txt_to_string(args.template_path)
    name = input("Please enter your FULL NAME:\n")
    position = input("Please enter the position you are applying for:\n")
    cover_letter_dir = input("Please enter a folder name to save all the cover letters:\n")
    os.mkdir(cover_letter_dir)

    for company in companies:
        customize_pdf(tem, cur_date, company, name, position, cover_letter_dir)

    print(f"Your customized cover letters are saved in the folder {cover_letter_dir}")
