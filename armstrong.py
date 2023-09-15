# Python program to determine whether
# the number is Armstrong number or not

# Function to calculate x raised to
# the power y
def power(x, y):
	
	if y == 0:
		return 1
	if y % 2 == 0:
		return power(x, y // 2) * power(x, y // 2)
		
	return x * power(x, y // 2) * power(x, y // 2)

