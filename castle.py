from mcpi import minecraft
mc=minecraft.Minecraft.create()
x=-112
z=-112
mc.setBlocks(x,4,z,x+80,45,z+80,0)
mc.setBlocks(x,4,z,x+78,13,z+78,98)#thành
mc.setBlocks(x+4,4,z+4,x+74,13,z+74,0)
for i in range(0,79,2):#lưỡi cưa ngoài
    mc.setBlock(x,14,z+i,98)
    mc.setBlock(x+i,14,z,98)
    mc.setBlock(x+78,14,z+i,98)
    mc.setBlock(x+i,14,z+78,98)
for i in range(0,73,2):#lưỡi cưa trong
    mc.setBlock(x+3,14,z+3+i,98)
    mc.setBlock(x+3+i,14,z+3,98)
    mc.setBlock(x+75,14,z+3+i,98)
    mc.setBlock(x+3+i,14,z+75,98)
mc.setBlocks(x+37,4,z+75,x+41,9,z+78,0)#cổng thành
mc.setBlocks(x+38,10,z+75,x+40,10,z+78,0)
mc.setBlocks(x+39,11,z+75,x+39,11,z+78,0)
mc.setBlocks(x+15,4,z+15,x+63,21,z+63,4)#lâu đài tầng 1
mc.setBlocks(x+16,5,z+16,x+62,20,z+62,41)#phủ vàng
mc.setBlocks(x+17,6,z+17,x+61,19,z+61,0)
mc.setBlocks(x+37,4,z+63,x+41,9,z+62,0)#cổng lâu dài 
mc.setBlocks(x+38,10,z+63,x+40,10,z+62,0)
mc.setBlocks(x+39,11,z+63,x+39,11,z+62,0)
for i in range(16,63,9):#cửa sổ lầu 1
    mc.setBlocks(x+i,15,z+62,x+i+1,19,z+63,20)
    mc.setBlocks(x+15,15,z+i,x+16,19,z+1+i,20)
    mc.setBlocks(x+62,15,z+i,x+63,19,z+1+i,20)
    mc.setBlocks(x+i,15,z+15,x+i+1,19,z+16,20)
for i in range(15,65,2):#lưỡi cưa lầu 1
    mc.setBlock(x+15,22,z+i,4)
    mc.setBlock(x+i,22,z+15,4)
    mc.setBlock(x+63,22,z+i,4)
    mc.setBlock(x+i,22,z+63,4)
mc.setBlocks(x+20,22,z+20,x+58,35,z+58,1)#lâu đài tầng 2
mc.setBlocks(x+21,20,z+21,x+57,34,z+57,0)
mc.setBlocks(x+21,21,z+21,x+57,21,z+57,20)
for i in range(20,60,2):#lưỡi cưa lầu 2
    mc.setBlock(x+20,36,z+i,1)
    mc.setBlock(x+i,36,z+20,1)
    mc.setBlock(x+58,36,z+i,1)
    mc.setBlock(x+i,36,z+58,1)
mc.setBlocks(x+25,35,z+25,x+53,35,z+53,20)#kiếng sân thượng cho sáng :))
mc.setBlock(x+39,35,z+39,1)
for i in range(25,56,9):
    mc.setBlocks(x+i,29,z+58,x+i+1,32,z+58,20)
    mc.setBlocks(x+20,29,z+i,x+20,32,z+1+i,20)
    mc.setBlocks(x+58,29,z+i,x+58,32,z+1+i,20)
    mc.setBlocks(x+i,29,z+20,x+i+1,32,z+20,20)
mc.setBlocks(x+39,36,z+39,x+39,45,z+39,85)#cột cờ
mc.setBlocks(x+37,43,z+37,x+37,45,z+37,35,14)#cờ 
mc.setBlocks(x+38,43,z+38,x+38,45,z+38,35,14)#cờ
mc.setBlocks(x+39,43,z+39,x+39,45,z+39,35,14)#cờ
mc.setBlocks(x+37,4,z+20,x+41,5,z+77,35,14)#thảm đỏ
mc.setBlocks(x+37,5,z+78,x+41,5,z+78,67,3)#thềm
mc.setBlocks(x+37,4,z+79,x+41,4,z+79,67,3)
mc.setBlocks(x+36,6,z+20,x+42,9,z+23,35,15)#ngai vàng
mc.setBlocks(x+37,6,z+20,x+41,9,z+23,41) 
mc.setBlocks(x+38,7,z+22,x+40,9,z+23,0)
for i in range(2):
    mc.setBlocks(x+39-i,11-i,z+21,x+39+i,11-i,z+21,41)
for i in range(3):
    mc.setBlocks(x+39-i,12-i,z+20,x+39+i,12-i,z+20,35,15)
for i in range(23,55,2):
    mc.setBlocks(x+i,22,z+23,x+i,25,z+50,47)#sách
mc.setBlocks(-55,22,-55,-91,25,-55,47)#sách
for i in range(0,17):
    mc.setBlocks(x+54,5+i,z+36+i,x+57,5+i+2,z+36+i,1)
    mc.setBlocks(x+55,5+i,z+36+i,x+56,5+i,z+36+i,67,2)#cầu thang
    mc.setBlocks(x+55,5+i+1,z+36+i,x+56,5+i+4,z+36+i,0)
mc.setBlock(x+17,6,z+17,50,5)#torch
mc.setBlock(x+61,6,z+17,50,5)
mc.setBlock(x+17,6,z+61,50,5)
mc.setBlock(x+61,6,z+61,50,5)
for j in range(25,60,3):#cây 
    mc.setBlock(x+43,6,z+j,17)
    mc.setBlock(x+35,6,z+j,17)
    mc.setBlocks(x+35,7,z+j,x+35,8,z+j,18)
    mc.setBlocks(x+43,7,z+j,x+43,8,z+j,18)
