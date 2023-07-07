import os
from django.shortcuts import render
from django.http import HttpResponse
from docx2pdf import convert


def convert_to_pdf(request):
    if request.method == 'POST':
        # Assuming the file input field has the name 'word_file'
        word_file = request.FILES['word_file']

        # Save the uploaded Word file temporarily
        with open('temp.docx', 'wb') as f:
            for chunk in word_file.chunks():
                f.write(chunk)

        # Convert the Word file to PDF
        convert("temp.docx", "temp.pdf")

        # Read the PDF file
        with open("temp.pdf", 'rb') as f:
            pdf_data = f.read()

        # Clean up the temporary files
        os.remove("temp.docx")
        os.remove("temp.pdf")

        # Send the PDF file as a response to the user
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        response.write(pdf_data)

        return response

    return render(request, 'converter/convert.html')
