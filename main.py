import pygame
import sys

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time_s = int(current_time / 1000)
    score_surface = score_font.render(str(current_time_s), False, (64,64,64))
    score_rect = score_surface.get_rect()
    score_rect.center = (400, 50)
    screen.blit(score_surface, score_rect)

    return current_time_s

def display_start_screen(score):
    font = pygame.font.Font("font/Pixeltype.ttf", 50)
    score_font = pygame.font.Font("font/Pixeltype.ttf", 40)
    
    title_surf = font.render("Jumper Game", False, (64, 64, 64))
    title_rect = title_surf.get_rect()
    title_rect.center = (400, 50)

    score_surf = score_font.render(f"Final score: {score}", False, (64, 64, 64))
    score_rect = score_surf.get_rect()
    score_rect.center = (400, 80)

    player_img = pygame.image.load("graphics/player/player_walk_1.png")
    player_img = pygame.transform.scale_by(player_img, 2)
    p_rect = player_img.get_rect()
    p_rect.center = (400, 190)

    instruction_surf = font.render("Press Space to start", False, (64, 64, 64))
    instruction_rect = instruction_surf.get_rect()
    instruction_rect.center = (400, 350)

    screen.fill((208, 244, 247))
    screen.blit(title_surf, title_rect)
    screen.blit(score_surf, score_rect)
    screen.blit(player_img, p_rect)
    screen.blit(instruction_surf, instruction_rect)


def play_bgm():
    bgm = pygame.mixer.Sound("audio/music.wav")
    bgm.set_volume(0.3)
    bgm.play(loops=-1)

def play_jump_sound():
    jump_sound = pygame.mixer.Sound("audio/jump.mp3")
    jump_sound.set_volume(0.5)
    jump_sound.play()

pygame.init()

WIDTH = 800
HEIGHT = 400
GAME_ACTIVE = True
start_time = 0
SCORE = 0
MOB_SPEED = 0
MOB_SPEED_CAP = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumper Game")

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

play_bgm()
while True:
    for event in pygame.event.get():
        if GAME_ACTIVE:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play_jump_sound()
                    if player_rect.bottom == 300:
                        player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    play_jump_sound()
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                GAME_ACTIVE = True
                snail_rect.left = 800
                MOB_SPEED = 0
                start_time = pygame.time.get_ticks()


    if GAME_ACTIVE:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # increase mob speed
        if MOB_SPEED <  MOB_SPEED_CAP:
            MOB_SPEED += 0.01

        # score
        score = display_score()

        # snail
        screen.blit(snail_surface, snail_rect)
        snail_rect.x -= 8 + MOB_SPEED
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
        display_start_screen(score)

    pygame.display.update()
    clock.tick(60) # run while loop 60 times per second