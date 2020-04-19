from mcpi import minecraft
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  #Establish input
GPIO.setup(13, GPIO.IN) #Play button
mc=minecraft.Minecraft.create()
#m=0 Face to the west
#m=-1 Face to the east
#gameover=True Build the minigame
#gameover=False Play the game
def minigame(x,y,z,v,m,gameover=True): #v is the hard of the game
    p=0 #Point
    k=y #Store value of y
    mc.setBlocks(x+1+m,k-2,z,x+1+m,k+5,z+1,42) #Background
    mc.setBlocks(x+1+m,k+4,z,x+1+m,k+4,z+1,35,14) #Back redline
    mc.setBlocks(x-m,k-2,z,x-m,k-1,z+1,89) #Glowstone
    mc.setBlocks(x-m,k,z,x-m,k,z+1,35,14) #Front redline
    mc.setBlocks(x-m,k+1,z,x-m,k+5,z+1,20) #Glass
    if not gameover:
        mc.postToChat('Help Steve to stablizing the energy column.')
        time.sleep(3)
        mc.postToChat('Keep the energy level under control.')
        time.sleep(3)
        mc.postToChat('So let begin in...')
        time.sleep(1)
        mc.postToChat('1')
        time.sleep(1)
        mc.postToChat('2')
        time.sleep(1)
        mc.postToChat('3')
        time.sleep(0.5)
        mc.postToChat('Let goooo..')
    while not gameover:
        if(GPIO.input(13) == False):   # Check input
            if k>=y:
                print("pressed")
                k-=1
                mc.setBlocks(x-m,y-2,z,x-m,y+5,z+1,20) # Reset the glass
                mc.setBlocks(x-m,y-2,z,x-m,k-1,z+1,89) # Reset the glow
                mc.setBlocks(x-m,k,z,x-m,k,z+1,35,14)  # Put the red bar
        time.sleep(v) # Raise the bar after v second(s)
        k+=1
        mc.setBlocks(x-m,y-2,z,x-m,y+5,z+1,20)  # Reset the glass
        mc.setBlocks(x-m,y-2,z,x-m,k-1,z+1,89)  # Reset the glow
        mc.setBlocks(x-m,k,z,x-m,k,z+1,35,14)   # Put the red bar

        if k==y+5: # Lose condition
            gameover=True
            mc.postToChat('YOU LOSE')
            mc.postToChat("Let's play again!")
            minigame(x,y,z,v,m,False) #Restart the game
        elif p==10: # Win condition
            mc.postToChat('YOU WIN')
            gameover=True
        else:
            p+=1