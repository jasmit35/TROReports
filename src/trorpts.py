'''
trorpts.py
'''
from argparse import ArgumentParser

from __init__ import __version__
from base_app import BaseApp

class TrorptsApp(BaseApp):

    def __init__(self):
        super().__init__('trorpts', __version__)

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
        pass

    def destruct(self):
        pass
