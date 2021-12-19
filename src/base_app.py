"""
base_app.py
"""

from config import Config

class BaseApp:

    def __init__(self, app_name, version='0.0.0'):
        self.app_name = app_name
        self.version = version

        self.cmdline_params = self.set_cmdline_params()
        self.environment = self.set_environment()

        self.cfgfile_params = self.set_cfgfile_params()

        self.logger = self.set_logger()
        self.report = self.set_report()

    def debug(self, message):
        self.logger.log.debug(message)

    def info(self, message):
        self.logger.log.info(message)

    def report(self, message):
        self.report.write(message)

    def set_cmdline_params(self):
        raise NotImplementedError("Please define set_cmdline_params in the derived class.")

    def set_environment(self):
        return self.cmdline_params.get('environment')

    def set_cfgfile_params(self):
        cfgfile = f"local/etc/{self.app_name}.cfg"
        cfgfile_all_parms = Config(cfgfile)
        return cfgfile_all_parms.get(self.environment)

    def set_logger(self):
        return None 

    def set_report(self):
        return None 
