from openpyxl import Workbook

class ExcelWriter:
    def __init__(self, filename="output.xlsx"):
        self.filename = filename
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title = "Company Financials"
        self.headers_written = False

    def write_headers(self, headers):
        if not self.headers_written:
            self.ws.append(headers)
            self.headers_written = True

    def add_row(self, row):
        formatted_row = [self.format_cell(value) for value in row]
        self.ws.append(formatted_row)

    def format_cell(self, value):
        if isinstance(value, list):
            return ", ".join(map(str, value))
        return value

    def save(self):
        self.wb.save(self.filename)
        print(f"Data saved to {self.filename}")

