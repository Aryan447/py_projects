import random
import math

# Taking Inputs of Lower Bound
lower = int(input("Enter Lower bound:- "))

# Taking Inputs of Upper Bound
upper = int(input("Enter Upper bound:- "))

# generating random number between
# lower and upper bound
x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of guesses
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break

	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

print("\n")
print("Name = Aryan Singh")
print("Enrollment No. = 0901AM211015")
print("3rd Sem")
print("Branch = AIML")