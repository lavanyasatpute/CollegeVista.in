from django.test import TestCase
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib import colors
from reportlab.platypus.flowables import Spacer
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
        "NT-D": ("NT-DModel.pkl", "NT-DModelData.pkl"),
        "EWS": ("EWSModel.pkl", "EWSModelData.pkl"),
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

    # Set the margins
    left_margin = 72  # in points
    right_margin = 72
    top_margin = 72
    bottom_margin = 10

    # Calculate the available space for the table based on the margins and page size
    page_width, page_height = letter
    available_width = page_width - left_margin - right_margin
    available_height = page_height - top_margin - bottom_margin

    table_data = []
    header_row = []
    for key in x[0].keys():
        header_row.append(key)
    table_data.append(header_row)

    for my_dict in x:
        row = [str(value) for value in my_dict.values()]
        table_data.append(row)

    # Define the table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 6),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ])

    # Set the font size and padding
    font_size = 10
    padding = 4

    # Create a list to hold the elements
    elements = []

    # Add the header row to the table
    table_data[0] = [cell.upper() for cell in table_data[0]]
    elements.append(Table(table_data[0:1], style=table_style))

    # Add a spacer to create padding
    elements.append(Spacer(1, 10))

    # Add the remaining rows to the table
    table_data[1:] = [[str(cell) for cell in row] for row in table_data[1:]]
    elements.append(Table(table_data[1:], style=table_style))

    # Create a SimpleDocTemplate and build the PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, leftMargin=left_margin,
                            rightMargin=right_margin, topMargin=top_margin, bottomMargin=bottom_margin)
    doc.build(elements)

    return pdf_file

