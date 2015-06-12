import os, argparse
import datetime as dt
import threading
from functools import wraps

def _caffeinate():
    os.system('caffeinate')

def caffeinate(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        thrd = threading.Thread(target = _caffeinate, args = ())
        # 'service' thread. does not stop process from terminating.
        thrd.daemon = True
        thrd.start()
        fn(*args, **kwargs)
    return wrapper

def get_single_args():
    parser = argparse.ArgumentParser(description = "CLI for single southwest check-in")
    parser.add_argument('firstname', help = "first name")
    parser.add_argument('lastname', help = "last name")
    parser.add_argument('code', help = "southwest code")
    parser.add_argument('-d', '--date', help = "date (format is mm/dd/yyyy, default is today's date)", default = dt.datetime.now())
    parser.add_argument('-t', '--time', help = "time (format is hh:mm, default is current time)", default = dt.datetime.now())

    args = parser.parse_args()

    if isinstance(args.date, dt.datetime):
        args.date = args.date.strftime('%m/%d/%Y')
    if isinstance(args.time, dt.datetime):
        args.time = args.time.strftime('%H:%M')

    return args

def get_multiple_args():
    parser = argparse.ArgumentParser(description = "CLI for multiple southwest check ins")
    parser.add_argument('csv', help = "csv file full path")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    pass







