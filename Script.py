import time

def screen_setup(): #makes sure terminal is big enough for ASCII art
    print("1" * 125)
    for x in range(1, 50):
        print("")
    x = input("Resize terminal so: \n 1. You can see this entire message\n 2. You can see the numbers above\n 3. All those numbers are on the same line\nThen press Enter")
    animation()

def animation(): #plays ASCII art animation
    lyric_num = 1
    while True:
        for frameNum in range(1,51):
            with open("Frames/"+str(frameNum)+".txt") as frame:
                print(frame.read())
            with open("Lyrics/"+str(lyric_num)+".txt") as lyric:
                print(lyric.read())
            time.sleep(0.0417)
        if lyric_num < 7:
            lyric_num += 1
        else:
            lyric_num = 1

screen_setup()
