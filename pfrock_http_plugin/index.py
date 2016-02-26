#!/usr/bin/env python
# coding=utf8

import importlib
import logging
import traceback

from pfrock.core.constants import ROUTER_PATH
from pfrock.core.plugin import PfrockPlugin

logger = logging.getLogger('pfrock.handler')

ROUTER_HTTP_HANDLER = 'handler'


def import_from_file(class_path):
    r_index = class_path.rfind('.')
    module = importlib.import_module(class_path[0:r_index])
    my_class = getattr(module, class_path[r_index + 1:])
    return my_class


class PfrockHttpPlugin(PfrockPlugin):
    def get_handler(self, options, **kwargs):
        if not options:
            options = {}

        # url path
        url_path = kwargs.get(ROUTER_PATH)

        # handler class
        handler_class = options[ROUTER_HTTP_HANDLER] if ROUTER_HTTP_HANDLER in options else None

        if handler_class:

            try:
                my_class = import_from_file(handler_class)
                handler = (url_path, my_class, options)
                return handler
            except:
                logger.error(traceback.format_exc())
                return None

        return None
