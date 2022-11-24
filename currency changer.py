def main():
	print("Welcome to Currency Changer")
	print("                                                           ")
	print("1. Dollar to Peso")
	print("2. peso to dollar")
	print("                                                           ")
	print("3. kuwait to Peso")
	print("4. peso to kuwait")
	print("                                                           ")
	print("5. rupees to peso")
	print("6. peso to rupees")
	print("                                                           ")
	choices = input("Please select Currency: ")
	print("                                                           ")
	if choices >= "1":
		if choices <= "6":
			if choices == "1":
				money = float(input("Dollar: "))
				print("Peso:", money * 57.4749)
			if choices == "2":	
				money = float(input("Peso: "))
				print("Dollar:", money * 0.0174)
			if choices == "3":
				money = float(input("Kuwait: "))
				print("Peso: ", money * 186.6607)
			if choices == "4":
				money = float(input("Peso: "))
				print("Kuwait: ", money * 0.0054)
			if choices == "5":
				money = float(input("Rupees: "))
				print("Peso: ", money * 0.2583)
			if choices == "6":
				money = float(input("Peso: "))
				print("Rupees: ", money * 3.8716)
		else:
			print("Please select only from the Options above thankyou")
			exit()
	else:
		print("Please select only from the Options above thankyou")
		exit()
	loop = input("Do you want to convert Money Again?(Y/N): ")
	yeslist = ["YES", "Yes", "yes", "Y", "y"]
	if loop in yeslist:
		main()
	else:
		print("Thankyou! Come Again.")




main()

