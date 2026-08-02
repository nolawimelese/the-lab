import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    clock.tick(24)

pygame.quit()

# use pygame.Vector2 for position and velocity
# methods: init, update, and draw
# flock should be updated, and then drawn in a loop

class Boid:
    def __init__(self, x, y, vx, vy):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(vx, vy)

    def update(self):
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, 1)