





# first = input("birinchi sin: ")
# ishora = input("+.-.*./  birontasini kiriting: ")
# second =input("ikkinchi son: ")

# if ishora == ("+") :
#     print(first + second)
# elif ishora == "-" :
#     print(first - second)
# elif ishora == "*" :
#     print(first * second)
# elif ishora == "/" :
#     print(first / second)
# else:
#     print("noto`g`ri ")


# num =9
# con = 0
# lim = 3
# while con < lim:
#     guess = int(input('guess:'))
#     con +=1
#     if guess == num :
#         print("ha")

# for i in range(2,8):
#     print(i)
# pri = [10,20,30]

# total = 10
# for pir in pri:
#     total +=pir
# print(f'total: {total}')

# for a in range(4):
#     for b in range(3):
#         print(f'({a}, {b})')





# numbers = [5,2,5,9,2]
# for x in numbers:
#     print('x'*x)
# Function for nth fibonacci
# number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
	a = 0
	b = 1
	
	# Check is n is less
	# than 0
	if n < 0:
		print("Incorrect input")
		
	# Check is n is equal
	# to 0
	elif n == 0:
		return 0
	
	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program
print(fibonacci(9))

# This code is contributed by Saket Modi
# Then corrected and improved by Himanshu Kanojiya
