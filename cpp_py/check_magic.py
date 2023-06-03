def checkNumbers(a):

	count = 0

	if a[0] + a[1] + a[2] != 15:
	
		print("R1", end = ' ')
		count+=1
	
	if a[3] + a[4] + a[5] != 15:
	
		print("R2", end = ' ')
		count+=1
	
	if a[6] + a[7] + a[8] != 15:
	
		print("R3", end = ' ')
		count+=1
	
	if a[0] +a[3] + a[6] != 15:
	
		print("C1", end = ' ')
		count+=1
	
	if a[1] +a[4] + a[7] != 15:
	
		print("C2", end = ' ')
		count+=1
	
	if a[2] +a[5] + a[8] != 15:
	
		print("C3", end = ' ')
		count+=1
	
	if a[0] +a[4] + a[8] != 15:
	
		print("D1", end = ' ')
		count+=1
	
	if a[2] +a[4] + a[6] != 15:
	
		print("D2", end = ' ')
		count+=1
	
	if count == 0:
		print("NONE")


checker = True  
while checker:                            
	user_input = [int(number) for number in input("Enter the 3 by 3 magic square: ").split()]
	i = 0
	print("\nMagic square: ")		    
	while i < 9:
		if i%3 != 2:
			print(user_input[i], end = ' ')
		else:
			print(user_input[i])
		i+=1
	print("\nMissing:", end = ' ')
	checkNumbers(user_input)
	again = input("\n\nRun again? (Y/N): ")
	if again == "n" or again == "N":
		checker = False
	print()

