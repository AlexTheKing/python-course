import datetime

class Customer:
	def __init__(self, number):
		self.number = number

	def receive(self, data, customer=None):
		number = customer.number if customer else 'anon'
		print('Data from {0}: {1}'.format(number, data))

class CallService:
	MESSAGE = '''
	The wireless customer you are calling is not available.
	Please try your call again later.
	'''

	def __init__(self, caller, callee):
		self.caller = caller
		self.callee = callee

	def answer_on_no_callee(self):
		self.caller.receive(CallService.MESSAGE)

	@classmethod
	def pbx_uptime(cls):
		return datetime.datetime.now() - datetime.timedelta(days=-5, hours=-5, minutes=-42)		


service = CallService(Customer('333'), Customer('777'))
service.answer_on_no_callee()
print(service.pbx_uptime())
print(CallService.pbx_uptime())
