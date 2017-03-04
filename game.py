from trictionary import *

class Skate:

	def __init__(self):

		self.letters = []

	def attempt(self, percentage):

		if random.randint(1, 100) <= percentage:
			return True