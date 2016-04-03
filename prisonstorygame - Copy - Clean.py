# Corey Schultz
# 4/3/2016
import time
time.sleep(2)
print "The Interactive Prison Escape Game"
time.sleep(3)
print "Created by Corey Schultz"
time.sleep(3)
print "Let's Begin"
time.sleep(2)
import os
os.system("cls")
time.sleep(3)
# end of intro / start of game
# when values are selected but the other is the action, this is intentional, meant for comedic purposes (orange and left)

print "Klyde: Welcome, inmate #10G67D, to the Johnson Experimental Institute."
time.sleep(2) #delay for 5 seconds
print "Klyde: The kids they send in these days...keep getting younger and younger. It's a real shame. *shakes head* "
time.sleep(5) #delay for 5 seconds
print "Klyde: Well no point in sulking, I'm not the one spending the rest of my life in this hell hole. LOL! But, fortunately for you, you get to pick your own clothes! How exciting!"
time.sleep(2) #delay for 2 seconds
print "Klyde: Please select an orange or gray jumpsuit:"
answer = raw_input("Type 'orange' or 'gray' and hit the enter button ").lower()
if answer == "gray" or answer == "orange" :
	time.sleep(3)
	print "Klyde: Ah! Gray! What a fantastic choice! The hippopotamus herd! They'll be glad to have a man of your -er- type joining them. *giggles under breath* "
	print "Klyde: My apologies but I do have more important work to be getting back to"
	time.sleep(11)
	print "Klyde: F.R.A.N.K. , the AI chip we have installed in your brain will take it from here. "
	print "Klyde: Goodluck out there kiddo.*winks* "
	time.sleep(9)
	print "F.R.A.N.K: Welcome inmate #10G67D"
	time.sleep(6)
	name = raw_input("Please type in your name and press 'enter' ")
	print "You : Please, call me " + name 
	time.sleep(5)
	print "F.R.A.N.K: Alright,  I will be the voice in your head from now on, " + name
	time.sleep(5)
	print "You : Great"
	time.sleep(5)
	print "F.R.A.N.K: Although I am artificial intelligence, I can still detect sarcasm sir and I do not appreciate it "
	time.sleep(5)
	print "You : Golly, you really are in my head"
	time.sleep(5)
	print "F.R.A.N.K: Johnson Experimental Institute : Founded in the 1930's by the late-great Cave Johnson himself! You may remember him for his most famous quote : 'when life gives you-' "
	time.sleep(8)
	print "You : yeah, I've heard it before bro "
	time.sleep(4)
	print "F.R.A.N.K: well then, as we approach a fork in the hallway here please select your path"
	answer = raw_input("Please type 'left' or 'right' ").lower()
	if answer == "left" or answer == "right" :
		print "F.R.A.N.K: Right it is,please watch your step as we walk through this hallway"
		time.sleep(5)
		print "F.R.A.N.K: Now there is falling debris so please be careful"
		time.sleep(5)
		print " *BANG* *Giant Crashing Noise*"
		answer == raw_input("Please insert a response to that event ")
		time.sleep(4)
		print "F.R.A.N.K: I am going to pretend I didn't hear that " + name
		time.sleep(4)
		print "You : holy smokes batman, what is this place"
		time.sleep(4)
		print "F.R.A.N.K: wait, I think I hear something..."
		time.sleep(2)
		print " *A GIANT ALIEN DROPS THROUGH THE CEILING LOOKING LIKE A CRAZY PREDATOR, WHY IS IT ALWAYS ALIENS?* "
		answer = raw_input("Sir, you must decie quickly, do we 'fight' or 'run' ")
		if answer == "fight" :
			print " *I think you know that you're dead* "
			answer = raw_input("Would you like to try again? type 'yes'or 'no' ")
			if answer == "yes" :
				print "lol too bad you lost"
					
				time.sleep(4)
			elif answer == "no" :
				print "ok, goodbye"
				time.sleep(4)
		elif answer == "run" :
			print "F.R.A.N.K: OK, let's get out of here " + name
			time.sleep(3)
			print " *You are now sprinting at full speed down a collapsing hallway, realizing how out of shape you are and that probably stealing that candy bar was not worth all this trouble* "
			time.sleep(10)
			answer = raw_input("F.R.A.N.K: Sir, we have reached a dead end with two staricases. You must quickly decide! 'up' or 'down' ")
			if answer == "up" :
				print "F.R.A.N.K: oh no, the explosion collapsed this staircase, we have to go down! "
			elif answer == "down" :
				print "F.R.A.N.K: excellent choice sir! "
			print " * you enter a long, mysterius, dark hallway, and as F.R.A.N.K. turns on the flashlight in your fingers, you see a mysterious creature scuddle away* "
			time.sleep(7)
			print "*There is one doorway to your left and one to your right*"
			answer = raw_input( name + "would you like to go to the 'left' or the 'right'? ")
			if answer == "left":
				print " *the door opens, at first, you see nothing. But you hear a groaning noise coming from the dark corner of the room* "
				answer = raw_input("Do you approach 'go' the corner or 'leave' the room")
				if answer == "go":
					print "*you discover that the shape in the corner is another prisoner, who has dug a tunnel out of the prison*"
					print "*the prisoner is seemingly deceptive and intimierdating"
					answer = raw_input("Do you choose to trust the prisoner? 'yes' or 'no' ")
					if answer == "yes" :
						print "Congratualtions, you have escaped the prison and won"
						print "THE END"
						print ("\n")
						print "Made by Corey Schultz"
						print "Hack BCA III"
						print "4/2/16 - 4/3/16"
						print "Python" 
						time.sleep(8)
					elif answer == "no" :
						print "the alien has caught up to you, due to your lack of decisiveness"
						print "THE END"
						print ("\n")
						print "Made by Corey Schultz"
						print "Hack BCA III"
						print "4/2/16 - 4/3/16"
						print "Python" 
						time.sleep(8)
				elif answer == "leave" :
					print "*you exit the room, but the door to the right is locked, you are now forced to continue down the hallway*"
					print "*at the end of the hallway you reach a door, which when opened reveals a blinding light*"
					print ("\n")
					print "Made by Corey Schultz"
					print "Hack BCA III"
					print "4/2/16 - 4/3/16"
					print "Python" 
			elif answer == "right" :
				answer = raw_input("the door to the right is locked. You may now either go to the door on the 'left' or 'continue' down the hallway ")
				if answer == "left" :
					print " *the door opens, at first, you see nothing. But you hear a groaning noise coming from the dark corner of the room* "
					answer = raw_input("Do you approach 'go' the corner or 'leave' the room")
					if answer == "go":
						print "*you discover that the shape in the corner is another prisoner, who has dug a tunnel out of the prison*"
						print "*the prisoner is seemingly deceptive and intimierdating"
						answer = raw_input("Do you choose to trust the prisoner? 'yes' or 'no' ")
						if answer == "yes" :
							print "Congratualtions, you have escaped the prison and won"
							print "THE END"
							print ("\n")
							print "Made by Corey Schultz"
							print "Hack BCA III"
							print "4/2/16 - 4/3/16"
							print "Python" 
							time.sleep(8)
						elif answer == "no" :
							print "the alien has caught up to you, due to your lack of decisiveness"
							print "THE END"
							print ("\n")
							print "Made by Corey Schultz"
							print "Hack BCA III"
							print "4/2/16 - 4/3/16"
							print "Python" 
							time.sleep(8)
					elif answer == "leave" :
						print "*you exit the room, but the door to the right is locked, you are now forced to continue down the hallway*"
						print "*at the end of the hallway you reach a door, which when opened reveals a blinding light*"
						print ("\n")
						print "Made by Corey Schultz"
						print "Hack BCA III"
						print "4/2/16 - 4/3/16"
						print "Python" 
						time.sleep(8)

				elif answer == "continue":
					print "*at the end of the hall you find an air vent*"
					time.sleep(5)
					print "*after 20 minutes of crawling and climbing through tight spaces, you finally reach the outside. Congratulations, you are free*"
					time.sleep(6)
					print "*now only if there were a way to remove F.R.A.N.K. ..."
					time.sleep(2)
					print "THE END"
					print ("\n")
					print "Made by Corey Schultz"
					print "Hack BCA III"
					print "4/2/16 - 4/3/16"
					print "Python" 
					time.sleep(6)

# "if" break point


	else :
		print "F.R.A.N.K:: I quit , go home"
		time.sleep(2)
		print "F.R.A.N.K has exploded and blasted a hole in your brain. Just thought I should let you know ;)"
		print "THE END"
		print ("\n")
		print "Made by Corey Schultz"
		print "Hack BCA III"
		print "4/2/16 - 4/3/16"
		print "Python" 
		time.sleep(7)
else :
	print "Klyde: Ok smart guy let's get serious here, this is a prison"
	answer == raw_input("Type 'orange' or 'gray' and hit the enter button ").lower()
	if answer == "gray" or answer == "orange" :
			time.sleep(3)
	print "Klyde: Ah! Gray! What a fantastic choice! The hippopotamus herd! They'll be glad to have a man of your -er- type joining them. *giggles under breath* "
	print "Klyde: My apologies but I do have more important work to be getting back to"
	time.sleep(11)
	print "Klyde: F.R.A.N.K. , the AI chip we have installed in your brain will take it from here. "
	print "Klyde: Goodluck out there kid.*winks* "
	time.sleep(9)
	print "F.R.A.N.K: Welcome inmate #10G67D"
	time.sleep(6)
	name = raw_input("Please type in your name and press 'enter' ")
	print "You : Please, call me " + name 
	time.sleep(5)
	print "F.R.A.N.K.: Alright,  I will be the voice in your head from now on, " + name
	time.sleep(5)
	print "You : Great"
	time.sleep(5)
	print "F.R.A.N.K: Although I am artificial intelligence, I can still detect sarcasm sir and I do not appreciate it "
	time.sleep(5)
	print "You : Golly, you really are in my head"
	time.sleep(5)
	print "F.R.A.N.K: Johnson Experimental Institute : Founded in the 1930's by the late-great Cave Johnson himself! You may remember him for his most famous quote : 'when life gives you-' "
	time.sleep(8)
	print "You : yeah, I've heard it before bro "
	time.sleep(4)
	print "F.R.A.N.K: well then, as we approach a fork in the hallway here please select your path"
	answer = raw_input("Please type 'left' or 'right' ").lower()
	if answer == "left" or answer == "right" :
		print "F.R.A.N.K: Right it is,please watch your step as we walk through this hallway"
		time.sleep(5)
		print "F.R.A.N.K: Now there is falling debris so please be careful"
		time.sleep(5)
		print " *BANG* *Giant Crashing Noise*"
		answer == raw_input("Please insert a response to that event ")
		time.sleep(4)
		print "F.R.A.N.K: I am going to pretend I didn't hear that " + name
		time.sleep(4)
		print "You : holy jolly ranchers, what is this place"
		time.sleep(4)
		print "F.R.A.N.K: wait, I think I hear something..."
		time.sleep(2)
		print " *A GIANT COCKROACH DROPS THROUGH THE CEILING LOOKING LIKE A METEOR* "
		answer = raw_input("Sir, you must decie quickly, do we 'fight' or 'run' ")
		if answer == "fight" :
			print " *I think you know that you're dead* "
			answer = raw_input("Would you like to try again? type 'yes'or 'no' ")
			if answer == "yes" :
				print "lol too bad you lost"
				print ("\n")
				print "Made by Corey Schultz"
				print "Hack BCA III"
				print "4/2/16 - 4/3/16"
				print "Python" 
				time.sleep(4)
			elif answer == "no" :
				print "ok, goodbye"
				print ("\n")
				print "Made by Corey Schultz"
				print "Hack BCA III"
				print "4/2/16 - 4/3/16"
				print "Python" 
				time.sleep(4)
		elif answer == "run" :
			print "F.R.A.N.K: OK, let's get out of here " + name
			time.sleep(3)
			print " *You are now sprinting at full speed down a collapsing hallway, realizing how out of shape you are and that probably stealing that candy bar was not worth all this trouble* "
			time.sleep(10)
			answer = raw_input("Sir, we have reached a dead end with two staricases. You must quickly decide! 'up' or 'down' ")
			if answer == "up" :
				print "F.R.A.N.K: oh no, the explosion collapsed this staircase, we have to go down! "
			elif answer == "down" :
				print "F.R.A.N.K: excellent choice sir! "
			print " * you enter a long, mysterius, dark hallway, and as F.R.A.N.K. turns on the flashlight in your fingers, you see a mysterious creature scuddle away* "
			time.sleep(7)
			print "*There is one doorway to your left and one to your right*"
			answer = raw_input( name + "would you like to go to the 'left' or the 'right'? ")
			if answer == "left":
				print " *the door opens, at first, you see nothing. But you hear a groaning noise coming from the dark corner of the room* "
				answer = raw_input("Do you approach 'go' the corner or 'leave' the room")
				if answer == "go":
					print "*you discover that the shape in the corner is another prisoner, who has dug a tunnel out of the prison*"
					print "*the prisoner is seemingly deceptive and intimierdating"
					answer = raw_input("Do you choose to trust the prisoner? 'yes' or 'no' ")
					if answer == "yes" :
						print "Congratualtions, you have escaped the prison and won"
						print "THE END"
						print ("\n")
						print "Made by Corey Schultz"
						print "Hack BCA III"
						print "4/2/16 - 4/3/16"
						print "Python" 
						time.sleep(8)
					elif answer == "no" :
						print "the cockroach has caught up to you, due to your lack of decisiveness"
						print "THE END"
						print ("\n")
						print "Made by Corey Schultz"
						print "Hack BCA III"
						print "4/2/16 - 4/3/16"
						print "Python" 
						time.sleep(8)
				elif answer == "leave" :
					print "*you exit the room, but the door to the right is locked, you are now forced to continue down the hallway*"
			elif answer == "right" :
				answer = raw_input("the door to the right is locked. You may now either go to the door on the 'left' or 'continue' down the hallway ")
				print "*at the end of the hallway you reach a door, which when opened reveals a blinding light*"
				print "Made by Corey Schultz"
				print "Hack BCA III"
				print "4/2/16 - 4/3/16"
				print "Python" 
				if answer == "left" :
					print " *the door opens, at first, you see nothing. But you hear a groaning noise coming from the dark corner of the room* "
					answer = raw_input("Do you approach 'go' the corner or 'leave' the room")
					if answer == "go":
						print "*you discover that the shape in the corner is another prisoner, who has dug a tunnel out of the prison*"
						print "*the prisoner is seemingly deceptive and intimierdating"
						answer = raw_input("Do you choose to trust the prisoner? 'yes' or 'no' ")
						if answer == "yes" :
							print "Congratualtions, you have escaped the prison and won"
							print "THE END"
							print "Made by Corey Schultz"
							print "Hack BCA III"
							print "4/2/16 - 4/3/16"
							print "Python" 
							time.sleep(8)
						elif answer == "no" :
							print "the cockroach has caught up to you, due to your lack of decisiveness"
							print "THE END"
							print "Made by Corey Schultz"
							print "Hack BCA III"
							print "4/2/16 - 4/3/16"
							print "Python" 
							time.sleep(8)
					elif answer == "leave" :
						print "*you exit the room, but the door to the right is locked, you are now forced to continue down the hallway*"
						print "*at the end of the hallway you reach a door, which when opened reveals a blinding light*"
						print "*at the end of the hallway you reach a door, which when opened reveals a blinding light*"
						print "Made by Corey Schultz"
						print "Hack BCA III"
						print "4/2/16 - 4/3/16"
						print "Python" 
						time.sleep(8)
				elif answer == "continue" :
					print "*at the end of the hall you find an air vent*"
					time.sleep(5)
					print "*after 20 minutes of crawling and climbing through tight spaces, you finally reach the outside. Congratulations, you are free*"
					time.sleep(6)
					print "*now only if there were a way to remove F.R.A.N.K. ..."
					time.sleep(2)
					print "THE END"
					print "Made by Corey Schultz"
					print "Hack BCA III"
					print "4/2/16 - 4/3/16"
					print "Python" 
					time.sleep(6)

# end of game