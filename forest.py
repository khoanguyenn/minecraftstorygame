import random
from mcpi import minecraft
mc = minecraft.Minecraft.create()
#Tree
def tree(x,z):
    y=4
    mc.setBlocks(x-1,y+5,z-1,x+1,y+6,z+1,18) #Top-leave
    mc.setBlocks(x-2,y+3,z-2,x+2,y+4,z+2,18) #Bottom-leave
    mc.setBlocks(x,y,z,x,y+5,z,17,0)         #Log
#l : Initial x
#m : Initial y
#a : Length of x
#b : Length of y
def forest(l,m,a,b): 
    #Clear area
    mc.setBlocks(l-3,4,m-3,l+3+a,10,m+3+b,0)
    for i in range(0,a,5):
        for j in range(0,b,5):
            print(i,j)
            x=random.randint(l+i,l+i+2)
            z=random.randint(m+j,m+j+2)
            tree(x,z)
#For main program
forest(-112,10,55,100)
forest(77,-110,35,40)