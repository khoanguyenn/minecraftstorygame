from mcpi import minecraft
mc=minecraft.Minecraft.create()
x=19
z=-64
def denlong(x,y,z):
    mc.setBlock(x,y,z,85)
    mc.setBlock(x,y-1,z,89)
def tree(x,z):
    y=4
    mc.setBlocks(x-1,y+5,z-1,x+1,y+6,z+1,18)#lá
    mc.setBlocks(x-2,y+3,z-2,x+2,y+4,z+2,18)#lá
    mc.setBlocks(x,y,z,x,y+5,z,17,0)#thân
mc.setBlocks(x,4,z,x+38,6,z+38,4)#thềm đá
for i in range(3):#bậc tam cấp
    mc.setBlocks(x+17,4,z+41-i,x+21,4+i,z+41-i,4)
    mc.setBlocks(x+18,4,z+41-i,x+20,4+i,z+41-i,67,3)
for i in range(0,3,2):#nóc tầng trệt
    mc.setBlocks(x+4+i,13+i/2,z+4+i,x+34-i,13+i/2,z+34-i,44,2)#ván gỗ
    mc.setBlocks(x+5+i,13+i/2,z+5+i,x+33-i,13+i/2,z+33-i,4)#đá
mc.setBlocks(x+5,7,z+5,x+33,12,z+33,17)#tàng trệt
mc.setBlocks(x+6,8,z+5,x+15,11,z+33,35)#tường trắng tầng trệt
mc.setBlocks(x+23,8,z+5,x+32,11,z+33,35)
mc.setBlocks(x+5,8,z+6,x+33,11,z+15,35)
mc.setBlocks(x+5,8,z+23,x+33,11,z+32,35)
mc.setBlocks(x+5,8,z+17,x+33,11,z+21,35)
mc.setBlocks(x+17,8,z+5,x+21,11,z+33,35)
mc.setBlocks(x+6,7,z+6,x+32,12,z+32,0)
denlong(x+6,12,z+6);denlong(x+6,12,z+32);denlong(x+32,12,z+6);denlong(x+32,12,z+32)
mc.setBlocks(x+17,7,z+33,x+21,11,z+33,0)#cửa
mc.setBlocks(x+6,6,z+6,x+32,6,z+32,89)#đá sáng
mc.setBlocks(x+7,15,z+7,x+31,15,z+31,85)#hàng rào tầng 1
mc.setBlocks(x+8,15,z+8,x+30,15,z+30,0)
for i in range(0,3,2):#nóc tầng 1
    mc.setBlocks(x+9+i,21+i/2,z+9+i,x+29-i,21+i/2,z+29-i,44,2)#ván gỗ
    mc.setBlocks(x+10+i,21+i/2,z+10+i,x+28-i,21+i/2,z+28-i,4)#đá
mc.setBlocks(x+11,15,z+11,x+27,21,z+27,17)#tầng 1
mc.setBlocks(x+11,15,z+12,x+27,21,z+26,35)#tường trắng tầng 1
mc.setBlocks(x+12,15,z+11,x+16,21,z+27,35)
mc.setBlocks(x+22,15,z+11,x+26,21,z+27,35)
mc.setBlocks(x+17,15,z+11,x+21,21,z+11,35)
mc.setBlocks(x+18,15,z+27,x+20,21,z+27,0)#cửa
mc.setBlocks(x+12,15,z+12,x+26,21,z+26,0)
denlong(x+12,21,z+12);denlong(x+12,21,z+26);denlong(x+26,21,z+12);denlong(x+26,21,z+26)
mc.setBlocks(x+12,14,z+12,x+26,14,z+26,89)#đá sáng
mc.setBlocks(x+13,23,z+13,x+25,23,z+25,44,2)
for i in range(0,18,7):
    tree(x+i,z+44)
    tree(x+i,z+51)
    tree(x+24+i,z+44)
    tree(x+24+i,z+51)
