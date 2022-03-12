"""
categories_sheet.py
"""
import os
import sys

p = os.path.abspath("../local/python")
sys.path.insert(1, p)
from exclsheet import ExcelSheet


class CategoriesSheet(ExcelSheet):
    pass

    def build_worksheet(self, transactions, home_dir, start_date, end_date):
        headers = ("", "Account", "Category", "Amount")
        self.row = 2
        self.set_row_values(headers)
        self.row += 1

        previous_account = None
        sum_start = self.row

        for this_transaction in transactions:

            account_name = this_transaction[0]
            if account_name != previous_account:
                if self.row != 3:
                    self.add_summary_row(sum_start, self.row - 1)
                    sum_start = self.row
            previous_account = account_name

            self.set_row_values(
                [
                    "",  # Blank column
                    account_name,
                    this_transaction[1],  # Category name
                    this_transaction[2],  # Amount
                ]
            )
            self.format_row()
            self.row += 1

        self.add_summary_row(sum_start, self.row - 1)

        file_path = f"{home_dir}/local/rpt/categories_{start_date}_{end_date}.xlsx"
        self.save(file_path)

    def format_row(self):
        self.col = 3
        self.format_cell_date()
        self.col = 4
        self.format_cell_numeric()

    def add_summary_row(self, sum_start, sum_end):
        self.add_border_row(2, 4)
        self.col = 4
        self.add_summary_cell(sum_start, sum_end)
        self.format_cell_numeric()
        self.row += 2
