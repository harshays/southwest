from __future__ import print_function
import os
import sys
import datetime as dt
import utils
from southwest   import Southwest
from collections import defaultdict, namedtuple

User = namedtuple('User', ['fname', 'lname', 'code', 'email', 'time'])

class Schedule(object):

	@staticmethod
	def _get_users(users):
		for user in users:
			fname, lname, code, email, _ = [user[k] for k in User._fields]
			dt_str = '{} {}'.format(user['date'], user['time'])
			dtime  = dt.datetime.strptime(dt_str,'%m/%d/%Y %H:%M')
			yield User(fname, lname, code, email, dtime)

	@classmethod
	def from_config_path(cls, config_path):
		config_json = utils.load_json(config_path)
		sched_path  = config_json['schedule_config_path']
		sched_json  = utils.load_json(sched_path)
		return cls(config_json, sched_json)

	def __init__(self, config_json, schedule_json):
		self.config_json = config_json
		self.sched_json  = schedule_json

		self.out_log = config_json['logging']['out']
		self.err_log = config_json['logging']['error']

		self.email_notify = schedule_json['notify_via_email']
		self.users_json   = schedule_json['users']

		self.users    = list(self._get_users(self.users_json))
		self.checkins = list(map(Southwest, self.users))

	def run(self):
		for checkin in self.checkins:
			checkin.checkin(send_email=self.email_notify)

def run():
	args = utils.get_args()
	sch  = Schedule.from_config_path(args.config)
	sch.run()

if __name__ == '__main__':
	run()