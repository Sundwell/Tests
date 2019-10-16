from fpdf import FPDF


class BasePdf:
    def __init__(self):
        self.pdf = FPDF('P', 'mm', 'A4')
        self.pdf.add_page()
        self.text = open("text.txt", "r")

    def __del__(self):
        self.text.close()


class MyPdf(BasePdf):
    def write_pdf(self):
        self.pdf.output('main.pdf', 'F')

    def set_font(self):
        string_font = self.text.readline().split('_')
        self.pdf.set_font(string_font[0], string_font[1], int(string_font[2]))

    def create_cell(self):
        cell_string = self.text.readline().split('_')
        self.pdf.cell(int(cell_string[0]), int(cell_string[1]), cell_string[2], align=cell_string[3][:1])

    def set_ln(self):
        line_break = int(self.text.readline())
        self.pdf.ln(int(line_break))


if __name__ == '__main__':
    pdf = MyPdf()
    length = int(len(pdf.text.readlines()) / 3)
    pdf.text = open("text.txt", 'r')
    print(length)
    for line in range(length):
        pdf.set_font()
        pdf.create_cell()
        pdf.set_ln()
    pdf.write_pdf()
    print('PDF is generated.')
