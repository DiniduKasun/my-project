# Python implementation of Runge Kutta method of order 2 
def func(x, y): 
	return (3*(18-y)) 

# Finds value of y for a given x using step size h 
# and initial value y0 at x0. 
def rungeKutta(x0, y0, x, h): 
	# Count number of iterations using step size or 
	# step height h 
	n = (int)((x - x0)/h) 
	# Iterate for number of iterations 
	y = y0 
	for i in range(1, n + 1): 
		"Apply Runge Kutta Formulas to find next value of y"
		k1 = h * func(x0, y) 
		k2 = h * func(x0 + 0.5 * h, y + 0.5 * k1)  

		# Update next value of y 
		y = y + k2

		# Update next value of x 
		x0 = x0 + h 
	return y 

# Driver method 
x0 = 0
y = 14
x = 1
h = 0.2
print ('The value of y at x is:', rungeKutta(x0, y, x, h))








