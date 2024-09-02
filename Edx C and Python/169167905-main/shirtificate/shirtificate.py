from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")

    def add_shirt(self, name):
        self.image("shirtificate.png", x=0, y=60, w=210)
        self.set_font("Arial", "B", 24)
        self.set_text_color(255, 255, 255)
        self.text(x=55, y=140, txt=name)

def main():
    name = input("Name: ")

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.add_shirt(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
