import time

def screen_setup(): #makes sure terminal is big enough for ASCII art
    print('0' * 125)
    for _ in range(1, 50):
        print('')

    _ = input('''
Resize terminal so:
    1. You can see this entire message
    2. You can see the numbers above
    3. All those numbers are on the same line
Then press Enter
''')
    
    animation()

def animation(): #plays ASCII art animation
    lyricNum = 1
    while True:
        for frameNum in range(1,51):
            with open('Frames/'+str(frameNum)+'.txt') as frame:
                print(frame.read())
            with open('Lyrics/'+str(lyricNum)+'.txt') as lyric:
                print(lyric.read())

            time.sleep(0.0417)

        if lyricNum < 7:
            lyricNum += 1
        else:
            lyricNum = 1

screen_setup()