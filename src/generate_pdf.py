from markdown import markdown
import pdfkit
from subprocess import call

file_name = 'Vengadanathan_Resume'
input_filename = file_name+'.md'
output_filename = file_name+'.pdf'

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4', extensions=['markdown.extensions.tables'])

with open('Vengadanathan_Resume.html', 'w') as html_file:
    html_file.write(html_text)

call(["xvfb-run", "wkhtmltopdf", "Vengadanathan_Resume.html", "Vengadanathan_Resume.pdf"])
