from django.test import TestCase
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib import colors
import tempfile
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
import joblib

def lavanya(x, y):
    models = {
        "OBC": ("OBCModel.pkl", "OBCModelData.pkl"),
        "Open": ("OpenModel.pkl", "OpenModelData.pkl"),
        "VJ": ("VJModel.pkl", "VJModelData.pkl"),
        "SC": ("SCModel.pkl", "SCModelData.pkl"),
        "ST": ("STModel.pkl", "STModelData.pkl"),
        "SBC": ("SBCModel.pkl", "SBCModelData.pkl"),
        "NT-B": ("NT-BModel.pkl", "NT-BModelData.pkl"),
        "NT-C": ("NT-CModel.pkl", "NT-CModelData.pkl"),
        "NT-D": ("NT-DModel.pkl", "NT-DModelData.pkl")
    }
    
    if y in models:
        classifier = joblib.load(models[y][0])
        ram = joblib.load(models[y][1])
        
        j = classifier.predict([[x]])
        q = int(''.join(map(str, j - 1)))
        
        Branches = ram.iloc[q:, 2]
        Percentile = ram.iloc[q:, 3]
        Colleges = ram.iloc[q:, 1]
        
        Colleges = list(Colleges)
        Branches = list(Branches)
        Percentile = list(Percentile)

        my_list = []
        i = len(ram) - q
        
        for j in range(i - 1):
            my_dict = {}
            my_dict['Colleges'] = Colleges[j]
            my_dict['Branches'] = Branches[j]
            my_dict['Percentile'] = Percentile[j]
            my_list.append(my_dict)
        
        return my_list
    
    else:
        return 1

def generate_pdf(x):

    pdf_file = "College List.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    left_margin = 72  # in points
    right_margin = 72
    top_margin = 72
    bottom_margin = 18
    c.translate(left_margin, bottom_margin)

    table_data = []
    header_row = []
    for key in x[0].keys():
        header_row.append(key)
    table_data.append(header_row)

    for my_dict in x:
        row = [str(value) for value in my_dict.values()]
        table_data.append(row)

    table = Table(table_data)
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 6),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ])

    # Apply the table style
    table.setStyle(table_style)

    # Calculate the width of each column based on the page size and number of columns
    page_width, page_height = A4
    column_width = page_width / 3
    table_width = column_width * len(table_data[0])
    table.wrapOn(c, table_width, page_height)

    # Draw the table on the canvas, centered horizontally
    x = (page_width - table_width) / 2
    table.drawOn(c, x, 200)

    c.save()


    return pdf_file