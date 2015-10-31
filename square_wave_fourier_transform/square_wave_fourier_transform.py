import time, pygame,math
pygame.init()
size = 640,480
screen = pygame.display.set_mode(size)

grey = 70,70,70
pink  = 255,0,255
darkgreen = 0,100,0
lightgreen = 127,255,0
black = 0,0,0

resultant = [] 

frequency = 1
amplitude = 100/frequency

pygame.draw.line(screen, grey, (120,240),(520,240))
pygame.display.flip()

for x in range (0, 377):
    y = int(amplitude * math.sin((float(x)/30)*frequency))
    resultant.append(y)
    screen.set_at(((120 + x),(240 -y)), lightgreen)
    pygame.display.flip()
    time.sleep(0.01)

for x in range (0, 377):
    y = int(amplitude * math.sin((float(x)/30)*frequency))
    resultant.append(y)
    screen.set_at(((120 + x),(240 -resultant[x])), pink)

pygame.display.flip()

frequency = frequency + 2
amplitude = 100/frequency

while 1:
    for x in range (0, 377):

        screen.set_at((120 + x, 240 - resultant[x]), black)

        point_y = int(amplitude * math.sin((float(x)/30)*frequency))
        resultant[x] = (resultant[x] + point_y)

        screen.set_at((120 + x, 240 - resultant[x]), pink)
        screen.set_at((120 + x, 240 - point_y), lightgreen)

        pygame.display.flip()
        time.sleep(0.01)

    for x in range (0, 377):
        
        screen.set_at((120 + x, 240 - int(amplitude * math.sin((float(x)/30)*frequency))), darkgreen)

    pygame.display.flip    
    frequency = frequency + 2
    amplitude = 100/frequency

