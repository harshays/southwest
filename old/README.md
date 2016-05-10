###southwest
<hr>
##### Why use it?

Southwest is a python package for southwest flight check in(s). Comes in handy
when you're unable to manually check in. Scheduling it to run exactly
when the online check in opens up increases chances of getting
an 'A' group boarding pass.
##### Installing
```sh
$ pip install -r requirements.txt
$ python setup.py install
```
##### Console scripts
1. ``` southwest ``` simply prints howto.txt to the console
2. ``` southwest.checkin firstname lastname southwestcode --date --time ``` to
check in a user
3. ``` southwest.checkins csvfilepath ``` to check in multiple users. example -
./southwest/users.csv

##### Dependencies
1. Firefox browser - the default webdriver is Firefox. You can change the driver
in southwest/southwest.py, provided you've the driver installed.