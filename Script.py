import time

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
            frame = open("Frames/"+str(frameNum)+".txt", "r")
            lyric = open("Lyrics/"+str(lyricNum)+".txt", "r")
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
