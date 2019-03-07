class Process:

	def __init__(self, atime, btime):
		self.arrirval_time = atime
		self.burst_time = btime
		self.is_complete = False
		self.complete_time = None

	def is_complete(self):
		return self.is_complete

	def get_total_time(self):
		if self.is_complete is False:
			return None
		else:
			return (self.complete_time - self.arrirval_time)