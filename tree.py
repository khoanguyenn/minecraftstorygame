from mcpi import minecraft
mc = minecraft.Minecraft.create()
def growTree(x,z,direction):
	y = 4
	#Bottom
	mc.setBlocks(x-1,y+3,z,x+1,y+3,z,18)
	mc.setBlocks(x,y+3,z-1,x,y+3,z+1,18)
	#Top
	mc.setBlocks(x,y+6,z-1,x,y+6,z+1,18)
	mc.setBlocks(x-1,y+6,z,x+1,y+6,z,18)
	mc.setBlocks(x+1,y+4,z+1,x-1,y+5,z-1,18)
	#Log
	mc.setBlocks(x,y,z,x,y+5,z,17)
	#Torch
	if direction: 
		#For north-south direction
		mc.setBlock(x+1,y+2,z,50,1)
		mc.setBlock(x-1,y+2,z,50,2)
	else: 
		#For east-west direction
		mc.setBlock(x,y+2,z-1,50,4)
		mc.setBlock(x,y+2,z+1,50,3)
#West
mc.postToChat("West")
for i in range(0,110,11):
	for j in range(0,9,8):
		growTree(-10-i,4-j,False)
#East
mc.postToChat("East")
for i in range(0,110,11):
	for j in range(0,9,8):
		growTree(109-i,4-j,False)
#South
mc.postToChat("South")
for i in range(0,110,11):
	for j in range(0,9,8):
		growTree(-4+j,109-i,True)
#North
mc.postToChat("North")
for i in range(0,110,11):
	for j in range(0,9,8):
		growTree(-4+j,-10-i,True)