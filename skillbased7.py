import random, math

lowerBound = int(input("Enter Lower bound: "))
upperBound = int(input("Enter Upper bound: "))

# generating random number between lower and upper bound
var = random.randint(lowerBound, upperBound)
print("\n\tYou've only ",
	round(math.log(upperBound - lowerBound + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of guesses
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upperBound - lowerBound + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number: "))

	# Condition testing
	if var == guess:
		print("YOU WON, you guessed in ",
			count, " try")
		break


	elif var > guess:
		print("Your guess is lower")

	elif var < guess:
		print("Your guess is higher")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upperBound - lowerBound + 1, 2):
	print("\nThe number is %d" % var)

print("\n")
print("Name = Aryan Singh")
print("Enrollment No. = 0901AM211015")
print("3rd Sem")
print("Branch = AIML")
