"""
transactions_sheet
"""
#  Imports from the python standard library
import os
import sys

#  Imports from my standard library
p = os.path.abspath("../local/python")
sys.path.insert(1, p)
from exclsheet import ExcelSheet


class TransactionsSheet(ExcelSheet):
    def __init__(self, app_name="app name", version="0.0.0"):
        ExcelSheet.__init__(self)
        self.app_name = app_name
        self.version = version

    def build_worksheet(self, transactions, home_dir, start_date, end_date):
        # self.debug(f"begin build_worksheet({home_dir=}, {start_date=}, {end_date=})")
        self.set_headers()

        previous_account = None
        sum_start = self.row

        for this_transaction in transactions:

            account_name = this_transaction[0]
            if account_name != previous_account:
                if self.row != 3:
                    self.add_summary_row(sum_start, self.row - 1)
                    sum_start = self.row
            previous_account = account_name

            trans_date = this_transaction[1]
            description = this_transaction[2]
            category_name = this_transaction[3]
            amount = this_transaction[4]
            cleared = this_transaction[5]

            self.set_row_values(
                [
                    "",
                    account_name,
                    trans_date,
                    description,
                    category_name,
                    cleared,
                    this_transaction[6],  # Number
                    this_transaction[7],  # Memo
                    this_transaction[8],  # Tax item
                    amount,
                ],
            )
            self.format_row()
            self.row += 1

        self.add_summary_row(sum_start, self.row - 1)

        file_path = f"{home_dir}/local/rpt/transactions_{start_date}_{end_date}.xlsx"
        self.save(file_path)

        # self.debug("end   build_worksheet - returns None")

    def set_headers(self):
        headers = (
            "",
            "Account",
            "Date",
            "Description",
            "Category",
            "Cleared",
            "Number",
            "Memo",
            "Tax item",
            "Amount",
        )
        self.row = 2
        self.set_row_values(headers)
        self.row += 1

    def format_row(self):
        self.col = 3
        self.format_cell_date()
        self.col = 10
        self.format_cell_numeric()

    def add_summary_row(self, sum_start, sum_end):
        self.add_border_row(2, 10)
        self.col = 10
        self.add_summary_cell(sum_start, sum_end)
        self.format_cell_numeric()
        self.row += 2
