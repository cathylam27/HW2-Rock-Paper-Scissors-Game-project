from gameComponents import gameVars

def winorlose(status):
	print("You", status, " Hey~ Would you like to kill the Monster again?")
	choice = input("Y / N? ")

	if choice == "N" or choice =="n":
		print("You chose to quit! See you next time!｡^‿^｡")
		exit()
	elif choice == "Y" or choice == "y":

		gameVars.player_lives = gameVars.total_lives
		gameVars.computer_lives = gameVars.total_lives
		gameVars.play_choice = False
	else:
		print("Please choose - Y or N")
		choice = input("Y / N? ")