from mcpi import minecraft
mc = minecraft.Minecraft.create()
def statue(x,z):
    p=mc.player.getPos()
    y= 4
    mc.setBlocks(x,y,z,x+8,y,z+8,44,5)#thềm
    mc.setBlocks(x+1,y,z+1,x+7,y,z+7,89)
    mc.setBlocks(x+2,y,z+2,x+6,y,z+6,5)
    mc.setBlocks(x+4,y,z+4,x+5,y+9,z+4,4)#người
    mc.setBlocks(x+4,y+8,z+4,x+5,y+9,z+5,98)    #Head
    mc.setBlocks(x+4,y+5,z+4,x+5,y+7,z+4,42)    #Body
    mc.setBlocks(x+4,y+1,z+4,x+5,y+1,z+4,42)    #Shoe
    mc.setBlocks(x+6,y+5,z+4,x+6,y+7,z+4,98)#tay trái
    mc.setBlocks(x+6,y+5,z+5,x+6,y+5,z+8,85)
    mc.setBlocks(x+3,y+7,z+4,x+3,y+7,z+6,98)#tay phải
    mc.setBlocks(x+3,y+8,z+6,x+3,y+13,z+6,85)#cột cờ
    mc.setBlocks(x+2,y+11,z+6,x+2,y+13,z+6,35,14)#cờ 
    mc.setBlocks(x+1,y+11,z+5,x+1,y+13,z+5,35,14)#cờ
    mc.setBlocks(x,y+11,z+4,x,y+13,z+4,35,14)#cờ
statue(-4,-4)    
