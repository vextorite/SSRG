from proccessor import scrapeUrl
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        #logo 
        self.image("logo.png", 10, 8, 25)
        #just setting width allows for auto height that wont distort
        # path, x coord, y coord, width
        self.set_font('helvetica', 'B', 20)
        #title
        self.cell(80)
        self.cell(30, 10, 'MOSS Similarity Report', border=False, ln=True, align='C')
        self.ln(20)

        return super().header()

    def footer(self):
        self.set_y(-15) # 15 mm from the bottom
        self.set_font('helvetica', 'I', 10)
        #page number
        self.cell(0,10, f'Page {self.page_no()}/{{nb}}', align='C')
        return super().footer()
    
    def report_title(self, re_num, re_title):
        # set font
        self.set_font('helvetica', '', 12)
        # background color
        self.set_fill_color(200, 220, 255)
        # Chapter title
        report_title = f'Output {re_num} : {re_title}'
        self.cell(0, 5, report_title, ln=1, fill=1)
        # line break
        self.ln()


def generateReport(url, pathName):
    myList = scrapeUrl(url)
    pdf = PDF()
    # metadata
    pdf.set_title("MOSS REPORT")
    pdf.set_author('SSRG Team')
    pdf.add_page()
    pdf.report_title(1, "Job Summary")
    pdf.ln(10)
    pdf.alias_nb_pages()
    # add a page
    pdf.set_auto_page_break(auto=True, margin=15) # how far from the bottom of the page will the page break be added
    #specify font
    pdf.set_font('Times', '', 10)
    #table code
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / 3  # distribute content evenly
    for row in myList:
        for x in row:
            pdf.multi_cell(col_width, line_height, x, border=1, ln=3, max_line_height=pdf.font_size)
        pdf.ln(line_height)
    pdf.add_page()
    pdf.report_title(2, "Graphs and Summary Statistics<DEMO PLACEHOLDER>")
    pdf.image("Matplotlib-Heatmap-using-seaborn-Package.jpeg", 50, 50, 100)
    pdf.image("histogram-problems.png", 50, 130, 100)
    pdf.output(pathName)
