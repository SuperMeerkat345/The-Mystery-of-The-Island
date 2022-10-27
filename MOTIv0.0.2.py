import random 
import time

#Before you start reading, I am quite new to python but have some experience in other languages so you might see me implementing solutions to problems like function changing in very inefficient ways so please forgive me.
#My functions are classified in subcategories so gamePauseSettings would be the settings in the pause menu in the main game
clearScreen = "\n"*100
name=""
version="0.0.2"
#keeps track of what you type into the console
console = ""
#World
worldRandom = random.randint(0,100)
worldSet = 1
worldRaw = ["forest", "clearing", "lake", "beach"]
possibleWorld = ["You are surrounded by trees.", "You are in a clearing surrounded by trees.", "You are at a lake.", "You are on a beach"]


#The current position is random option out of list worldRaw

currentWorld = worldRaw[worldSet]
#Character
health = 100
backpack = [] 
#For scene changing (function changing)
sceneChangeName = "menuStart"
sceneChangePermission = True


def functionTemplate():
    #changes scene to "" so that no improper warps to functions
    global sceneChangeName
    sceneChangeName = ""

    #Gives permission to go to next scene
    sceneChangePermission = True
    #specifies which scene to go to, please define these at the while loop at the back of the code.
    sceneChangeName = "menuStart"



#end function template
def menuStart():
    global sceneChangeName
    sceneChangeName = "" 
    
    input("Welcome to The Mystery of The Forest a text-based survival game, Please press Enter to continue.")
    input("For a balanced gameplay experience don't copy paste commands.")
    input("Please keep in mind that this game is still in development, version "+version+" (Enter)")
    

    sceneChangePermission = True
    sceneChangeName = "menuName"

    
def menuName():
    global sceneChangeName
    sceneChangeName = ""

    #start code
    global name
    name = input("What would you like to be refered to as? \n")
    if name == "":
        input("Please enter a name, press Enter to continue.")
        sceneChangePermission = True
        sceneChangeName = "menuName"
    else:
        input("Welcome "+name+"!")
        input("Press Enter to start the actual game.")
        
        sceneChangePermission = True
        sceneChangeName = "preGame"
    
    
    
    
    
    








def preGame():
    global sceneChangeName
    sceneChangeName = "" 

    #start code
    input("You wake up in a forest. It is eerily silent for a forest.")
    input("There are no birds there is no wind yet... there is something.")
    input("Something hiding in the darkness, in the shadows, just waiting")
    input("You should probably get up and get out of here. It's just a feeling.")
    
     
    
    


    sceneChangePermission = True
    sceneChangeName = "preGameLookAround"


def preGameLookAround():
    global sceneChangeName
    sceneChangeName = "" 
    
    global console
    console = input("You can look around by typing in \"look around\"\n")
    if console == "look around":
        input("You are in a clearing surrounded by trees.")
        input("If you want a list of commands you can type \"help\" keep in mind that you might lose or gain permission to commands (like starting a fire when not at a fire)")
        sceneChangePermission = True
        sceneChangeName = "gameWorldMain"
    else:
        input("Not a proper command please try again")
        sceneChangePermission = True
        sceneChangeName = "preGameLookAround"
        
    




def gameWorldMain():
    global currentWorld
    #Doesn't let change scene
    global sceneChangeName
    sceneChangeName = "" 
    #start code

    
    global console
    console = input("What would you like to do:\n")

    if console == "help":
        input("Current availible commands:")

        input("\nClear screen - \"clear\"")
        input("Look around - \"look around\"")
        input("Travel - \"travel\"")
        input("Help - \"help\"")
        if currentWorld == "beach":
            input("Continue traveling on beach - \"travel along beach\"")
        
        # resets console scene
        
        sceneChangePermission = True
        sceneChangeName = "gameWorldMain"
        
    elif console == "look around":
        if currentWorld == "forest":
            input(possibleWorld[0])

            
            sceneChangePermission = True
            sceneChangeName = "gameWorldMain"
            
        elif currentWorld == "clearing":
            input(possibleWorld[1])

            
            sceneChangePermission = True
            sceneChangeName = "gameWorldMain"
            
        elif currentWorld == "lake":
            input(possibleWorld[2])

            
            sceneChangePermission = True
            sceneChangeName = "gameWorldMain"
        elif currentWorld == "beach":
            input(possibleWorld[3])

            
            sceneChangePermission = True
            sceneChangeName = "gameWorldMain"
            
        else:
            input("Error: currentWorld not found. Please report issue.")
            
            
            sceneChangePermission = True
            sceneChangeName = "gameWorldMain"
            

    

    #end code
   

    
    elif console == "travel":
        global worldRandom
        global worldSet
       
        print("Traveling... (Please don't touch keys while traveling)")
        time.sleep(3)
        if worldRandom >= 0 and worldRandom <= 59:
            #worldSet = forest
            worldSet = 0
            input("Traveling complete")
            worldRandom = random.randint(0,100)
        elif worldRandom >= 60 and worldRandom <= 79:
            #worldSet = clearing
            worldSet = 1
            input("Traveling complete")
            worldRandom = random.randint(0,100) 
            
        elif worldRandom >= 80 and worldRandom <= 89:
            #worldSet = lake
            worldSet = 2
            input("Traveling complete")
            worldRandom = random.randint(0,100)
            
        elif worldRandom >= 90 and worldRandom <= 100:
            #worldSet = beach
            worldSet = 3
            input("Traveling complete")
            worldRandom = random.randint(0,100)
           

        else:
            print("Error with worldRandom and worldSet please report issue.")
            sceneChangePermission = True
            sceneChangeName = "gameWorldMain"
            return
 
        
        

        currentWorld = worldRaw[worldSet]
        sceneChangePermission = True
        sceneChangeName = "gameWorldMain"
        

    
    elif console == "clear":
        print(clearScreen)
        sceneChangePermission = True
        sceneChangeName = "gameWorldMain"
    elif console == "travel along beach" and currentWorld == "beach":
        print("Traveling... (Please don't touch keys while traveling)")
        time.sleep(3)
        input("Traveling complete")
        currentWorld == "beach"
        sceneChangePermission = True
        sceneChangeName = "gameWorldMain"
    else:
        input("Not a proper command please try again, type help for a list of commands.")
        
        
        sceneChangePermission = True
        sceneChangeName = "gameWorldMain"

        
        
      

















    #end code



while sceneChangePermission==True:

    if sceneChangeName == "menuStart":
        menuStart()
        sceneChangePermission==False
    if sceneChangeName == "menuName":
        menuName()
        sceneChangePermission==False
    if sceneChangeName == "preGame":
        preGame()
        sceneChangePermission==False
    if sceneChangeName == "preGameLookAround":
        preGameLookAround()
        sceneChangePermission==False
    if sceneChangeName == "gameWorldMain":
        gameWorldMain()
        sceneChangePermission==False
    if sceneChangeName == "worldGenerator":
        worldGenerator()
        sceneChangePermission==False
    





#the end
