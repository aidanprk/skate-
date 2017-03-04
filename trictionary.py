import random

class Trictionary:

	def __init__(self):
		
		self.list()

	def list(self):

		#Difficulty measured from 1-10
		#Position 1=Regular, 2=Fakie, 3=Nollie, 4=Switch


		self.tricks = [

		#Ollies-------------------------------------------------------------------------Ollies
		{
		'name' : 'Ollie',
		'difficulty': 1,
		'position' : 1
		},
		{
		'name' : 'Ollie',
		'difficulty': 1,
		'position' : 2
		},
		{
		'name' : 'Ollie',
		'difficulty': 2,
		'position' : 3
		},
		{
		'name' : 'Ollie',
		'difficulty': 3,
		'position' : 4
		},

		#Backside 180s
		{
		'name' : 'Backside 180',
		'difficulty': 3,
		'position' : 1
		},
		{
		'name' : 'Half Cab',
		'difficulty': 2,
		'position' : 1
		},
		{
		'name' : 'Backside 180',
		'difficulty': 3,
		'position' : 3
		},
		{
		'name' : 'Backside 180',
		'difficulty': 6,
		'position' : 4
		},

		#Frontside 180s
		{
		'name' : 'Frontside 180',
		'difficulty': 2,
		'position' : 1
		},
		{
		'name' : 'Frontside Half Cab',
		'difficulty': 2,
		'position' : 1
		},
		{
		'name' : 'Frontside 180',
		'difficulty': 4,
		'position' : 3
		},
		{
		'name' : 'Frontside 180',
		'difficulty': 3,
		'position' : 4
		},

		#Backside 360s
		{
		'name' : 'Backside 360',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Full Cab',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Backside 360',
		'difficulty': 5,
		'position' : 3
		},
		{
		'name' : 'Backside 360',
		'difficulty': 7,
		'position' : 4
		},

		#Frontside 180s
		{
		'name' : 'Frontside 360',
		'difficulty': 6,
		'position' : 1
		},
		{
		'name' : 'Frontside Full Cab',
		'difficulty': 4,
		'position' : 1
		},
		{
		'name' : 'Frontside 360',
		'difficulty': 5,
		'position' : 3
		},
		{
		'name' : 'Frontside 360',
		'difficulty': 7,
		'position' : 4
		},

		#Pop Shuvit-------------------------------------------------------------------------Shuvits
		{
		'name' : 'Pop Shuvit',
		'difficulty': 2,
		'position' : 1
		},
		{
		'name' : 'Pop Shuvit',
		'difficulty': 1,
		'position' : 2
		},
		{
		'name' : 'Shuvit',
		'difficulty': 3,
		'position' : 3
		},
		{
		'name' : 'Shuvit',
		'difficulty': 4,
		'position' : 4
		},

		#Frontside Pop Shuvit
		{
		'name' : 'Front Shuv',
		'difficulty': 3,
		'position' : 1
		},
		{
		'name' : 'Front Shuv',
		'difficulty': 1,
		'position' : 2
		},
		{
		'name' : 'Backside Shuvit',
		'difficulty': 2,
		'position' : 3
		},
		{
		'name' : 'Front Shuv',
		'difficulty': 4,
		'position' : 4
		},

		#360 Shuvits
		{
		'name' : '360 Pop Shuvit',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : '360 Shuv',
		'difficulty': 3,
		'position' : 2
		},
		{
		'name' : '360 Shuvit',
		'difficulty': 4,
		'position' : 3
		},
		{
		'name' : '360 Shuvit',
		'difficulty': 6,
		'position' : 4
		},

		#360 Front Shuvs
		{
		'name' : '360 Front Shuv',
		'difficulty': 7,
		'position' : 1
		},
		{
		'name' : '360 Front Shuv',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Backside 360 Shuvit',
		'difficulty': 4,
		'position' : 3
		},
		{
		'name' : '360 Front Shuv',
		'difficulty': 7,
		'position' : 4
		},

		#Impossibles
		{
		'name' : 'Impossible',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Impossible',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Impossible',
		'difficulty': 9,
		'position' : 3
		},
		{
		'name' : 'Impossible',
		'difficulty': 8,
		'position' : 4
		},

		#Frontfoot Impossible
		{
		'name' : 'Frontfoot Impossible',
		'difficulty': 7,
		'position' : 1
		},
		{
		'name' : 'Frontfoot Impossible',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Frontfoot Impossible',
		'difficulty': 4,
		'position' : 3
		},
		{
		'name' : 'Frontfoot Impossible',
		'difficulty': 7,
		'position' : 4
		},

		#Backside Bigspin-------------------------------------------------------------------------Bigspins 
		{
		'name' : 'Backside Bigspin',
		'difficulty': 6,
		'position' : 1
		},
		{
		'name' : 'Bigspin',
		'difficulty': 3,
		'position' : 2
		},
		{
		'name' : 'Frontside Bigspin',
		'difficulty': 5,
		'position' : 3
		},
		{
		'name' : 'Backside Bigspin',
		'difficulty': 8,
		'position' : 4
		},

		#Backside Bigger-spin
		{
		'name' : 'Backside Bigger-spin',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : 'Bigger-spin',
		'difficulty': 6,
		'position' : 2
		},
		{
		'name' : 'Frontside Bigger-spin',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Backside Bigger-spin',
		'difficulty': 9,
		'position' : 4
		},

		#Frontside Bigspin
		{
		'name' : 'Frontside Bigspin',
		'difficulty': 6,
		'position' : 1
		},
		{
		'name' : 'Frontside Bigspin',
		'difficulty': 4,
		'position' : 2
		},
		{
		'name' : 'Backside Bigspin',
		'difficulty': 4,
		'position' : 3
		},
		{
		'name' : 'Frontside Bigspin',
		'difficulty': 7,
		'position' : 4
		},

		#Frontside Biggerspin
		{
		'name' : 'Frontside Bigger-spin',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : 'Frontside Bigger-spin',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Backside Bigger-spin',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Frontside Bigger-spin',
		'difficulty': 9,
		'position' : 4
		},

		#Backside 360 Bigspin
		{
		'name' : 'Backside 360 Bigspin',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : '360 Bigspin',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Frontside 360 Bigspin',
		'difficulty': 8,
		'position' : 3
		},
		{
		'name' : 'Backside 360 Bigspin',
		'difficulty': 10,
		'position' : 4
		},

		#Frontside 360 Bigspin
		{
		'name' : 'Frontside 360 Bigspin',
		'difficulty': 10,
		'position' : 1
		},
		{
		'name' : 'Frontside 360 Bigspin',
		'difficulty': 8,
		'position' : 2
		},
		{
		'name' : 'Backside 360 Bigspin',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Frontside 360 Bigspin',
		'difficulty': 10,
		'position' : 4
		},

		#kickflip-------------------------------------------------------------------------kickflips
		{
		'name' : 'Kickflip',
		'difficulty': 3,
		'position' : 1
		},
		{
		'name' : 'Kickflip',
		'difficulty': 3,
		'position' : 2
		},
		{
		'name' : 'Kickflip',
		'difficulty': 5,
		'position' : 3
		},
		{
		'name' : 'Kickflip',
		'difficulty': 5,
		'position' : 4
		},

		#Double flip
		{
		'name' : 'Double Flip',
		'difficulty': 6,
		'position' : 1
		},
		{
		'name' : 'Double Flip',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Double Flip',
		'difficulty': 8,
		'position' : 3
		},
		{
		'name' : 'Double Flip',
		'difficulty': 8,
		'position' : 4
		},

		#Backside Flip
		{
		'name' : 'Backside Flip',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Half Cab Flip',
		'difficulty': 4,
		'position' : 1
		},
		{
		'name' : 'Frontside Flip',
		'difficulty': 6,
		'position' : 3
		},
		{
		'name' : 'Backside Flip',
		'difficulty': 7,
		'position' : 4
		},

		#Backside Flip
		{
		'name' : 'Backside Flip',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Half Cab Flip',
		'difficulty': 4,
		'position' : 1
		},
		{
		'name' : 'Frontside Flip',
		'difficulty': 6,
		'position' : 3
		},
		{
		'name' : 'Backside Flip',
		'difficulty': 7,
		'position' : 4
		},

		#Frontside Flip
		{
		'name' : 'Frontside Flip',
		'difficulty': 6,
		'position' : 1
		},
		{
		'name' : 'Frontside Half Cab Flip',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Backside Flip',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Frontside Flip',
		'difficulty': 7,
		'position' : 4
		},

		#Backside 360 Flip
		{
		'name' : 'Backside 360 Kickflip',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : 'Full Cab Flip',
		'difficulty': 7,
		'position' : 1
		},
		{
		'name' : 'Frontside 360 Kickflip',
		'difficulty': 9,
		'position' : 3
		},
		{
		'name' : 'Backside 360 Kickflip',
		'difficulty': 9,
		'position' : 4
		},

		#Frontside 360 Flip
		{
		'name' : 'Frontside 360 Kickflip',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : 'Frontside Full Cap Flip',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : 'Backside 360 Kickflip',
		'difficulty': 10,
		'position' : 3
		},
		{
		'name' : 'Frontside 360 Kickflip',
		'difficulty': 10,
		'position' : 4
		},

		#Varial Flip
		{
		'name' : 'Varial Kickflip',
		'difficulty': 3,
		'position' : 1
		},
		{
		'name' : 'Varial Kickflip',
		'difficulty': 3,
		'position' : 2
		},
		{
		'name' : 'Varial Kickflip',
		'difficulty': 6,
		'position' : 3
		},
		{
		'name' : 'Varial Kickflip',
		'difficulty': 6,
		'position' : 4
		},

		#Nightmare Flip
		{
		'name' : 'Nightmare Flip',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Nightmare Flip',
		'difficulty': 6,
		'position' : 2
		},
		{
		'name' : 'Nightmare Flip',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Nightmare Flip',
		'difficulty': 7,
		'position' : 4
		},

		#360 Flip
		{
		'name' : '360 Flip',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : '360 Flip',
		'difficulty': 4,
		'position' : 2
		},
		{
		'name' : '360 Flip',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : '360 Flip',
		'difficulty': 7,
		'position' : 4
		},

		#540 Flip
		{
		'name' : '540 Flip',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : '540 Flip',
		'difficulty': 8,
		'position' : 2
		},
		{
		'name' : '540 Flip',
		'difficulty': 10,
		'position' : 3
		},
		{
		'name' : '540 Flip',
		'difficulty': 10,
		'position' : 4
		},

		#360 Double Flip
		{
		'name' : '360 Double Flip',
		'difficulty': 7,
		'position' : 1
		},
		{
		'name' : '360 Double Flip',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : '360 Double Flip',
		'difficulty': 9,
		'position' : 3
		},
		{
		'name' : '360 Double Flip',
		'difficulty': 9,
		'position' : 4
		},

		#Hardflips
		{
		'name' : 'Hardflip',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Hardflip',
		'difficulty': 5,
		'position' : 2
		},
		{
		'name' : 'Hardflip',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Hardflip',
		'difficulty': 7,
		'position' : 4
		},

		#Hardflip 180
		{
		'name' : 'Ghetto Bird',
		'difficulty': 7,
		'position' : 1
		},
		{
		'name' : 'Hardflip 180',
		'difficulty': 6,
		'position' : 2
		},
		{
		'name' : 'Hardflip 180',
		'difficulty': 8,
		'position' : 3
		},
		{
		'name' : 'Ghetto Bird',
		'difficulty': 9,
		'position' : 4
		},

		#360 Hardflips
		{
		'name' : '360 Hardflip',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : '360 Hardflip',
		'difficulty': 9,
		'position' : 2
		},
		{
		'name' : '360 Hardflip',
		'difficulty': 10,
		'position' : 3
		},
		{
		'name' : '360 Hardflip',
		'difficulty': 10,
		'position' : 4
		},

		#Bigflips
		{
		'name' : 'Bigflip',
		'difficulty': 6,
		'position' : 1
		},
		{
		'name' : 'Bigflip',
		'difficulty': 5,
		'position' : 2
		},
		{
		'name' : 'Bigflip',
		'difficulty': 8,
		'position' : 3
		},
		{
		'name' : 'Bigflip',
		'difficulty': 9,
		'position' : 4
		},

		#Backside Bigger-flip
		{
		'name' : 'Bigger-Flip',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : 'Bigger-Flip',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Bigger-Flip',
		'difficulty': 8,
		'position' : 3
		},
		{
		'name' : 'Bigger-flip',
		'difficulty': 10,
		'position' : 4
		},

		#Backside 360 Bigflip
		{
		'name' :'360 Bigflip',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : '360 Bigflip',
		'difficulty': 8,
		'position' : 2
		},
		{
		'name' : 'Frontside 360 Bigflip',
		'difficulty': 10,
		'position' : 3
		},
		{
		'name' : '360 Bigflip',
		'difficulty': 10,
		'position' : 4
		},
		#Heelflip-------------------------------------------------------------------------Heelflips
		{
		'name' : 'Heelflip',
		'difficulty': 3,
		'position' : 1
		},
		{
		'name' : 'Heelflip',
		'difficulty': 4,
		'position' : 2
		},
		{
		'name' : 'Heelflip',
		'difficulty': 5,
		'position' : 3
		},
		{
		'name' : 'Heelflip',
		'difficulty': 5,
		'position' : 4
		},

		#Double Heelflip
		{
		'name' : 'Double Heelflip',
		'difficulty': 7,
		'position' : 1
		},
		{
		'name' : 'Double Heelflip',
		'difficulty': 9,
		'position' : 2
		},
		{
		'name' : 'Double Heelflip',
		'difficulty': 8,
		'position' : 3
		},
		{
		'name' : 'Double Heelflip',
		'difficulty': 8,
		'position' : 4
		},

		#Frontside Heel
		{
		'name' : 'Frontside Heel',
		'difficulty': 6,
		'position' : 1
		},
		{
		'name' : 'Frontside Halfcab Heelflip',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Backside Heel',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Frontside Heel',
		'difficulty': 7,
		'position' : 4
		},

		#Backside Heel
		{
		'name' : 'Backside Heel',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Halfcab Heel',
		'difficulty': 5,
		'position' : 1
		},
		{
		'name' : 'Frontside Heel',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Backside Heelflip',
		'difficulty': 6,
		'position' : 4
		},

		#Backside 360 Heelflip
		{
		'name' : 'Backside 360 Heelflip',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : 'Backside Full Cab Heel',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : 'Frontside 360 Heelflip',
		'difficulty': 10,
		'position' : 3
		},
		{
		'name' : 'Backside 360 Heelflip',
		'difficulty': 10,
		'position' : 4
		},

		#Frontside 360 Flip
		{
		'name' : 'Frontside 360 Heelflip',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : 'Full Cap Heel',
		'difficulty': 7,
		'position' : 1
		},
		{
		'name' : 'Backside 360 Heelflip',
		'difficulty': 8,
		'position' : 3
		},
		{
		'name' : 'Frontside 360 Heelflip',
		'difficulty': 9,
		'position' : 4
		},

		#Varial Heelflip
		{
		'name' : 'Varial Heel',
		'difficulty': 6,
		'position' : 1
		},
		{
		'name' : 'Varial Heel',
		'difficulty': 5,
		'position' : 2
		},
		{
		'name' : 'Varial Heel',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Varial Heel',
		'difficulty': 7,
		'position' : 4
		},

		#Double Varial Heel
		{
		'name' : 'Double Varial Heel',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : 'Double Varial Heel',
		'difficulty': 8,
		'position' : 2
		},
		{
		'name' : 'Double Varial Heel',
		'difficulty': 10,
		'position' : 3
		},
		{
		'name' : 'Double Varial Heel',
		'difficulty': 10,
		'position' : 4
		},

		#Laser Flip
		{
		'name' : 'Laser Flip',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : 'Laser Flip',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Laser Flip',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Laser Flip',
		'difficulty': 9,
		'position' : 4
		},

		#Inward Heel
		{
		'name' : 'Inward Heel',
		'difficulty': 6,
		'position' : 1
		},
		{
		'name' : 'Inward Heel',
		'difficulty': 5,
		'position' : 2
		},
		{
		'name' : 'Inward Heel',
		'difficulty': 7,
		'position' : 3
		},
		{
		'name' : 'Inward Heel',
		'difficulty': 7,
		'position' : 4
		},

		#Inwardheel 180
		{
		'name' : 'Inward Heel 180',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : 'Inward Heel 180',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Inward Heel 180',
		'difficulty': 8,
		'position' : 3
		},
		{
		'name' : 'Inward Heel 180',
		'difficulty': 10,
		'position' : 4
		},

		#360 Inward Heel
		{
		'name' : '360 Inward Heel',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : '360 Inward Heel',
		'difficulty': 8,
		'position' : 2
		},
		{
		'name' : '360 Inward Heel',
		'difficulty': 10,
		'position' : 3
		},
		{
		'name' : '360 Inward Heel',
		'difficulty': 10,
		'position' : 4
		},

		#Bigheel
		{
		'name' : 'Bigheel',
		'difficulty': 8,
		'position' : 1
		},
		{
		'name' : 'Bigheel',
		'difficulty': 7,
		'position' : 2
		},
		{
		'name' : 'Bigheel',
		'difficulty': 8,
		'position' : 3
		},
		{
		'name' : 'Bigheel',
		'difficulty': 9,
		'position' : 4
		},

		#Backside Bigger-Heel
		{
		'name' : 'Bigger-Heel',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : 'Bigger-Heel',
		'difficulty': 9,
		'position' : 2
		},
		{
		'name' : 'Bigger-Heel',
		'difficulty': 10,
		'position' : 3
		},
		{
		'name' : 'Bigger-Heel',
		'difficulty': 10,
		'position' : 4
		},

		#360 Bigheel
		{
		'name' :'360 Bigheel',
		'difficulty': 9,
		'position' : 1
		},
		{
		'name' : '360 Bigheel',
		'difficulty': 8,
		'position' : 2
		},
		{
		'name' : 'Backside 360 Bigheel',
		'difficulty': 10,
		'position' : 3
		},
		{
		'name' : '360 Bigheel',
		'difficulty': 10,
		'position' : 4
		},

		#Non-Berric------------------------------------------------------------Non-Berric Tricks
		{
		'name' : 'Boneless',
		'difficulty': 2,
		'position' : 5
		},
		{
		'name' : 'Boneless 180',
		'difficulty': 3,
		'position' : 5
		},
		{
		'name' : 'Bonless 360',
		'difficulty': 6,
		'position' : 5
		},
		{
		'name' : 'No-Comply',
		'difficulty': 3,
		'position' : 5
		}
		]

	def listAll(self):

		trick_return = []

		for i in self.tricks:
			name = i['name']
			pos = i['position']
			prefix = ' '
			if pos == 1:
				prefix = ''
			elif pos == 2:
				prefix = 'Fakie '
			elif pos == 3:
				prefix = 'Nollie '
			elif pos == 4:
				prefix = 'Switch '
			else:
				prefix = ''

			trick_return.append(prefix + name)

		return trick_return

	def search(self, word):

		trick_return = []

		for i in self.tricks:
				name = i['name']
				pos = i['position']
				prefix = ' '
				if pos == 1:
					prefix = ''
				elif pos == 2:
					prefix = 'Fakie '
				elif pos == 3:
					prefix = 'Nollie '
				elif pos == 4:
					prefix = 'Switch '
				else:	
					prefix = ''


				if word.lower() in prefix.lower() + name.lower():
					trick_return.append(prefix + name)

		if len(trick_return) > 0:
			return trick_return
	
	def difficulty(self, type):

		trick_return = []

		if isinstance(type, str) == False:
			
			for i in self.tricks:
				if i['difficulty'] == type:
					x = 1

					name = i['name']
					pos = i['position']
					prefix = ''

					if pos == 1:
						prefix = ''
					elif pos == 2:
						prefix = 'Fakie '
					elif pos == 3:
						prefix = 'Nollie '
					elif pos == 4:
						prefix = 'Switch '
					else:	
						prefix = ''

					trick_return.append(prefix + name)

		elif isinstance(type, str) == True:
			if type.lower() == 'easy':
				for i in self.tricks:
					if i['difficulty'] <= 3:
						x = 1

						name = i['name']
						pos = i['position']
						prefix = ''

						if pos == 1:
							prefix = ''
						elif pos == 2:
							prefix = 'Fakie '
						elif pos == 3:
							prefix = 'Nollie '
						elif pos == 4:
							prefix = 'Switch '
						else:	
							prefix = ''

						trick_return.append(prefix + name)
			elif type.lower() == 'medium':
				for i in self.tricks:
					if i['difficulty'] <=5:
						x = 1

						name = i['name']
						pos = i['position']
						prefix = ''

						if pos == 1:
							prefix = ''
						elif pos == 2:
							prefix = 'Fakie '
						elif pos == 3:
							prefix = 'Nollie '
						elif pos == 4:
							prefix = 'Switch '
						else:	
							prefix = ''

						trick_return.append(prefix + name)
			elif type.lower() == 'hard':
				for i in self.tricks:
					if i['difficulty'] <=8:
						x = 1

						name = i['name']
						pos = i['position']
						prefix = ''

						if pos == 1:
							prefix = ''
						elif pos == 2:
							prefix = 'Fakie '
						elif pos == 3:
							prefix = 'Nollie '
						elif pos == 4:
							prefix = 'Switch '
						else:	
							prefix = ''

						trick_return.append(prefix + name)
		return trick_return

	def random(self, rest = None, val=None):
		gen = []

		for i in self.tricks:
			if val == None:
				return random.choice(self.search(rest))
			elif val != None:
				if rest.lower() == 'dif':
					self.difficulty(val)
			elif rest == None:
				gen.append(i['name'])
			else:
				print('Error ' + rest + ' not understood')

		if len(gen) > 0:
			return random.choice(gen) 
		else:
			print('No results for '+ rest)

if __name__ == '__main__':
	dic = Trictionary()
	print(dic.listAll())



