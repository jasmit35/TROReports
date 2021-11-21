"""
trorpts.py
"""
#  Imports from the python standard library
import argparse
import config
import logging
import os
import sys
from traceback import print_exception

#  Imports from my standard library
from std_dbconn import get_database_connection

#  Imports from this application's other modules
from categories_sheet import CategoriesSheet
import transactions_sheet as ts
from transactions import TransactionsTable

# p = os.path.abspath("../local/python")
# sys.path.insert(1, p)


def get_cmdline_parms():
    parser = argparse.ArgumentParser(description="TROLoad")
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


def get_cfgfile_parms(environment):
    cfgfile = "local/etc/trorpts.cfg"
    cfgfile_all_parms = config.Config(cfgfile)
    return cfgfile_all_parms[environment]


def start_log(log_level):
    if log_level == "DEBUG":
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(filename="troload.log"),
            ],
        )
    else:
        if log_level == "INFO":
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                handlers=[
                    logging.StreamHandler(),
                    logging.FileHandler(filename="troload.log"),
                ],
            )
    return logging


# def select_precident_value(
#     cmd_parms, cfg_parms, os_parms, parameter_name, default_value=None
# ):
#     return_value = None
#     if default_value is not None:
#         return_value = default_value

#     try:
#         return_value = os_parms[parameter_name]
#     except KeyError:
#         pass

#     if parameter_name in cfg_parms.keys():
#         return_value = cfg_parms[parameter_name]

#     if parameter_name in cmd_parms.keys():
#         return_value = cmd_parms[parameter_name]
#     return return_value


def generate_requested_report(log, db_conn, home_dir, report, first_date, last_date):
    if report == "trans":
        tt = TransactionsTable(db_conn)
        transactions = tt.select_date_range(first_date, last_date)
        ts.build_worksheet(log, transactions, home_dir, first_date, last_date)

    if report == "cats":
        tt = TransactionsTable(db_conn)
        transactions = tt.select_date_range_summary(first_date, last_date)
        cs = CategoriesSheet()
        cs.build_worksheet(transactions, home_dir, first_date, last_date)


# def my_shutdown(log, rc=0, sysout=None, syserr=None):
#     # rpt.finish_std_rpt(rc)
#     log.info("trorpts is ending...")
#     sys.stdout.flush()
#     sys.exit(rc)


def main():
    cmdline_params = get_cmdline_parms()

    environment = cmdline_params["environment"]
    cfgfile_params = get_cfgfile_parms(environment)

    log_level = cfgfile_params["log_level"]
    log = start_log(log_level)
    log.info("trorpts is starting...")

    db_host = cfgfile_params["database_host"]
    db_conn = get_database_connection(environment, db_host)

    requested_report = cmdline_params["report"]

    home_dir = cfgfile_params["home_dir"]
    generate_requested_report(
        log,
        db_conn,
        home_dir,
        requested_report,
        cmdline_params["first_date"],
        cmdline_params["last_date"],
    )

    log.info("trorpts is ending...")
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Following uncaught exception occured. {e}")
        print_exception(e)
