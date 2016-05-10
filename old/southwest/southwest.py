import re
import time
import datetime as dt
import selenium
import selenium.webdriver.common


class SouthwestCheckIn(object):
    """
        Southwest Check In class

        parameters:
            fname - first name
            lname - last name
            code - southwest check in code
            date - mm/dd/yyyy format required (or 'today')
            time - 24 hour format required (or 'now')
    """

    def __init__(self, fname, lname, code, date, time, driver_name = 'Firefox'):
        self.fname = fname
        self.lname = lname
        self.name = "{} {}".format(fname, lname)
        self.code = code.upper()
        self.date = date
        self.time = time

        self._assert()

        self.datetime = self._get_datetime_obj(date, time)
        self.datetime_now = dt.datetime.now()
        self.seconds = self._get_seconds()

        self.driver = None
        self.driver_name = driver_name
        self.link = 'https://www.southwest.com/flight/retrieveCheckinDoc.html'


    def check_in(self):
        """ Southwest Check In using driver """
        try:
            self.driver = getattr(selenium.webdriver, self.driver_name)()
            self.driver.get(self.link)
        except selenium.common.exceptions.WebDriverException as e:
            print e.msg
            print 'install firefox driver and try again'
            exit(0)

        code_elem = self.driver.find_element_by_id('confirmationNumber')
        fname_elem = self.driver.find_element_by_id('firstName')
        lname_elem = self.driver.find_element_by_id('lastName')
        submit_elem = self.driver.find_element_by_id('submitButton')

        code_elem.send_keys(self.code)
        fname_elem.send_keys(self.fname)
        lname_elem.send_keys(self.lname)

        submit_elem.click()
        time.sleep(1)

        try:
            confirm_elem = self.driver.find_element_by_id('printDocumentsButton')
            confirm_elem.click()

        except selenium.common.exceptions.NoSuchElementException:
            print "{}'s details are incorrect.".format(self.name),\
                  "update input and try again."
        except Error:
            print ("unknown error")
        finally:
            self.driver.quit()

    def _get_datetime_obj(self, date, time):
        date = map(int, date.split('/'))
        time = map(int, time.split(':'))
        return dt.datetime(date[2], date[0], date[1], *time)

    def _get_seconds(self):
        seconds = dt.timedelta.total_seconds(self.datetime - self.datetime_now)
        return seconds if seconds > 0 else 0

    def _assert(self):
        def error(attr):
            return "{}'s {} is invalid. Try again".format(self.name, attr)

        date_pattern = r'^(\d\d)/(\d\d)/(\d\d\d\d)$'
        time_pattern = r'^(\d\d):(\d\d)$'

        date_re = re.search(date_pattern, self.date)
        time_re = re.search(time_pattern, self.time)

        try:
            assert isinstance(self.fname, str) and self.fname.isalpha(), error('fname')
            assert isinstance(self.lname, str) and self.lname.isalpha(), error('lname')
            assert isinstance(self.code, str) and len(self.code) == 6, error('code')
            assert date_re, error('date')
            assert time_re, error('time')

            month, day, year = map(int, date_re.groups())
            hour, minute = map(int, time_re.groups())

            assert 0 < month < 13 and 0 < day < 32, error('date')
            assert 0 <= hour <= 24 and 0 <= minute <= 59, error('time')

        except AssertionError as err:
            print (err.message)
            exit(0)


