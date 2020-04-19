from mcpi import minecraft
mc = minecraft.Minecraft.create()
x = 69
y = 4
z = -27
a = 20
b = 40

def buildGarden(x,z):
	#
	mc.setBlocks(x,y,z,x+b,y,z+a,17) #Build surrouding log
	mc.setBlocks(x,y+1,z,x+b,y+6,z+a,85) #Place fences
	mc.setBlocks(x+1,y+1,z,x+b-1,y+5,z+a,0) #Cave inside
	mc.setBlocks(x,y+1,z+1,x+b,y+5,z+a-1,0) #Cave inside
	mc.setBlocks(x,y+7,z,x+b,y+7,z+a,18) #Set leave to the top
	for i in range(1,a,2):
		if i < a-1:
			mc.setBlocks(x+1,y,z+i,x+b-1,y,z+i,12) #Set sand
			mc.setBlocks(x+1,y,z+i+1,x+b-1,y,z+i+1,9) #Set water
			#Set leave & log
			mc.setBlocks(x-1,y+4,z+i+1,x-1,y+7,z+i+1,18)
			mc.setBlocks(x+b+1,y+4,z+i+1,x+b+1,y+7,z+i+1,18)
			mc.setBlocks(x,y+7,z+i+1,x+b,y+7,z+i+1,17)
			#Set sugarcane
			mc.setBlocks(x+1,y+1,z+i,x+b-1,y+4,z+i,83)
		else:
			mc.setBlocks(x+1,y,z+i,x+b-1,y,z+i,12) #Set sand
			mc.setBlocks(x+1,y+1,z+i,x+b-1,y+4,z+i,83) #Set sugarcane

buildGarden(x,z)