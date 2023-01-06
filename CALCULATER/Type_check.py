
## check the given input is string ,integer,float  without any inbulid function 

#user_input= input("enter the value ")
def check(user_input):
	num_char=["0","1","2","3","4","5","6","7","8","9"]

	num_count = 0
	dot_count = 0
	other_count = 0
	for i in user_input:
		if i in num_char:
			num_count += 1
		elif i == ".":
			dot_count += 1
		else:
			other_count +=1
	if other_count == 0 and dot_count ==0:
		user_input = int(user_input)

	elif other_count == 0 and dot_count ==1:
		user_input = float(user_input)
	else:
		user_input = str(user_input)
	return user_input

