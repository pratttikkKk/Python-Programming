num_of_balls= 6
num_of_ballers=4
legal_balls = True

for ballers in range(1, num_of_ballers+1):
	for balls in range(1,num_of_balls+1):
		if (legal_balls==True):
			print("Bowler ",ballers,"bowled", balls ,"balls")

		else:
			print("illegl bowling")
