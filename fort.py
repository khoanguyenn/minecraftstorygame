from mcpi import minecraft
mc=minecraft.Minecraft.create()
p=mc.player.getPos()
y=p.y
def fort(x,z):
    mc.setBlocks(x,4,z,x+7,14,z+7,1)
    mc.setBlocks(x-3,15,z-3,x+10,18,z+10,1)
    mc.setBlocks(x-2,16,z-2,x+9,18,z+9,0)
    for i in range(-3,10,2):
        mc.setBlock(x+i,19,z-3,1)
        mc.setBlock(x-3,19,z+i,1)
        mc.setBlock(x+10,19,z+i+1,1)
        mc.setBlock(x+i+1,19,z+10,1)
fort(-66,-20)
fort(-87,-20)
fort(-28,-45)
fort(-28,-102)
