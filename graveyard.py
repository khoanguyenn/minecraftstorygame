import random
from mcpi import minecraft
mc = minecraft.Minecraft.create()
x = 13
z = -73
a = 60
b = 30
def buildGraveYard(x,z):

	mc.setBlocks(x,4,z,x+a,4,z-b,85) #Fence
	mc.setBlocks(x,4+1,z,x+a,4+1,z-b,44)
	mc.setBlocks(x+1,4,z-1,x+59,4+1,z-29,0)

	mc.setBlocks(x,4,z-13,x,4+5,z-17,17) #Gate
	mc.setBlocks(x,4,z-14,x,4+4,z-16,0) 

	mc.setBlocks(x,4-1,z-14,x+a-1,4-1,z-16,13) #Gravel road

	for i in range(0,int(b/2-5),6):
		for j in range(0,a,5):
			mc.setBlock(x+3+j,4,z-3-i,4)
			mc.setBlock(x+3+j,4+1,z-3-i,44)
			mc.setBlock(x+3+j,4,z-6-i,random.randint(37,38))
			mc.setBlocks(x+3+j,4,z-4-i,x+3+j,4,z-5-i,44)

	for i in range(0,int(b/2-5),6):
		for j in range(0,a,5):
			mc.setBlock(x+3+j,4,z-21-i,4)
			mc.setBlock(x+3+j,4+1,z-21-i,44)
			mc.setBlock(x+3+j,4,z-18-i,random.randint(37,38))
			mc.setBlocks(x+3+j,4,z-19-i,x+3+j,4,z-20-i,44)

buildGraveYard(x,z)