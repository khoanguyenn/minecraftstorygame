import random
from mcpi import minecraft 
mc = minecraft.Minecraft.create()
x = 64
y = 4 
z = 8
a = 45 
b = 45
topcolor = [14,15,11,7]
def buildVendor(x,z):
	mc.setBlocks(x,y-1,z,x+4,y-1,z+3,4) #Build foundation

	mc.setBlocks(x,y,z,x+4,y,z+3,5)
	mc.setBlocks(x+1,y,z+1,x+3,y,z+2,0)

	mc.setBlocks(x,y+3,z-1,x+4,y+4,z+4,35,0) #Build top
	color = random.choice(topcolor) #Random color 
	for i in range(0,6,2):
		mc.setBlocks(x+i,y+3,z-1,x+i,y+4,z+4,35,color)
	mc.setBlocks(x,y+4,z-1,x+5,y+4,z-1,0) #Delete 2 left-over
	mc.setBlocks(x,y+4,z+4,x+5,y+4,z+4,0)

	mc.setBlocks(x,y+1,z,x+4,y+3,z+3,85) #Build fence
	mc.setBlocks(x+1,y+1,z,x+3,y+3,z+3,0)
	mc.setBlocks(x,y+1,z+1,x+5,y+3,z+2,0)

for j in range(0,b,10):
	for i in range(0,a,10):
		buildVendor(x+i,z+j)

