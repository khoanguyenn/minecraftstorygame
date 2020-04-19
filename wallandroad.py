from mcpi import minecraft
mc = minecraft.Minecraft.create()
x = -3
y = 13
z = 119
#Roadmap
mc.postToChat("Setting road and pathway...")
mc.setBlocks(-2,3,-128,2,3,128,13) 	#Set gravel south-north
mc.setBlocks(-128,3,-2,128,3,2,13) 	#Set gravel west-east
mc.setBlocks(-10,3,10,10,3,-10,13) 	#Set roundabout gravel
mc.setBlocks(3,3,31,48,3,33,13) 	#Top villager's house path
mc.setBlocks(2,3,45,48,3,47,13) 	#Bottom villager's house path
mc.setBlocks(-75,3,-3,-71,3,-33,13) #Castle's path
mc.setBlocks(12,3,-89,3,3,-87,13)	#Gravelyard's path
mc.setBlocks(39,3,-22,37,3,-3,13)	#Pagoda's path
mc.setBlocks(61,3,-63,65,3,-3,13)	#North-east villager main path
mc.setBlocks(98,3,-46,66,3,-44,13)	#Top villager's house path
mc.setBlocks(98,3,-56,66,3,-54,13)
mc.postToChat("Done!")
#Set stone wall
mc.postToChat("Building wall...")
mc.setBlocks(119,4,119,-119,12,-118,1)
mc.setBlocks(116,4,116,-116,12,-115,0)
mc.postToChat("Done!")
#Set gate
mc.postToChat("Building gate...")
for i in range(0,6,1):
	if i >= 3: k = 3
	else: k = i 
	mc.setBlocks(x+k,y+k,z,x+6-k,y+k,z-2,1)

for i in range(0,3,1):
	mc.setBlocks(x+i+1,y+i-1,z,x+5-i,y+i-1,z-2,0)
mc.setBlocks(x+1,4,z,x+5,y-1,z-2,0)
for i in range(0,3,1):
	mc.setBlocks(x+i+1,y+i-1,z-1,x+5-i,y+i-1,z-1,85)
mc.setBlocks(x+1,y-2,z-1,x+5,y-5,z-1,85,3)
mc.postToChat("Done!")
mc.postToChat("Roadmap and wall have been completed.")