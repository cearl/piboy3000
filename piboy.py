#!/usr/bin/python
#seperate functions
# 
#
import pygame, time,sys, random, os, glob, OsmApi, subprocess
from pygame.locals import *
from pynmea import nmea
#attempt to provide some randomness
random.seed("gerHork;CobzibMekteajto3456@#$xjurvizjanJeKicvocsurc")
pygame.init()
music_files = glob.glob("./music/*")
music_list = []
pygame.mixer.init()

def gps_nmea():
    gps_data = subprocess.os("blah blah")
    gpgga = nmea.GPGGA()
    gpgga.parse(data)

def key_bindings():
    count = len(music_list)

    
    return
def find_music():
    for i in glob.glob("./music/*"):
        music_list.append(i)
         

def main():
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption("PipBoy 3000")
 
    # Background Image
    background = pygame.image.load("pipboy-bg2.png").convert()
    # Alpha Counter
    alphaCount = 200
    alphaInOut = True
 
    keepGoing = True
    clock = pygame.time.Clock()
 
    # Game Loop
    while keepGoing:
        clock.tick(30)
        screen.blit(background, (0, 0))

        ###Key Bindings ####
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    sys.exit(0)
                if (event.key == K_UP):    
                     gps_osm()
                if (event.key == K_RIGHT):
                    background = pygame.image.load("pipboy-bg2.png")
                    background = pygame.image.load("pipboy-bg2.png").convert()
                if (event.key == K_LEFT):
                    background = pygame.image.load("map.png")
                    background = pygame.image.load("map.png").convert()

                if (event.key == K_DOWN):
                    print("down")
                if (event.key == K_n):
                    try:
		        pygame.mixer.music.load(music_list[random.randint(0, count)])
                        pygame.mixer.music.play()
		    except:
		        pygame.mixer.music.load(music_list[random.randint(0, count)])
                        pygame.mixer.music.play()
			main()

        #####################
        ## Pipboy Overlay ###
        

        ##
        count = len(music_list)
        music_state = pygame.mixer.music.get_busy()
        if ( music_state == False):
            try:
	        pygame.mixer.music.load(music_list[random.randint(0, count)])
                pygame.mixer.music.play()                   
	    except:
	        pygame.mixer.music.load(music_list[random.randint(0, count)])
                pygame.mixer.music.play()
		main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
 
        # Fill the background
        screen.fill((0, 0, 0))
        background = pygame.transform.scale(background,(640,400)) 
        # Reset alpha
        if (alphaCount >= 255):
            alphaCount = 255
            alphaInOut = not alphaInOut
        elif (alphaCount <= 225):
            alphaCount = 225
            alphaInOut = not alphaInOut
 
        # Set background's alpha and iterate alphaCount
        background.set_alpha(alphaCount)
 
        if (alphaInOut):
            alphaCount += 5
        else:
            alphaCount -= 5
	 
	
        # Draw the background to the screen buffer
        # Flip the buffer

        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    find_music()
    main()
