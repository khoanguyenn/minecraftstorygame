from mcpi import minecraft
mc = minecraft.Minecraft.create()
def wheat(x,z,a,b):
    p=mc.player.getPos()
    y=4
    mc.setBlocks(x,y-1,z,x+a,y-1,z+b,17,0)#gỗ    
    mc.setBlocks(x,y,z,x,y,z+b,85)#hàng rào
    mc.setBlocks(x,y,z,x+a,y,z,85)
    mc.setBlocks(x+a,y,z,x+a,y,z+b,85)
    mc.setBlocks(x,y,z+b,x+a,y,z+b,85)
    for i in range(1,a-1,5):
        if a-1-i<5:
            k=a-1-i
            mc.setBlocks(x+i,y-1,z+1,x+i+k,y-1,z+b-1,60,7)
            mc.setBlocks(x+i,y,z+1,x+i+k,y,z+b-1,59,7)
        else:
            mc.setBlocks(x+i,y-1,z+1,x+i+3,y-1,z+b-1,60,7)
            mc.setBlocks(x+i,y,z+1,x+i+3,y,z+b-1,59,7)
            mc.setBlocks(x+i+4,y-1,z+1,x+i+4,y-1,z+b-1,9)
        print(i)
mc.postToChat("Building the southeast wheat field...")
wheat(-55,19,45,90)
mc.postToChat("Done!")
mc.postToChat("Building the southwest wheat field...")
wheat(9,60,100,50)
mc.postToChat("Done!")
mc.postToChat("Complete to build the farm.")