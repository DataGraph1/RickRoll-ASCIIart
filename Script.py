import time

stats = [] #player stats, filled from save file

effects = [
    "levitation",
    "speed",
    "danger",
    "luck",
    "hop"
]

itemCount = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13
]


items = [ #all items in game
    "club",
    "dagger",
    "short sword",
    "sword",
    "long sword",
    "small axe",
    "axe",
    "large axe",
    "small hammer",
    "hammer",
    "mace",
    "short bow",
    "bow",
    "long bow",
    "light crossbow",
    "crossbow",
    "large crossbow",
    "glass vial",
    "leather cap",
    "leather tunic",
    "leather leggings",
    "small sheild",
    "sheild",
    "large sheild",
    "net",
    "woodern arrows",
    "stone arrows",
    "copper arrows",
    "steal arrows",
    "enchanted arrows",
]

def slotSelector(): #user chooses save file
    for x in range(1,4): #displays save files
        f = open("Saves/"+str(x)+".txt")
        print(str(x) + "]", f.readline(1) + "%")
        f.close
    
    option = input("Choose a save slot") #allows save file choice
    if "1" in option:
        f = open("Saves/1.txt")
    elif "2" in option:
        f = open("Saves/2.txt")
    elif "3" in option:
        f = open("Saves/3.txt")
    else:
        print("Non-existent save file, try again!")
        slotSelector()

    for x in range(2,5): #save file stats into list
        stats.append(f.readlines(27))
    f.close

def screenSetUp(): #makes sure terminal is big enough for ASCII art
    print("1" * 125)
    for x in range(1, 50):
        print("")
    x = input("Resize terminal so: \n 1. You can see this entire message\n 2. You can see the numbers above\n 3. All those numbers are on the same line\nThen press Enter")
    animation()

def animation(): #plays ASCII art animation
    lyricNum = 1
    while True:
        for frameNum in range(1,51):
            frame = open(".config/SaveFiles/"+str(frameNum)+".txt", "r")
            lyric = open(".config/SaveData/"+str(lyricNum)+".txt", "r")
            print(frame.read())
            print(lyric.read())
            frame.close
            lyric.close
            time.sleep(0.0417)
        if lyricNum < 7:
            lyricNum += 1
        else:
            lyricNum = 1

animation()
