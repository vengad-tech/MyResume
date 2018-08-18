FROM python:3
RUN apt-get update
RUN apt-get --assume-yes install wkhtmltopdf
RUN apt-get --assume-yes install xvfb
RUN pip install pdfkit
RUN pip install markdown
ADD Vengadanathan_Resume.md /
ADD src/generate_pdf.py /
RUN python generate_pdf.py
