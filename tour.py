#Vietnamese German University
#By Team 4
#Building function for castle
#Connections used: Minecraft API
from mcpi import minecraft
mc = minecraft.Minecraft.create()
from lab import buildTimeMachine
import time
import game
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  #Establish input
GPIO.setup(6,GPIO.IN) #Enter button
GPIO.setup(5,GPIO.IN) #Exit button
def Move(x1,y1,z1,x2,y2,z2):
	t = 0.04
	if (x2 - x1 > 0):
		while x1 < x2:
			mc.player.setPos(x1,y1,z1)
			x1 = x1 + 0.2
			time.sleep(t)
	elif (x2 - x1 < 0):
		while x1 > x2:
			mc.player.setPos(x1,y1,z1)
			x1 = x1 - 0.2
			time.sleep(t)
	if (z2 - z1 > 0):
		while z1 < z2:
			mc.player.setPos(x1,y1,z1)
			z1 = z1 + 0.2
			time.sleep(t)
	elif (z2 - z1 < 0):
		while z1 > z2:
			mc.player.setPos(x1,y1,z1)
			z1 = z1 - 0.2
			time.sleep(t)
#SCENCE 1 - LABORATORY
mc.postToChat("Let's take a tour around this laboratory")
Move(0.5,-5,0.5,0.5,-5,4.5)
Move(0.5,-5,4.5,7.5,-5,4.5)
mc.postToChat("This is a typical room for scientist")
time.sleep(3)
Move(7.5,-5,4.5,0.5,-5,4.5)
Move(0.5,-5,4.5,0.5,-5,27.5)
mc.postToChat("And... this is my room, Steve's room")
time.sleep(3)
Move(0.5,-5,27.5,-6.5,-5,27.5)
Move(-6.5,-5,27.5,-6.5,-5,23.5)
Move(-6.5,-5,23.5,-10.5,-5,23.5)
Move(-10.5,-5,23.5,-10.5,-5,27.5)
mc.postToChat("I have been working since last night")
time.sleep(5)
mc.postToChat("I need to have a break")
mc.player.setPos(-13.5,-5.5,21.5)
time.sleep(5)
mc.player.setPos(-10.5,-5,27.5)
time.sleep(5)
mc.postToChat("Did i just take a nap ?")
time.sleep(5)
mc.postToChat("Dad help meeee...")
time.sleep(3)
mc.postToChat("Sarah ?")
Move(-10.5,-5,27.5,0.5,-5,27.5)
Move(0.5,-5,27.5,0.5,-5,37.5)
mc.postToChat("Sarahh... Oh no...")
time.sleep(3)
mc.postToChat("I need to close the portal now")
time.sleep(3)
Move(0.5,-5,37.5,7.5,-5,37.5)
mc.postToChat("Level 1")
game.Minigame(10,-5,37,1,0,False)
time.sleep(3)
Move(7.5,-5,37.5,7.5,-5,48.5)
mc.postToChat("Level 2")
game.Minigame(10,-5,48,1,0,False)
time.sleep(3)
Move(7.5,-5,48.5,-5.5,-5,48.5)
mc.postToChat("Level 3")
game.Minigame(-10,-5,48,1,-1,False)
time.sleep(3)
Move(-5.5,-5,48.5,-5.5,-5,37.5)
mc.postToChat("Level 4")
game.Minigame(-10,-5,37,1,-1,False) 
time.sleep(3)
mc.postToChat("I have to get back to my room now...")
time.sleep(3)
Move(-5.5,-5,37.5,0.5,-5,37.5)
Move(0.5,-5,37.5,0.5,-5,27.5)
Move(0.5,-5,27.5,-6.5,-5,27.5)
Move(-6.5,-5,27.5,-6.5,-5,23.5)
Move(-6.5,-5,23.5,-10.5,-5,23.5)
Move(-10.5,-5,23.5,-10.5,-5,27.5)
mc.postToChat("I'm so tired")
time.sleep(5)
mc.player.setPos(-13.5,-5.5,21.5)
time.sleep(8)
mc.postToChat("30 years later...")
time.sleep(8)
mc.postToChat("Argg...")
mc.player.setPos(-10.5,-5,27.5)
time.sleep(3)
Move(-10.5,-5,27.5,-10.5,-5,23.5)
Move(-10.5,-5,23.5,-6.5,-5,23.5)
Move(-6.5,-5,23.5,-6.5,-5,27.5)
Move(-6.5,-5,27.5,0.5,-5,27.5)
mc.postToChat("Finally, the time machine has been completed")
time.sleep(3)
mc.postToChat("I'm not quite sure whether if it works or not...")
time.sleep(3)
mc.postToChat("But i want Sarah back!")
time.sleep(3)
Move(0.5,-5,27.5,0.5,-5,48.5)
while (GPIO.input(6) == True):
	mc.postToChat("Hold enter button to enter the time machine")
	time.sleep(2)
mc.player.setPos(0.5,-4,52.5)
mc.postToChat("Time machine: ready")
time.sleep(3)
mc.postToChat("Time portal: openning...")
time.sleep(3)
mc.postToChat("Time portal: ready")
time.sleep(3)
mc.postToChat("Jump!")
mc.player.setPos(-13.5,-5.5,21.5)
#SCENCE 2 - NOTCH'S KINGDOM
buildTimeMachine(-1,4,121) #Time machine arrive the city
mc.player.setPos(0.5,5,123.5) #On time machine
mc.postToChat("Ouchh, my head")
time.sleep(3)
mc.postToChat("What year is it ?")
time.sleep(3)
mc.postToChat("Oh gosh, the timer has broken")
time.sleep(3)
mc.postToChat("Anyway, let's take a look then...")
time.sleep(3)
Move(0.5,4,123.5,0.5,4,109.5)
mc.postToChat("Wow, look at those wheats, they're looked well")
time.sleep(3)
Move(0.5,4,109.5,0.5,4,88.5)
mc.postToChat("Are that villagers' houses ?")
time.sleep(3)
Move(0.5,4,88.5,0.5,4,72.5)
mc.postToChat("Hello ?...")
time.sleep(3)
mc.postToChat("Seem to be nobody here...")
time.sleep(3)
Move(0.5,4,72.5,0.3,4,46.5)
mc.postToChat("Let's take a look at the house, shall we ?")
time.sleep(3)
Move(0.3,4,46.5,13.5,4,46.5)
while (GPIO.input(6) == True):
	mc.postToChat("Hold enter button to enter the house")
	time.sleep(3)	
mc.player.setPos(13.5,5,52.5)
mc.postToChat("What a nice house !")
time.sleep(8)
while (GPIO.input(5) == True):
	mc.postToChat("Hold exit button to exit the house")
	time.sleep(3)
mc.player.setPos(13.5,4,46.5)
Move(13.5,4,46.5,0.5,4,46.5)
mc.postToChat("This place looks strange!")
time.sleep(3)
Move(0.5,4,46.5,0.5,4,32.5)
mc.postToChat("Anyway, let's go then...")
time.sleep(3)
Move(0.5,4,32.5,0.5,4,7.5)
mc.postToChat("That's Notch statue - a legend of Minecraft world")
time.sleep(3)
Move(0.5,4,7.5,7.5,4,7.5)
Move(7.5,4,7.5,7.5,4,0.5)
Move(7.5,4,0.5,38.5,4,0.5)
mc.postToChat("What a big pagoda !")
time.sleep(3)
Move(38.5,4,0.5,38.5,4,-20.5)
while (GPIO.input(6) == True):
	mc.postToChat("Hold enter button to enter pagoda")
	time.sleep(3)
mc.player.setPos(38.5,7,-30)
Move(38.5,7,-30,38.5,7,-43)
mc.postToChat("Why's nothing in here ?")
time.sleep(3)
while (GPIO.input(5) == True):
	mc.postToChat("Hold exit button to exit the pagoda")
	time.sleep(3)
mc.player.setPos(38.5,4,-20.5)
Move(38.5,4,-20.5,38.5,4,0.5)
Move(38.5,4,0.5,82.5,4,0.5)
mc.postToChat("Look at market on the right side")
time.sleep(3)
mc.postToChat("So colorful !!!")
time.sleep(3)
mc.postToChat("Hmm...")
time.sleep(3)
mc.postToChat("Are those bamboos ?")
time.sleep(3)
while (GPIO.input(5) == True):
	mc.postToChat("Hold exit button get back to the north statue")
	time.sleep(3)
mc.player.setPos(0.5,4,7.5)
Move(0.5,4,7.5,-6.5,4,7.5)
Move(-6.5,4,7.5,-6.5,4,0.5)
Move(-6.5,4,0.5,-72.5,4,0.5)
Move(-72.5,4,0.5,-72.5,4,7.5)
mc.postToChat("Urgg, I shouldn't go there, so scary") #Play some horror music ?
time.sleep(3)
Move(-72.5,4,7.5,-72.5,4,0.5)
Move(-72.5,4,0.5,-72.5,4,-30.5)
while (GPIO.input(6) == True):
	mc.postToChat("Hold enter button to enter the castle")
	time.sleep(3)
mc.player.setPos(-72.5,6,-49.5)
time.sleep(3)
Move(-72.5,6,-49.5,-72.5,6,-81.5)
mc.postToChat("That's look gorgeous")
time.sleep(3)
Move(-72.5,6,-81.5,-55.5,6,-81.5)
while (GPIO.input(6) == True):
	mc.postToChat("Hold enter button to enter the library")
	time.sleep(3)
mc.player.setPos(-55.5,22,-57.5)
mc.postToChat("Wow, that's a big library...")
time.sleep(3)
Move(-55.5,22,-57.5,-65.5,22,-57.5)
mc.postToChat("This place seems to be not my place")
time.sleep(3)
mc.postToChat("Because I only see historical books")
time.sleep(3)
Move(-65.5,22,-57.5,-75.5,22,-57.5)
while (GPIO.input(5) == True):
	mc.postToChat("Hold exit button to exit the castle")
	time.sleep(3)
mc.player.setPos(-72.5,4,-30.5)
Move(-72.5,4,-30.5,-72.5,4,0.5)
Move(-72.5,4,0.5,-6.5,4,0.5)
Move(-6.5,4,0.5,-6.5,4,-6.5)
Move(-6.5,4,-6.5,0.5,4,-87.5)
mc.postToChat("That was a long way...")
time.sleep(3)
mc.postToChat("Oh, graveyard then... Why this weird tree stand here ?")
time.sleep(3)
Move(0.5,4,-87.5,13.5,4,-87.5)
mc.postToChat("That's scary. I'm not feeling comfortable now...")
time.sleep(3)
Move(13.5,4,-87.5,26.5,4,-87.5)
time.sleep(3)
mc.postToChat("That's alot of dead people")
time.sleep(3)
Move(26.5,4,-87.5,56.5,4,-87.5)
mc.postToChat("Wait, What ?")
time.sleep(3)
#Pause
Move(56.5,4,-87.5,56.5,4,-89.5)
mc.postToChat("Sarah ?")
time.sleep(3)
mc.postToChat("Sarah - 68 years old")
time.sleep(3)
#Pause
mc.postToChat("Oh no, I have to...")
time.sleep(3)
mc.player.setPos(56.5,2,-89.5)
time.sleep(5)
mc.player.setPos(-10.5,-5,27.5)
mc.postToChat("Did i just take a nap ?")
time.sleep(5)
mc.postToChat("Dad help meeee...")
time.sleep(3)
mc.player.setPos(-13.5,-5.5,21.5)
mc.postToChat("End.")
