import pygame
import sys
import os
from pygame import mixer

pygame.mixer.init()
pygame.mixer.pre_init()
pygame.mixer.get_init()



def play_music():
    
    song_choices_files = ["BJ-Thomas-Rain-Drops-Keep-Falling-On-My-Head.mp3","[MP3DOWNLOAD.TO] Dan Hartman - I Can Dream About You (1984)-192k.mp3","Brenda_Lee_-_If_You_Love_Me_Really_Love_Me.mp3"]
    song_choices = ["1)Raindrops keep falling on my head - BJ Thomas","2)I Can Dream About You - Dan Hartman(1984)","3)If You Love Me(Really Love Me) - Brenda Lee"]
    choice = int(input("Pick a song: \n \n"+"{} \n{} \n{} \n".format(*song_choices)+ "\n"+"[1,2,3]>>>: "))
    n = choice - 1
    def choose_song(n):
        song = song_choices_files[n]
        pygame.mixer.music.load (song)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
    print ("Press 'p' to pause")
    print ("Press 'r' to resume")
    print ("Press 'v' to set volume")
    print ("Press 's' to skip")
    print ("Press 'e' to exit")
    while True:
        choose_song(n)
            
        #second loop so that can go back to choose_song when type 'n'    
        while True:
            ch = input("['p','r','v','s','e']>>>")

            if ch == "p":
                pygame.mixer.music.pause()
            elif ch == "r":
                pygame.mixer.music.unpause()
            elif ch == "v":
                v = float(input("Enter volume from 0-1: "))
                pygame.mixer.music.set_volume(v)
            elif ch == "s":
                n = n+1
                break
            elif ch == "e":
                pygame.mixer.music.stop()
                return False
                
       
            
                    
        
        
play_music()            

        
