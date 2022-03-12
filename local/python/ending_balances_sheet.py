"""
ending_amounts_sheet.py
"""
import os
import sys

p = os.path.abspath("../local/python")
sys.path.insert(1, p)
from exclsheet import ExcelSheet


class EndingBalancesSheet(ExcelSheet):
    def build_worksheet(self, rows, end_date):
        headers = (f"As of {end_date}", "")
        self.row = 1
        self.set_row_values(headers)
        self.row += 1

        headers = ("", "Account", "Balance")
        self.set_row_values(headers)
        self.row += 1

        sum_start = self.row

        for this_row in rows:

            self.set_row_values(
                [
                    "",
                    this_row[0],
                    this_row[1],
                ]
            )
            self.format_row()
            self.row += 1

        self.add_summary_row(sum_start, self.row - 1)

        file_path = f"local/rpt/ending_balances_{end_date}.xlsx"
        self.save(file_path)

    def format_row(self):
        self.col = 3
        self.format_cell_numeric()

    def add_summary_row(self, sum_start, sum_end):
        self.add_border_row(2, 3)
        self.col = 3
        self.add_summary_cell(sum_start, sum_end)
        self.format_cell_numeric()
        self.row += 2
