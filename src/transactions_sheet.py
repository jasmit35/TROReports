"""
transactions_sheet
"""
#  Imports from the python standard library
import os
import sys

#  Imports from my standard library
p = os.path.abspath("../local/python")
sys.path.insert(1, p)
import exclsheet as exl


def build_worksheet(this_app, transactions, home_dir, start_date, end_date):
    this_app.debug(f"begin build_worksheet({home_dir=}, {start_date=}, {end_date=})")

    this_sheet = exl.ExcelSheet()
    set_headers(this_sheet)

    previous_account = None
    sum_start = this_sheet.row

    for this_transaction in transactions:

        account_name = this_transaction[0]
        if account_name != previous_account:
            if this_sheet.row != 3:
                add_summary_row(this_sheet, sum_start, this_sheet.row - 1)
                sum_start = this_sheet.row
        previous_account = account_name

        trans_date = this_transaction[1]
        description = this_transaction[2]
        category_name = this_transaction[3]
        amount = this_transaction[4]
        cleared = this_transaction[5]

        this_sheet.set_row_values(
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
        format_row(this_sheet)
        this_sheet.row += 1

    add_summary_row(this_sheet, sum_start, this_sheet.row - 1)

    file_path = f"{home_dir}/local/rpt/transactions_{start_date}_{end_date}.xlsx"
    this_sheet.save(file_path)

    this_app.debug("end   build_worksheet - returns None")


def set_headers(this_sheet):
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
    this_sheet.row = 2
    this_sheet.set_row_values(headers)
    this_sheet.row += 1


def format_row(this_sheet):
    this_sheet.col = 3
    this_sheet.format_cell_date()
    this_sheet.col = 10
    this_sheet.format_cell_numeric()


def add_summary_row(this_sheet, sum_start, sum_end):
    this_sheet.add_border_row(2, 10)
    this_sheet.col = 10
    this_sheet.add_summary_cell(sum_start, sum_end)
    this_sheet.format_cell_numeric()
    this_sheet.row += 2
