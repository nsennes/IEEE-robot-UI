import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((800,480))
clock = pygame.time.Clock()
animation_speed = 0.5

#angryFace function
def angryFaceAnimation(screen, angry_face_list, animation_speed):
    global angry_face_surf, af_index
    af_index += animation_speed
    if af_index >= len(angry_face_list):af_index = 0
    angry_face_surf = angry_face_list[int(af_index)]
    screen.blit(angry_face_surf, (0, 0))  # Draw the angry face


#angryFace
angry_face_list = [pygame.transform.scale(pygame.image.load(f'graphics/angryFace/{i}.png'), (800, 480)) for i in range(1, 15)]
af_index = 0
angry_face_surf = angry_face_list[af_index]

#



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    angryFaceAnimation(screen, angry_face_list, animation_speed)

    pygame.display.update()
    clock.tick(30)
