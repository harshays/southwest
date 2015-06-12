from southwest import SouthwestCheckIn
from multiple_check_ins import MultipleSouthwestCheckIns
from single_check_in import SingleSouthwestCheckIn
from utils import caffienate, get_single_args, get_multiple_args
import selenium
import time
import os
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

@caffeinate
def southwest_check_ins():
	args = get_multiple_args()
	check_ins = MultipleSouthwestCheckIns(args.csv)
	check_ins.run()

@caffeinate
def southwest_check_in():
	args = get_single_args()
	check_in = SingleSouthwestCheckIn(args)
	check_in.run()

def southwest_help():
	with open('southwest/howto.txt') as f:
		print f.read()


