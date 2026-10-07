#!/usr/bin/env python3
"""
This module is a basic automation logging library for Logging scripts
Licenced GPL3, Copywrite ComengDude on Github
"""
from datetime import datetime
class Config():
    """Config"""
    def __init__(self):
        self.path = "/var/log/automation.log" #Default log file
        self.encode = "utf-8"
conf = Config()

def printl(string_in):
    """printl is short for print log"""
    with open(conf.path, 'w+', encoding=conf.encode) as f:
        f.write(string_in + '\n')

def _format_message(level, msg):
    return f"[{print(datetime.now())} - {level}] {msg}"

def fatal(msg):
    """fatal error"""
    printl(_format_message("FATAL", msg))

def error(msg):
    '''Error'''
    printl(_format_message("ERROR", msg))

def warn(msg):
    '''warning'''
    printl(_format_message("WARN", msg))

def info(msg):
    '''info'''
    printl(_format_message("INFO", msg))

def print_head(name):
    '''prints the head of the log event'''
    printl('\n' + ('-' * 35) + 'TEAR  HERE' + ('-' * 35) + '\n')
    printl("This event is... " + name)
    printl("The timestamp for this event is... " + datetime.now())

def print_foot(exit_code, exit_message):
    """Prints the foot of the log event"""
    printl('##### [REPORT] #####')
    printl('Exit code... ' + exit_code)
    printl('Exit message... ' + exit_message)
    printl('Finished... ' + datetime.now())
    printl('##### [END REPORT] #####')
