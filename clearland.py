from mcpi import minecraft
mc = minecraft.Minecraft.create()
#Clearland
mc.postToChat("Clearing land...")
mc.setBlocks(-128,0,128,128,64,-128,0)
mc.postToChat("Clear land complete")
mc.postToChat("Placing grassblock to the world...")
mc.setBlocks(-128,0,128,128,3,-128,2)
mc.postToChat("Done")
mc.postToChat("The world is ready")