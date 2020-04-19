from mcpi import minecraft
mc = minecraft.Minecraft.create()
def house(x,z):
    air=0
    plank=5
    cobblestone=4
    stair=53
    wood=17
    door=64
    l=10
    w=7
    x-=1
    y=4
    z-=1
    mc.setBlocks(x+1,y,z+1,x+l,y+7,z+w,5)#basic 
    mc.setBlocks(x+5,y+1,z+1,x+6,y+4,z+1,0)#cửa
    mc.setBlocks(x+2,y+1,z+2,x+l-1,y+8,z+w-1,0)
    mc.setBlocks(x+1,y+7,z+1,x+l,y+7,z+1,0)
    mc.setBlocks(x+1,y+7,z+w,x+l,y+7,z+w,0)
    for i in range(0,4):#cột gỗ
        mc.setBlocks(x+1+3*i,y,z+1,x+1+3*i,y+5,z+1,17,0)
        mc.setBlocks(x+1+3*i,y,z+w,x+1+3*i,y+5,z+w,17,0)
    mc.setBlocks(x+l-1,y+2,z+1,x+l-2,y+3,z+1,20)#cửa sổ
    mc.setBlocks(x+2,y+2,z+1,x+3,y+3,z+1,20)
    mc.setBlocks(x+1,y+2,z+3,x+1,y+3,z+5,20)
    mc.setBlocks(x+l,y+2,z+3,x+l,y+3,z+5,20)
    mc.setBlocks(x+3,y+1,z+w,x+3,y+4,z+w,20)
    mc.setBlocks(x+l-2,y+1,z+w,x+l-2,y+4,z+w,20)
    mc.setBlocks(x+4,y+1,z+w-1,x+7,y+3,z+w-1,4)
    mc.setBlocks(x+5,y+1,z+w-1,x+6,y+12,z+w-1,4)
    mc.setBlocks(x+5,y+1,z+w-1,x+6,y+2,z-w-1,0)
    mc.setBlock(x+4,y+1,z+w-2,67,2)
    mc.setBlock(x+7,y+1,z+w-2,67,2)
    mc.setBlock(x+4,y+3,z+w-1,67,0)
    mc.setBlock(x+7,y+3,z+w-1,67,1)
    #Bed
    mc.setBlock(x+2,y+1,z+w-1,26,8)
    mc.setBlock(x+2,y+1,z+w-2,26,0)
    mc.setBlock(x+l-1,y+1,z+w-1,26,8)
    mc.setBlock(x+l-1,y+1,z+w-2,26,0)
    mc.setBlock(x+2,y+1,z+2,54,5)
    mc.setBlock(x+l-1,y+1,z+2,54,4)
    mc.setBlock(x+2,y+1,z+3,58)
    mc.setBlock(x+l-1,y+1,z+3,58)
    #Roof
    for i in range(0,4):
        mc.setBlocks(x,y+5+i,z+i,x+l+1,y+5+i,z+i,53,2)
        mc.setBlocks(x,y+5+i,z+w+1-i,x+l+1,y+5+i,z+w+1-i,53,3)
    mc.setBlocks(x,y+8,z+4,x+l+1,y+8,z+4,5)#mái
    mc.setBlocks(x+2,y,z+2,x+l-1,y,z+w-1,4)#nền
    mc.setBlocks(x+5,y,z+1,x+6,y,z+1,53,2)#trym
house(9,50)
house(9,36)
house(9,22)
house(24,50)
house(24,36)
house(24,22)
house(39,50)
house(39,36)
house(39,22)
#Northeast section
house(73,-42)
house(73,-54)
house(73,-66)
house(88,-42)
house(88,-54)
house(88,-66)
