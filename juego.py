from random import randint

# Throwing a dice
def dice(): return randint(1, 6)

# Throwing two dices
def dices(): return (dice(), dice())

# Throwing two dices, calculate points
def simpleRound():
	midres = dices()
	if midres[0] == 4: return midres[1]
	if midres[1] == 4: return midres[0]
	return 0

# A round for a player
# Player is an object with a "choose" method,
# which gets the first result,
# and returns whether it wants to throw again or not
def round(player):
	first = simpleRound()
	
	if first == 0: return simpleRound()
	
	if player.choose(first): return dice()
	else: return first

class Juan:
	def __init__(self):
		pass

	def choose(self, first):
		return first <= 3

class Maria:
	def __init__(self, opscore):
		self.opscore = opscore

	def choose(self, first):
		if self.opscore < first: return False
		if self.opscore > first: return True
		return first <= 3

# A match, which consists of two rounds, one for each player
def match():
	juanscore = round(Juan())
	mariascore = round(Maria(juanscore))
	if juanscore < mariascore: return 1
	if juanscore > mariascore: return -1
	return 0

# Several matches, recording wins of each player and draws
def bigMatch(size):
	draws = 0
	juanwins = 0
	mariawins = 0
	for _ in range(size):
		res = match()
		if res == -1:  juanwins = juanwins + 1
		elif res == 1: mariawins = mariawins + 1
		else:          draws = draws + 1

	return (juanwins, mariawins, draws)

def printBigMatch(size):
	(juanwins, mariawins, draws) = bigMatch(size)
	print("n = " + str(size))
	print("Juan gana el juego: " + str(juanwins / size))
	print("María gana el juego: " + str(mariawins / size))
	print("El juego resulta en empate: " + str(draws / size))
	print()

if __name__ == "__main__":
	printBigMatch(1000)
	printBigMatch(10000)
	printBigMatch(100000)
