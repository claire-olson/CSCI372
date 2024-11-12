import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 36)

# Hangman images
hangman_images = [pygame.image.load(f"hangman{i}.png") for i in range(7)]

# Game variables
word_bank = {
    "animals": ["tiger", "elephant", "giraffe", "kangaroo", "zebra"],
    "fruits": ["apple", "banana", "mango", "orange", "watermelon"],
    "countries": ["canada", "france", "brazil", "japan", "australia"],
    "sports": ["soccer", "basketball", "tennis", "cricket", "swimming"]
}
max_attempts = 6
score = 0

# Game functions
def select_word(category):
    return random.choice(word_bank[category]).upper()

def display_message(text, x, y, color=BLACK, font=font_small):
    message = font.render(text, True, color)
    screen.blit(message, (x, y))

def draw_hangman(wrong_guesses):
    screen.blit(hangman_images[wrong_guesses], (150, 100))

def display_word(word, guessed_letters):
    display = ''.join([letter + ' ' if letter in guessed_letters else '_ ' for letter in word])
    word_text = font_large.render(display.strip(), True, BLACK)
    screen.blit(word_text, (400, 200))

def handle_guess(guess, word, guessed_letters, wrong_guesses):
    global score
    if guess in guessed_letters or guess in wrong_guesses:
        return "Already guessed!"
    elif guess in word:
        guessed_letters.add(guess)
        score += 10
        return "Good guess!"
    else:
        wrong_guesses.add(guess)
        score -= 5
        return "Wrong guess!"

def is_won(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def is_lost(wrong_guesses):
    return len(wrong_guesses) >= max_attempts

# Main Game Loop
def game_loop(player_mode):
    global score
    running = True
    guessed_letters = set()
    wrong_guesses = set()
    word = select_word("animals") if player_mode == "computer" else input("Enter a word for Player 2 to guess: ").strip().upper()
    score = 0

    while running:
        screen.fill(WHITE)
        draw_hangman(len(wrong_guesses))
        display_word(word, guessed_letters)
        display_message(f"Score: {score}", 650, 50, BLUE)
        display_message("Attempts Left: " + str(max_attempts - len(wrong_guesses)), 650, 100, RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and len(event.unicode) == 1:
                    guess = event.unicode.upper()
                    result = handle_guess(guess, word, guessed_letters, wrong_guesses)
                    display_message(result, 300, 400)

        if is_won(word, guessed_letters):
            display_message("You Win!", 300, 300, GREEN, font_large)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
        elif is_lost(wrong_guesses):
            display_message(f"Game Over! The word was {word}", 200, 300, RED, font_large)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        pygame.display.flip()

def main_menu():
    running = True
    while running:
        screen.fill(WHITE)
        display_message("Welcome to Hangman", 250, 100, BLUE, font_large)
        display_message("1. Play Against Computer", 280, 300)
        display_message("2. Player vs Player", 280, 350)
        display_message("Press 'Q' to Quit", 280, 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop("computer")
                elif event.key == pygame.K_2:
                    game_loop("player")
                elif event.key == pygame.K_q:
                    running = False

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
    pygame.quit()
    sys.exit()
