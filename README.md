# CoverLetterCustomizer

This is a simple Python script that will customize cover letters for you. Given a cover letter template (in a txt format) and a list of companies to apply to (line-separated txt file), this script will create individual cover letters for each company and return a folder with all the letters in a PDF format.

## Installation and Setup

Before running this code, you will need to install some dependencies: Argparse, DateTime, FPDF, and os. See the links for installation instructions (in general, you can use ```bash pip install <package>```). In addition, you will need to have template of your cover letter saved as a .txt file with the following modifications:
 - Put "[Date]" wherever you want the date to go