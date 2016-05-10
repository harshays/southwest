from __future__ import print_function
import os
import sys
import datetime as dt
import mechanize
import utils

class Southwest(object):
	"""
	southwest core class for checking in a single user
	all user information in User namedtuple
	"""
	DEBUG = True

	URL = { 
		'checkin': 'https://www.southwest.com/flight/retrieveCheckinDoc.html',
		'confirm': ''
	}

	def __init__(self, user):
		self.user    = user
		self.browser = utils.get_browser()

	@utils.notify('Check In', DEBUG)
	def _checkin(self):
		self.browser.open(Southwest.URL['checkin'])
		self.browser.select_form(nr=1)
		self.browser.form['confirmationNumber'] = self.user.code
		self.browser.form['firstName'] = self.user.fname
		self.browser.form['lastName'] = self.user.lname
		self.browser.submit()
		return self.browser.geturl() != Southwest.URL['checkin']

	@utils.notify('Invalid Check In', DEBUG)
	def _invalid_checkin(self):
		soup = utils.get_soup(self.browser)
		ul   = soup.find('ul', {'class': 'list_errors'})
		li   = ul.find_all('li')[0]
		err  = 'Error: ' + li.text.split('\n')[0]
		print (err)
		return err

	@utils.notify('Confirm Check In', DEBUG)
	def _confirm(self, send_email=True):
		raise NotImplementedError

	def checkin(self, send_email=True):
		success = self._checkin()
		if success: self._confirm(send_email)
		else:		self._invalid_checkin()