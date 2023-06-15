import pygame
from pygame.locals import *
from Pong Game TEST import starte_spiel

# Fenstergröße
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500


# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def show_menu():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Spielmenü")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)

    while True:
        screen.fill(BLACK)


        # Text für die Menüoptionen zeichnen

        start_text = font.render("Starten", True, WHITE)
        start_rect = start_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        screen.blit(start_text, start_rect)


        options_text = font.render("Optionen", True, WHITE)
        options_rect = options_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        screen.blit(options_text, options_rect)

        pygame.display.flip()
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return        
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if start_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    start_game()  # Rufe deine Spielfunktion auf, wenn "Starten" ausgewählt wurde
                    return

                elif options_rect.collidepoint(mouse_pos):
                    print("Optionen ausgewählt")  # Hier kannst du deine Optionen-Funktion aufrufen oder weitere Logik hinzufügen

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Spiel")
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)
        


        # Hier kannst du dein Spiel zeichnen und aktualisieren
        

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


show_menu()