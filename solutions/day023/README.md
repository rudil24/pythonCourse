# CAPSTONE project: Turtle Crossing Game
Day 23 in the 100 days of Python! 
## Project Description
Build a "frogger-like" road crossing game using Python Turtle library, with heavy reliance on object oriented programming (OOP) structure.
In the game, 
  1. A turtle moves forwards (moving from bottom of screen to top of screen) when you press the "Up" key. 
     * for this first iteration of the game, it can only move forwards, not back, left or right.
  2. Cars (rectangular blocks randomly colored from a color list) are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
  3. A turtle "dies" if a car contacts it. Then the turtle starts again from the bottom of the screen unless out of lives.
  4. A turtle completes a level if he makes it all the way to the top of the screen. Then:
     * the level increments
     * the turtle moves back to bottom of screen and restarts the next level
     * the cars are a bit faster and more frequent as you go up in levels.
  5. 3 lives and the game is over.

## Deliverables
### MVP: 
- [x] build a working Turtle Crossing Game as described above, on local machine, using starting project files in day023 folder
- [x] utilize object oriented programming (classes and methods in external files, class inheritance, keeping main.py very tight and readable for game flow only, etc.)
- [x] add "3 lives" and "increased car frequency" (more traffic, not just speed) as project musts for playability (Angela's version does not have these)
### stretch goals: 
- [x] high score (highest level achieved) saved to data.txt file
- [x] instead of uniform speed for all cars that increases with level, make different speeds for individual cars (also increasing relative speed, each level)
- [ ] possible improvements to turtle movement (4-way movement and turtle orientation, instead of just up.)
- [ ] investigate possible graphics improvement to cars (just rectangles, really?)
- [ ] build even more of a Frogger knockoff, where you land 5 turtles in 5 pods going from left to right at the top of the screen, before you level up.

## Mockup
![docs/turtle-crossing-image.png](docs/turtle-crossing-image.png)

## To Run
  1. For now, clone to local deployment only. Requires Turtle and Time packages (usually included in your standard Python install).
  1. I built it in Python 3.14.2, but I think it should work in any 3.x based on the standard libraries and code used.

## Development Workflow
- [x] 1. Create the screen 
- [x] 2. Create turtle and turtle movement
- [x] 3. Car spawning and movement (remember, more cars and faster cars as levels increase)
- [x] 4. Detect collision between turtle and car; end of life sequence
- [x] 5. Detect level complete; increment level; start next level
- [x] 6. Keep scoreboard of current level
- [x] 7. DEPLOY and TEST (locally) 
- [x] 8. improve playability via less cars spawning on earliest level (since they are slowest moving across the screen, spawns need to slow or we get a bit of a traffic jam. fixed that.)

## Reflection
| DATE  | NOTES |
|---|---|
| 14-jan-2026 | SUMMARY: Running short on time & need to get to the next day, but got all MVP features working (which include extra "lives' and "traffic" features), also 2 of the "high want" features (high score feature and varying car speeds.) Moving on! |
| 13-jan-2026 | I like the simple README's I've started doing for each day's project, they seem like just the right amount of description, mockup, and dev steps. much easier than a full-blown Product Req's Document, which will come into play I'm sure on later projects. |



## References
  * [Google Q&A: Can I can go further on car shapes using Turtle library](docs/qa_on_car_shapes.md)
