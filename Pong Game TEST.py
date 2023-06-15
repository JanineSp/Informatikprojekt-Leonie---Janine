import pygame
from pygame.locals import *

def starte_spiel():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mein Spiel")
    clock = pygame.time.Clock()

    running = True
    while running:
       screen.fill((0, 0, 0))
    # Spielfeld
    window_width = 1000
    window_height = 500
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pong Game")

    # Hintergrundbild
    image = pygame.image.load("Tischtennistisch.jpg")
    window.blit(image, (0, 0))

    # Farbzuweisung
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PINK = (255, 0, 255)
    ORANGE = (255, 140, 0)

    # Schläger
    paddle_width = 10
    paddle_height = 60
    paddle_speed = 5
    paddle1_x = 10
    paddle1_y = window_height // 2 - paddle_height // 2
    paddle2_x = window_width - paddle_width - 10
    paddle2_y = window_height // 2 - paddle_height // 2

    # Spielball
    ball_radius = 8
    ball_x = window_width // 2
    ball_y = window_height // 2
    ball_dx = 3
    ball_dy = 3

    # Punktestand
    score1 = 0
    score2 = 0
    font = pygame.font.Font(None, 50)

    # Game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Move the paddles
        keys = pygame.key.get_pressed()
        if keys[K_w] and paddle1_y > 0:
            paddle1_y -= paddle_speed
        if keys[K_s] and paddle1_y < window_height - paddle_height:
            paddle1_y += paddle_speed
        if keys[K_UP] and paddle2_y > 0:
            paddle2_y -= paddle_speed
        if keys[K_DOWN] and paddle2_y < window_height - paddle_height:
            paddle2_y += paddle_speed

        # Update ball position
        ball_x += ball_dx
        ball_y += ball_dy

        # Check for ball collision with paddles
        if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
            ball_dx = abs(ball_dx)
        if ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
            ball_dx = -abs(ball_dx)

        # Check for ball collision with walls
        if ball_y <= 0 or ball_y >= window_height - ball_radius:
            ball_dy = -ball_dy

        # Check for ball out of bounds
        if ball_x <= 0:
            score2 += 1
            ball_x = window_width // 2
            ball_y = window_height // 2
        elif ball_x >= window_width:
            score1 += 1
            ball_x = window_width // 2
            ball_y = window_height // 2

        # Clear the screen
        window.fill(BLACK)
        window.blit(image, (0, 0))

        # Draw the paddles and ball
        pygame.draw.rect(window, ORANGE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
        pygame.draw.rect(window, ORANGE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
        pygame.draw.circle(window, PINK, (ball_x, ball_y), ball_radius)

        # Draw the scores
        score_text = font.render(str(score1), True, WHITE)
        window.blit(score_text, (window_width // 2 - 50, 10))
        score_text = font.render(str(score2), True, WHITE)
        window.blit(score_text, (window_width // 2 + 30, 10))

        # Update the display
        pygame.display.update()

        # Set the frames per second
        clock.tick(60)
        pygame.display.flip()
       clock.tick(60)

       for event in pygame.event.get():
           if event.type == QUIT:
               running = False
           elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   running = False
# Quit the game
pygame.quit()
