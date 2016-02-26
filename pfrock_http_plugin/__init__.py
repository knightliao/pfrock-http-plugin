from pfrock.core.register import PfrockPluginRegister
from pfrock_http_plugin.index import PfrockHttpPlugin

__version__ = '0.2.1.dev6'

PfrockPluginRegister.register(PfrockHttpPlugin)
