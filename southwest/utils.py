import os
import sys
import argparse
import datetime as dt
import threading
from functools import wraps

def caffeinate(fn):
    caff = lambda: os.system('caffeinate')
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if sys.platform == 'darwin':
            thrd = threading.Thread(target = caff, args = ())
            thrd.daemon = True
            thrd.start()
        fn(*args, **kwargs)
    return wrapper

def get_single_args():
    parser = argparse.ArgumentParser(description = "CLI for single southwest check-in")
    parser.add_argument('firstname', help = "enter first name")
    parser.add_argument('lastname', help = "enter last name")
    parser.add_argument('code', help = "enter southwest code")
    parser.add_argument('-d', '--date', help = "date (format is mm/dd/yyyy, default is today's date)", default = dt.datetime.now().strftime('%m/%d/%Y'))
    parser.add_argument('-t', '--time', help = "time (format is hh:mm, default is current time)", default = dt.datetime.now().strftime('%H:%M'))
    return parser.parse_args()

def get_multiple_args():
    parser = argparse.ArgumentParser(description = "CLI for multiple southwest check ins")
    parser.add_argument('csv', help = "enter csv file full path")
    return parser.parse_args()
