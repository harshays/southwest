import argparse
from southwest import *
import datetime as dt
import sched


class SingleSouthwestCheckIn(object):
    """
        CLI for a single southwest checkin
        Uses argparse and optional default datetime values for convienience

        @params firstname   user's first name
        @params lastname    user's last name
        @params code        southwest code
        @params date        format is mm/dd/yyyy. default is today.
        @params time        format is hh:mm. default is current time. 
    """
    def __init__(self, parser_args):
        self.args = parser_args
        self.obj = self._get_obj()  
        self.scheduler = sched.scheduler(time.time, time.sleep)    
        
    def _get_obj(self):
        return SouthwestCheckIn(self.args.firstname, self.args.lastname, \
               self.args.code, self.args.date, self.args.time)
    
    def _schedule(self):
        seconds = self.obj._get_seconds()
        print ("{0} is scheduled to check-in in {1:.1f} seconds" 
               .format(self.obj.name, seconds))
        self.scheduler.enter(seconds, 1, self.obj.check_in, ())

    def run(self):
        self._schedule()
        self.scheduler.run()


