"""
std_params
"""
from argparse import ArgumentParser
import config


def get_cmdline_parms():
    parser = ArgumentParser(description="TROLoad")
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
