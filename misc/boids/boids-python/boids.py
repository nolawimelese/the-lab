import pygame

# use pygame.Vector2 for position and velocity
# methods: init, update, and draw
# flock should be updated, and then drawn in a loop

# parameters
# neighbor radius: how close birds have to be to be classified as neighbors
neighbor_radius = 50
sep_weight = .3
aln_weight = .3
coh_weight = .3
speed_limit = 5
boid_size = 5

class Boid:
    def __init__(self, x, y, vx, vy):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(vx, vy)
        self.neighbors = []

    def separation(self, neighbors):
        sep = pygame.Vector2()
        for b in neighbors:
            if (self.position != b.position): # just in case 2 boids are in the same pos
                sep += (self.position - b.position)/self.position.distance_to(b.position)**2
        if len(neighbors) == 0:
            return sep
        return sep / len(neighbors)

    def alignment(self, neighbors):
        aln = pygame.Vector2()
        for b in neighbors:
            aln += b.velocity
        if len(neighbors) == 0:
            return aln
        return (aln / len(neighbors)) - self.velocity # subtract velocity so 2 perfectly aligned boids don't just speed up

    def cohesion(self, neighbors):
        coh = pygame.Vector2()
        return coh

    def update(self, flock):
        self.neighbors = [b for b in flock if b is not self and self.position.distance_to(b.position) < neighbor_radius]
        self.velocity += (sep_weight * self.separation(self.neighbors)) + (aln_weight * self.alignment(self.neighbors)) + (coh_weight * self.cohesion(self.neighbors))
        if (self.velocity.magnitude() > speed_limit):
            self.velocity.scale_to_length(speed_limit)
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, boid_size)


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

flock = [Boid(100,100,1,1), Boid(110,100,1,1), Boid(100,110,1,1)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

    for boid in flock:
        boid.update(flock)
        boid.draw(screen)
    
    pygame.display.flip()
    clock.tick(24)

pygame.quit()
