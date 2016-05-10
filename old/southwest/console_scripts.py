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
    help = """
Southwest is a python package to schedule southwest flight check-ins.

There are 2 entry points:

o   southwest.checkin

    CLI for a single check in. Check in can be
    scheduled using the command line.

o   southwest.checkins

    CLI for multiple check ins. The only positional
    argument is the full path to the csv file 
    containing the check in information. 

o   CSV format

    Each check in should be on a separate line.
    The format is fname,lname,code,date,time.
    time & date should be in 24 hr & mm/dd/yyyy format.

o   Misc

    Use southwest.checkin -h or southwest.checkins -h 
    for help. Also, note that unless you have drivers
    for Chrome or Safari installed, Selenium is packaged
    with the Firefox driver. Therefore, the Firefox browser
    should be installed.
            """
    print (help)

if __name__ == '__main__':
    southwest_help()
