import cwiid, time, random, sys
import unicornhat as UH

UH.brightness(0.05)
score = 0.0

class killer:
    def __init__(self):
        self.visible = True
        self.oldxy = None
        self.y = random.randint(0, 7)
        self.x = 7
        self.moves = 0
        self.good = False
    def move(self):
        self.oldxy = [self.x, self.y]
        self.x = self.x - 1
        if self.x < 0:
            self.visible = True
            self.x = 7
            self.y = random.randint(0, 7)
            self.good = random.choice([True, False, False, False])
        self.moves = self.moves + 1

print 'Press 1 + 2 on wiimote now.'
time.sleep(1)
wm = cwiid.Wiimote()
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

killSpeed = input('Enter a killbot speed. Recommended 1. ')

inactiveKillers = []
activeKillers = []
killerNum = raw_input('How many killers do you want? ')
for i in range(0, int(killerNum)):
    inactiveKillers.append(killer())
print len(inactiveKillers)
if len(inactiveKillers) > 0:
    activeKillers.append(inactiveKillers.pop())

UH.rotation(90)

pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
UH.set_pixels(pixels)
UH.show()

time.sleep(1)

pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
UH.set_pixels(pixels)
UH.show()

time.sleep(1)

pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
UH.set_pixels(pixels)
UH.show()

time.sleep(1)

UH.clear()
UH.rotation(0)


edge = [1, 9, 17, 25, 33, 41, 49, 57]
length = len(edge)

oldxy = None
position = 0    

loopNum = 0

rumble = 'off'

while True:
    o = wm.state['acc']
    pitch = o[1]

    if pitch > 129:
        if position == 0:
            position = length-1
        else:
            position = position - 1

    elif (pitch < 120) and (pitch > 99):
        if position == length-1:
            position = 0
        else:
            position = position + 1

    yaw_pixel_number = edge[position]
    y = yaw_pixel_number // 8
    x = yaw_pixel_number % 8

    if oldxy:
        UH.set_pixel(oldxy[0], oldxy[1], 0, 0, 0)
        
    UH.set_pixel(x, y, 255, 255, 255)
    oldxy = [x, y]
    
    for killbot in activeKillers:
        if (killbot.x == x) and (killbot.y == y) and (not killbot.good) and (killbot.visible):
            wm.rumble = 1
            time.sleep(0.3)
            wm.rumble = 0
            UH.rotation(90)
            pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (255, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
            UH.set_pixels(pixels)
            UH.show()
            time.sleep(5)
            print 'Score: %i'%int(score)
            wm.close()
            sys.exit()

        elif (killbot.x == x) and (killbot.y == y) and (killbot.good) and (killbot.visible):
            wm.rumble = 1
            rumble = 9
            score = score + 1.0
            killbot.visible = False
            UH.set_pixel(killbot.x, killbot.y, 0, 0, 0)

    if loopNum == killSpeed:
        for killbot in activeKillers:
            killbot.move()
            
            if killbot.visible:
                UH.set_pixel(killbot.oldxy[0], killbot.oldxy[1], 0, 0, 0)
                if killbot.good:
                    draw = True
                    for tbot in activeKillers:
                        if (tbot.x == killbot.x) and (tbot.y == killbot.y) and (not tbot.good):
                            draw = False
                    if draw:
                        UH.set_pixel(killbot.x, killbot.y, 0, 255, 0)
                else:
                    UH.set_pixel(killbot.x, killbot.y, 255, 0, 0)

            if (killbot.moves == 44) and (len(inactiveKillers) > 0):
                activeKillers.append(inactiveKillers.pop())
        score = score + 1.0/4.0
        print score
        loopNum = 0
    else:
        loopNum = loopNum + 1
    
    if rumble != 'off':
        if rumble == 0:
            wm.rumble = 0
            rumble = 'off'
        else:
            rumble = rumble - 1

    UH.show()
    time.sleep(0.075)
