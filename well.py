from mcpi import minecraft
mc=minecraft.Minecraft.create()
def buildWell(x,z):
	mc.setBlocks(x,4,z,x+4,4,z+4,4)
	mc.setBlocks(x+1,4,z+1,x+3,4,z+3,9)
	mc.setBlocks(x,5,z,x+4,8,z+4,85)
	mc.setBlocks(x,5,z+1,x+4,8,z+3,0)
	mc.setBlocks(x+1,5,z,x+3,8,z+4,0)
	mc.setBlocks(x,9,z,x+4,9,z+4,44,2)
buildWell(74,54)
buildWell(94,54)