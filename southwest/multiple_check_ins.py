import sched
import csv
from southwest import SouthwestCheckIn
import time

class MultipleSouthwestCheckIns(object):
    """
        parses csv file and
        schedules multiple check-ins

        @params fname - user information csv filename

        @info - CSV File Headers:
        first name, last name, code, mm/dd/yyyy, hh:mm (24 hr)
    """

    def __init__(self, filename):
        self.filename = filename
        self.users_csv = None
        self.users = []

        self._assert()

        self.scheduler = sched.scheduler(time.time, time.sleep)
        self._parse_file()

    def _parse_file(self):
        try:
            with open(self.filename, 'r+') as f:
                self.users_csv = list(csv.reader(f, skipinitialspace = True))

            self.users = map(lambda user: SouthwestCheckIn(*user), self.users_csv)

        except IOError:
            print ("IO Error. Check file and filename parameter")

    def _schedule(self):
        for i, user in enumerate(self.users):
            seconds = user._get_seconds()
            print ("{0} is scheduled to check-in in {1:.1f} seconds"
                   .format(user.name, seconds))

            self.scheduler.enter(seconds, 1, user.check_in, ())

    def _assert(self):

        try:
            f = open(self.filename, 'r')
        except IOError as e:
            print e
            exit(0)
        try:
            csv_reader = csv.reader(f, skipinitialspace = True)
        except csv.Error as e:
            print e
            exit(0)
        finally:
            f.close()


    def run(self):
        self._schedule()
        self.scheduler.run()




