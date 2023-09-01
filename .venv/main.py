import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((800,480))
clock = pygame.time.Clock()



#angryFace
angry_face_list = [pygame.transform.scale(pygame.image.load(f'graphics/angryFace/{i}.png'), (800, 480)) for i in range(1, 15)]
af_index = 0
angry_face_surf = angry_face_list[af_index]
af_animation_speed = 0.5

#angryFace function
def angryFaceAnimation(screen, angry_face_list, af_animation_speed):
    global angry_face_surf, af_index
    af_index += af_animation_speed
    if af_index >= len(angry_face_list):af_index = 0
    angry_face_surf = angry_face_list[int(af_index)]
    screen.blit(angry_face_surf, (0, 0))  # Draw each frame of the angry face


#happyFace
happy_face_list = [pygame.transform.scale(pygame.image.load(f'graphics/happyFace/{i}.png'), (800,480)) for i in range(1,17)]
hf_index = 0
happy_face_surf = happy_face_list[hf_index]
hf_animation_speed = 0.35

#happyFace function
def happyFaceAnimation(screen, happy_face_list, hf_animation_speed):
    global happy_face_surf, hf_index
    hf_index += hf_animation_speed
    if hf_index >= len(happy_face_list): hf_index = 0
    happy_face_surf = happy_face_list[int(hf_index)]
    screen.blit(happy_face_surf,(0,0))


#neutralFace
neutral_face_list = [pygame.transform.scale(pygame.image.load(f'graphics/neutralFace/{i}.png'), (800,480)) for i in range(1,23)]
nf_index = 0
neutral_face_surf = neutral_face_list[nf_index]
nf_animation_speed = 0.6

#neutralFace function
def neutralFaceAnimation(screen, neutral_face_list, nf_animation_speed):
    global neutral_face_surf, nf_index
    nf_index += nf_animation_speed
    if nf_index >= len(neutral_face_list): nf_index = 0
    neutral_face_surf = neutral_face_list[int(nf_index)]
    screen.blit(neutral_face_surf,(0,0))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #angryFaceAnimation(screen, angry_face_list, af_animation_speed)
    #happyFaceAnimation(screen, happy_face_list, hf_animation_speed)
    neutralFaceAnimation(screen, neutral_face_list, nf_animation_speed)

    pygame.display.update()
    clock.tick(30) #this is to control the amount of framerates in the animation
