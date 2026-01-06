import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 400
GAME_ACTIVE = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

score_font = pygame.font.Font("font/Pixeltype.ttf", 50)
score_surface = score_font.render("Hello world", False, (64, 64, 64))
score_rect = score_surface.get_rect()
score_rect.center = (400, 50)

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect()
snail_rect.midbottom = (600, 300)

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect()
player_rect.midbottom = (80, 300)
player_gravity = 0

while True:
    for event in pygame.event.get():
        if GAME_ACTIVE:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                GAME_ACTIVE = True
                snail_rect.left = 800

    if GAME_ACTIVE:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # score
        pygame.draw.rect(screen, "#c0e8ec", score_rect)
        pygame.draw.rect(screen, "#c0e8ec", score_rect, 20,)
        screen.blit(score_surface, score_rect)

        # snail
        screen.blit(snail_surface, snail_rect)
        snail_rect.x -= 8
        if snail_rect.right < 0: 
            snail_rect.x = 800

        # player
        player_gravity += 0.8
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            GAME_ACTIVE = False

    else:
        screen.fill("Yellow")

    pygame.display.update()
    clock.tick(60) # run while loop 60 times per second