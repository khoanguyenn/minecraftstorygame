from mcpi import minecraft 
mc = minecraft.Minecraft.create()
x = -15
y = -6
z = -1
def buildTimePortal(x,y,z):
	#Time portal
	mc.setBlocks(x,y,z+1,x+5,y+5,z+1,89)
	mc.setBlocks(x+1,y,z+1,x+4,y+4,z+1,0)
	mc.setBlocks(x+1,y+5,z+1,x+4,y+5,z+1,9)
	mc.setBlocks(x,y,z,x+5,y+5,z,42)
	mc.setBlocks(x+1,y+1,z,x+4,y+4,z,0)
def buildTimeMachine(x,y,z):
	#Iron foudation
	mc.setBlocks(x+1,y,z,x+2,y,z+3,42)
	#Bottom-Side
	mc.setBlocks(x,y,z,x,y,z+3,67,4)
	mc.setBlocks(x+3,y,z,x+3,y,z+3,67,5)
	#Top-side
	mc.setBlocks(x,y+1,z,x,y+1,z+3,44)
	mc.setBlocks(x+3,y+1,z,x+3,y+1,z+3,44)
	#Control panelminigame.
	mc.setBlocks(x+1,y+1,z+3,x+2,y+1,z+3,42)
	#Chair
	mc.setBlocks(x+1,y+1,z+1,x+2,y+1,z+1,67,3)
def tree(x,y,z):
	mc.setBlock(x,y,z,17)
	mc.setBlocks(x,y+1,z,x,y+2,z,18)
def buildLaboratory(x,z):
	mc.setBlocks(x,y,z,x+31,y+7,z+60,42)		#Create a big cube
	mc.setBlocks(x+14,y,z+35,x+17,y+7,z+56,89) 	#Lighting main lab
	mc.setBlocks(x+14,y,z+2,x+17,y+7,z+31,89) 	#Lighting hall
	mc.setBlocks(x+12,y+1,z+1,x+19,y+6,z+32,0)	#Make room
	#Entrance to main lab
	mc.setBlocks(x+15,y+1,z+33,x+16,y+3,z+33,0)
	mc.setBlocks(x+15,y+4,z+33,x+16,y+4,z+33,44)
	for i in range(0,45,11):
		#Lighting system
		mc.setBlocks(x+2,y,z+i+2,x+9,y+7,z+i+9,89)
		#Make room
		mc.setBlocks(x+1,y+1,z+i+1,x+10,y+6,z+i+10,0)
		#Make door 
		mc.setBlocks(x+11,y+1,z+i+5,x+11,y+2,z+i+6,0)
		mc.setBlocks(x+11,y+3,z+i+5,x+11,y+3,z+i+6,44)  
		#Table and chair
		mc.setBlocks(x+3,y+1,z+i+4,x+6,y+1,z+i+7,42)
		mc.setBlocks(x+4,y+1,z+i+4,x+4,y+1,z+i+7,0)
		mc.setBlocks(x+3,y+1,z+i+5,x+3,y+1,z+i+6,67,1)
		tree(x+1,y+1,z+i+1)		#Tree for decoration
		tree(x+1,y+1,z+i+10) 	#Tree for decoration
		tree(x+10,y+1,z+i+1) 	#Tree for decoration
		tree(x+10,y+1,z+i+10) 	#Tree for decoration
		mc.setBlock(x+5,y+1,z+i+10,58)	#Crafting table
		mc.setBlock(x+6,y+1,z+i+10,54)	#Chest
		#Lighting system
		mc.setBlocks(x+22,y,z+i+2,x+29,y+7,z+i+9,89)
		#Make room
		mc.setBlocks(x+21,y+1,z+i+1,x+30,y+6,z+i+10,0)
		#Make door
		mc.setBlocks(x+20,y+1,z+i+5,x+20,y+2,z+i+6,0)
		mc.setBlocks(x+20,y+3,z+i+5,x+20,y+3,z+i+6,44)
		#Table and chair
		mc.setBlocks(x+25,y+1,z+i+4,x+28,y+1,z+i+7,42)
		mc.setBlocks(x+27,y+1,z+i+4,x+27,y+1,z+i+7,0)
		mc.setBlocks(x+28,y+1,z+i+5,x+28,y+1,z+i+6,67,0)
		tree(x+30,y+1,z+i+1)	#Tree for decoration
		tree(x+30,y+1,z+i+10) 	#Tree for decoration
		tree(x+21,y+1,z+i+1)	#Tree for decoration
		tree(x+21,y+1,z+i+10) 	#Tree for decoration
		mc.setBlock(x+25,y+1,z+i+10,58)	#Crafting table
		mc.setBlock(x+26,y+1,z+i+10,54)	#Chest
	mc.setBlocks(x+1,y+1,z+34,x+30,y+6,z+59,0) #Clear main lab
	#Time portal
	buildTimePortal(x+13,y+1,z+58)
	#Time machine
	buildTimeMachine(x+14,y+1,z+51)
buildLaboratory(x,z)

