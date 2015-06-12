from southwest import SouthwestCheckIn
from multiple_check_ins import MultipleSouthwestCheckIns
from single_check_in import SingleSouthwestCheckIn
from utils import caffeinate, get_single_args, get_multiple_args

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


