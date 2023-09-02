import pygame
from sys import exit
import time

# Initialize pygame and set up the display
pygame.init()
screen = pygame.display.set_mode((800, 480))
clock = pygame.time.Clock()
status = True

class FaceAnimation:
    def __init__(self, screen, face_list, animation_speed):
        self.screen = screen
        self.face_list = face_list
        self.animation_speed = animation_speed
        self.index = 0
        self.face_surf = face_list[self.index]

    def animate(self):
        self.index += self.animation_speed
        if self.index >= len(self.face_list):
            self.index = 0
        self.face_surf = self.face_list[int(self.index)]
        self.screen.blit(self.face_surf, (0, 0))

class Mood:
    def __init__(self):
        self.moods = {}
    
    def add_mood(self, name, face_list, animation_speed):
        self.moods[name] = FaceAnimation(screen, face_list, animation_speed)

    def animate(self, mood_name):
        if mood_name in self.moods:
            self.moods[mood_name].animate()
        else:
            print(f"Mood '{mood_name}' not found")

    def reset(self):
        self.animate("neutral") 

# Create a Mood instance
mood = Mood()

def setup_moods():
    angry_face_list = [pygame.transform.scale(pygame.image.load(f'graphics/angryFace/{i}.png'), (800, 480)) for i in range(1, 15)]
    mood.add_mood("angry", angry_face_list, 0.5)

    happy_face_list = [pygame.transform.scale(pygame.image.load(f'graphics/happyFace/{i}.png'), (800, 480)) for i in range(1, 18)]
    mood.add_mood("happy", happy_face_list, 0.35)

    neutral_face_list = [pygame.transform.scale(pygame.image.load(f'graphics/neutralFace/{i}.png'), (800, 480)) for i in range(1, 24)]
    mood.add_mood("neutral", neutral_face_list, 0.6)

def mood_loop(mood_name, duration=-1):
    start_ticks = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if status:
            mood.animate(mood_name)
            if duration != -1 and pygame.time.get_ticks() - start_ticks > duration:
                break
            

            
        pygame.display.update()
        clock.tick(30)  # Control the frame rates
