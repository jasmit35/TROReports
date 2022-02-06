"""
trorpts.py
"""
from argparse import ArgumentParser
from os import path as ospath
from sys import path as syspath
from traceback import print_exc

from __init__ import __version__
from categories_sheet import CategoriesSheet
from ending_balances_sheet import EndingBalancesSheet
from transactions_sheet import TransactionsSheet

shared_code_path = ospath.abspath("../local/python")
syspath.insert(1, shared_code_path)
from base_app import BaseApp
from std_dbconn import get_database_connection

shared_code_path = ospath.abspath("../tro/local/python")
syspath.insert(1, shared_code_path)
from transactions import TransactionsTable


class TrorptsApp(BaseApp):
    def __init__(self, app_name, version):
        super().__init__(app_name, version)
        self.db_conn = get_database_connection(self.environment)

    def set_cmdline_params(self):
        parser = ArgumentParser(description="TRORpts")
        parser.add_argument(
            "-e",
            "--environment",
            required=True,
            help="Environment - devl, test or prod",
        )
        parser.add_argument(
            "-r", "--report", required=True, help="Report - [cats, ending, trans]"
        )
        parser.add_argument(
            "-c",
            "--cfgfile",
            required=False,
            default="trorpts.cfg",
            help="Name of the configuration file to use",
        )
        parser.add_argument("-f", "--first-date", required=False, help="Start Date")
        parser.add_argument("-l", "--last-date", required=False, help="Last Date")
        args = parser.parse_args()
        return vars(args)

    def process(self):
        valid_reports = ['cats', 'ending', 'trans']
        report = self.cmdline_params.get("report")
        if report not in valid_reports:
            self.error('Errror! Report command line option was invalid.')
            self.output('Errror! Report command line option was invalid.')
            return 16

        first_date = self.cmdline_params.get("first_date")
        last_date = self.cmdline_params.get("last_date")
        home_dir = self.cfgfile_params.get("home_dir")
        tt = TransactionsTable(self.db_conn)

        if report == "cats":
            transactions = tt.select_date_range_summary(first_date, last_date)
            cs = CategoriesSheet()
            cs.build_worksheet(transactions, home_dir, first_date, last_date)

        if report == "ending":
            balances = tt.select_ending_balances(last_date)
            ebs = EndingBalancesSheet()
            ebs.build_worksheet(balances, last_date)

        if report == "trans":
            transactions = tt.select_date_range(first_date, last_date)
            ts = TransactionsSheet()
            ts.build_worksheet(self, transactions, home_dir, first_date, last_date)

        return 0

    def destruct(self, rc):
        self.db_conn = None
        super().destruct(rc)


if __name__ == "__main__":
    try:
        this_app = TrorptsApp("trorpts", __version__)
        rc = this_app.process()
        this_app.destruct(rc)
    except Exception as e:
        print(f"Following uncaught exception occured. {e}")
        print_exc()
