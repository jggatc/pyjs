"""Logging module for Pyjamas, mimicking CPython's logging module.

Usage example:
    from pyjamas import logging
    log = logging.getPrintLogger()
    log.debug('This is a debug message')
"""
__author__ = 'Peter Bittner <peter.bittner@gmx.net>'

from pyjamas.logging.handlers import AlertHandler, AppendHandler, ConsoleHandler
# blatantly copy everything from CPython's logging
from logging import *

PYJS_NAME = 'pyjs'

def __getLoggerForHandler(handler, name, level, fmt):
    formatter = Formatter(fmt)
    handler.setFormatter(formatter)
    logger = getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

def getAlertLogger(name=PYJS_NAME, level=DEBUG, fmt=BASIC_FORMAT):
    """A logger that shows any log message in a browser's alert popup dialog."""
    return __getLoggerForHandler(AlertHandler(), name, level, fmt)

def getAppendLogger(name=PYJS_NAME, level=DEBUG, fmt=BASIC_FORMAT):
    """A logger that appends text to the end of the HTML document body."""
    return __getLoggerForHandler(AppendHandler(), name, level, fmt)

def getConsoleLogger(name=PYJS_NAME, level=DEBUG, fmt=BASIC_FORMAT):
    """A logger that uses Firebug's console.log() function."""
    return __getLoggerForHandler(ConsoleHandler(), name, level, fmt)

def getPrintLogger(name=PYJS_NAME, level=DEBUG, fmt=BASIC_FORMAT):
    """A logger that prints text to cerr, the default error output stream."""
    return __getLoggerForHandler(StreamHandler(), name, level, fmt)
