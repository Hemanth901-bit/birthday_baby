import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Birthday, My Love! 🎈")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALLOON_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (255, 165, 0)]
QUOTE_COLOR = (255, 255, 255)
HEART_COLOR = (255, 0, 0)
STAR_COLOR = (255, 255, 0)
ROSE_COLOR = (255, 105, 180)

# Balloon class
class Balloon:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(30, 50)
        self.speed = random.uniform(0.5, 1.5)  # Balloon float speed

    def move(self):
        self.y -= self.speed  # Move the balloon up
        if self.y < 0:
            self.y = HEIGHT  # Reset balloon to bottom if it reaches the top

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.radius)
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x, self.y + 30), 3)  # Balloon string

# Heart symbol class
class Heart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(10, 20)
        self.speed = random.uniform(0.5, 2.0)  # Speed of heart floating
        self.angle = random.uniform(0, 360)

    def move(self):
        self.y -= self.speed  # Move the heart upwards
        self.x += random.choice([-1, 1])  # Move slightly left or right for a drifting effect
        if self.y < 0:  # Reset when it moves off the screen
            self.y = HEIGHT
            self.x = random.randint(100, WIDTH - 100)

    def draw(self):
        pygame.draw.circle(screen, HEART_COLOR, (int(self.x), int(self.y)), self.size)

# Star symbol class
class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(5, 10)
        self.speed = random.uniform(0.5, 1.5)
        self.angle = random.uniform(0, 360)

    def move(self):
        self.y -= self.speed  # Move the star upwards
        self.x += random.choice([-1, 1])  # Slight horizontal movement
        if self.y < 0:  # Reset when it moves off the screen
            self.y = HEIGHT
            self.x = random.randint(100, WIDTH - 100)

    def draw(self):
        pygame.draw.polygon(screen, STAR_COLOR, [
            (self.x, self.y - self.size),
            (self.x - self.size, self.y + self.size),
            (self.x + self.size, self.y + self.size),
        ])

# Rose symbol class
class Rose:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(15, 30)
        self.speed = random.uniform(0.3, 1.2)
        self.angle = random.uniform(0, 360)

    def move(self):
        self.y -= self.speed  # Move the rose upwards
        self.x += random.choice([-1, 1])  # Slight horizontal movement
        if self.y < 0:  # Reset when it moves off the screen
            self.y = HEIGHT
            self.x = random.randint(100, WIDTH - 100)

    def draw(self):
        pygame.draw.circle(screen, ROSE_COLOR, (int(self.x), int(self.y)), self.size)

# Heartfelt birthday message (instead of random quotes)
heartfelt_message = (
    "Happy Birthday, my love! From the moment we met, I knew that my life would never be the same. "
    "You are the light in my world, the reason my heart beats stronger every day. Your smile, your laughter, your presence, "
    "fill my life with so much joy and warmth. There are no words that can truly capture the depth of my feelings for you. "
    "You are my best friend, my soulmate, and the love of my life. Every moment with you feels like a beautiful dream come true, "
    "and today, on your special day, I just want you to know how incredibly grateful I am to have you by my side. "
    "Happy Birthday to the one who makes my heart soar. I love you more than words could ever say, and I look forward to "
    "celebrating many more birthdays with you, my love. 💖"
)

# Function to display the heartfelt message
def display_heartfelt_message():
    font = pygame.font.Font(None, 30)
    # Split the message into multiple lines to fit the screen
    lines = [heartfelt_message[i:i + 70] for i in range(0, len(heartfelt_message), 70)]
    
    # Display each line
    y_position = HEIGHT // 2 + 100
    for line in lines:
        text = font.render(line, True, QUOTE_COLOR)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y_position))
        y_position += 35  # Move down for the next line

def main():
    # Create random balloons, hearts, stars, and roses
    balloons = [Balloon(random.randint(100, WIDTH-100), random.randint(HEIGHT, HEIGHT+100), random.choice(BALLOON_COLORS)) for _ in range(10)]
    hearts = [Heart(random.randint(100, WIDTH-100), random.randint(HEIGHT, HEIGHT+100)) for _ in range(5)]
    stars = [Star(random.randint(100, WIDTH-100), random.randint(HEIGHT, HEIGHT+100)) for _ in range(5)]
    roses = [Rose(random.randint(100, WIDTH-100), random.randint(HEIGHT, HEIGHT+100)) for _ in range(5)]

    # Font for the "Happy Birthday" message
    font = pygame.font.Font(None, 60)
    title_text = font.render("Happy Birthday, My Love!", True, QUOTE_COLOR)

    while True:
        screen.fill(BLACK)  # Fill the screen with black background
        
        # Draw the title
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 100))
        
        # Move and draw each balloon
        for balloon in balloons:
            balloon.move()
            balloon.draw()

        # Move and draw each heart symbol
        for heart in hearts:
            heart.move()
            heart.draw()

        # Move and draw each star symbol
        for star in stars:
            star.move()
            star.draw()

        # Move and draw each rose symbol
        for rose in roses:
            rose.move()
            rose.draw()

        # Display the heartfelt birthday message
        display_heartfelt_message()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()  # Update the screen
        pygame.time.delay(10)  # Delay to control the speed of animation

if __name__ == "__main__":
    main()
