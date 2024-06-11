import pygame, sys, time

pygame.mixer.init()

print("1 = song1")
print("2 = song2")
print("3 = song3")
print("x = exit")

while True:
      user_input = input('Command: ')

      if user_input == '1':
         pygame.mixer.music.load('ifloseitall.mp3')
         pygame.mixer.music.play()

      if user_input == '2':
         pygame.mixer.music.load('abyss.mp3')
         pygame.mixer.music.play()   
      
      if user_input == '3':
         pygame.mixer.music.load('coraline.mp3')
         pygame.mixer.music.play()
         #time.sleep(3)
        # pygame.mixer.music.set_volume(0,1)   
      
      if user_input == 'x':
         sys.exit() 

