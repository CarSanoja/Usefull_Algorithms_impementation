# Monte Carlo localization - 2D problem

# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up
##############################################################################
# The sense function will take the probability matrix and make a 
# measurement of the actual position taking what the sensor see 
# (measurement), probability of the sensor be right 
def sense(prob,measurements,sensor_right,colors):
	suma=0
	for column in range(len(prob[0])):
		for row in range(len(prob)):
			if colors[row][column] == measurements:
				prob[row][column] = prob[row][column]*sensor_right
			else:
				prob[row][column] = prob[row][column]*(1-sensor_right)
			suma += prob[row][column]
	return prob,suma
###############################################################################
# mv[row][column]
def move(vector, mov, p_move):
	if mov[1]==1:
		new_vector = [[],[],[]]
		for row in range(len(vector)):
			single_row=vector[row][:]
			q = []
			for i in range(len(single_row)):
				s = p_move*single_row[(i-1)%len(single_row)]
				q.append(s)
			new_vector[row] = q
		return new_vector
	elif mov[0]==mov[1]==0:
		return vector
	else:
		new_vector = [[],[],[]]
		for column in range(len(vector[0])):
			single_row=vector[:][column]
			q = []
			for i in range(len(single_row)):
				s = p_move*single_row[(i-1)%len(single_row)]
				q.append(s)
			new_vector[column] = q
	return new_vector
###############################################################################
# When we sense, the Sum of the values doesn't sum 1. Thats way we have to
# normalize, the summatory of the total probability must be one.
def normalize(vector,suma):
	for row in range(len(vector[0])):
		for colum in range(len(vector)):
			vector[colum][row] = vector[colum][row] / suma
	return vector
###############################################################################
# This function create a vector with an Uniform Distribution of probabilities.
# with the same size of the map matrix
def construct(colors):
	prob_initial = 1.0
	rows = len(colors[0])
	#print(rows)
	columns = len(colors)
	#print(columns)
	prob_initial = prob_initial/rows/columns
	prob = [[prob_initial for row in range(rows)] for colum in range(columns)]
	#print(prob)
	return prob
################################################################################
# This will be de main function
def Localize(colors, measurements, motions, sensor_right, p_move):
	prob_matrix = construct(colors)
	for numero_mov in range(len(measurements)):
		if numero_mov==0:
			prob_matrix_moved = move(prob_matrix,motions[numero_mov],p_move)
			prob_matrix_sensed, suma = sense(prob_matrix_moved,measurements[numero_mov],sensor_right,colors)
		else:
			prob_matrix_moved = move(prob_matrix_sensed,motions[numero_mov],p_move)
			prob_matrix_sensed, suma = sense(prob_matrix_moved,measurements[numero_mov],sensor_right,colors)
	prob_loc_norm = normalize(prob_matrix_sensed,suma)
	return prob_loc_norm
################################################################################

colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R','G']
motions = [[0,0], [0,1],[-1,0]]
sensor_right = 0.7
p_move = 0.5
p = Localize(colors,measurements,motions,sensor_right,p_move)
print(p)