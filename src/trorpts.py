'''
trorpts.py
'''
from argparse import ArgumentParser
from os import path as ospath
from sys import path as syspath
from traceback import print_exc


from __init__ import __version__
from categories_sheet import CategoriesSheet
from transactions import TransactionsTable
import transactions_sheet as ts

shared_code_path = ospath.abspath("../local/python")
syspath.insert(1, shared_code_path)
from base_app import BaseApp
from std_dbconn import get_database_connection


class TrorptsApp(BaseApp):

    def __init__(self, app_name, version):
        super().__init__(app_name, version)
        self.db_conn = get_database_connection(self.environment)

    def set_cmdline_params(self):
        parser = ArgumentParser(description="TRORpts")
        parser.add_argument(
            "-e", "--environment", required=True, help="Environment - devl, test or prod"
        )
        parser.add_argument("-r", "--report", required=True, help="iReport - trans or cats")
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
        report = self.cmdline_params.get('report')
        first_date = self.cmdline_params.get('first_date')
        last_date = self.cmdline_params.get('last_date')
        home_dir = self.cfgfile_params.get('home_dir')
        if report == 'trans':
            tt = TransactionsTable(self.db_conn)
            transactions = tt.select_date_range(first_date, last_date)
            ts.build_worksheet(self, transactions, home_dir, first_date, last_date)

        if report == "cats":
            tt = TransactionsTable(self.db_conn)
            transactions = tt.select_date_range_summary(first_date, last_date)
            cs = CategoriesSheet()
            cs.build_worksheet(transactions, home_dir, first_date, last_date)

        return 0

    def destruct(self, rc):
        self.db_conn = None
        super().destruct(rc)


if __name__ == "__main__":
    try:
        this_app = TrorptsApp('trorpts', __version__)
        rc = this_app.process()
        this_app.destruct(rc)
    except Exception as e:
        print(f"Following uncaught exception occured. {e}")
        print_exc()
