## BOIDS

I started this idea with HTML in mind, but it'd be easier to code it in python with pygame. My solution is to code both, first in pygame with python, and second in HTML with JS

### The three rules

Each boid goes by this behavior

1. **Separation** — steer away from neighbors that are too close
2. **Alignment** — steer toward the average heading of neighbors
3. **Cohesion** — steer toward the average position of neighbors

### Things I might include for fun

- Mouse as a predator (or an attractor)
- Sliders for the weights and view radius, so I can play with it live
- Spatial hashing
- Obstacles?
