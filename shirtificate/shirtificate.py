from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png",0,60)
'''pdf.image("logo.png",68,160)'''
pdf.set_font("helvetica", "B", 45)
pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(r=255, g=255, b=255)
pdf.cell(0, 120, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", align='C')
pdf.output("shirtificate.pdf")