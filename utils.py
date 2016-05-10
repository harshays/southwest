from __future__ import print_function
import os
import sys
import datetime as dt
import mechanize
import json

from functools import wraps
from argparse  import ArgumentParser
from bs4       import BeautifulSoup


def get_args():
	parser = ArgumentParser(description="Southwest Check-ins")
	parser.add_argument("config", help="Full path to config path")
	return parser.parse_args()

def get_browser():
	br = mechanize.Browser()

	params = [('set_handle_equiv', True), ('set_handle_redirect', True),
	          ('set_handle_referer', True), ('set_handle_robots', False)]

	for param, value in params: getattr(br, param)(value)

	br.addheaders = [['User-Agent', 'Chrome']]
	return br

def get_soup(browser_obj):
	return BeautifulSoup(browser_obj.response().read(), 'lxml')

def notify(msg, debug):
    """decorator to output function calls along with messages"""
    def notify_decorator(function):
        @wraps(function)
        def notify_wrapper(*args, **kw):
            val = function(*args, **kw)
            if debug:
                output_args = ", ".join(map(str,args[1:]))
                print ("{}({}) -> {}".format(function.__name__, output_args, msg))
            return val
        return notify_wrapper
    return notify_decorator

def load_json(fpath):
    with open(fpath, 'r') as f:
        data = json.load(f)
    return data

def to_json(fpath, data):
    with open(fpath, 'w') as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))