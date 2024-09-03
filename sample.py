import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Register the bomb image
turtle.register_shape("C:\\PYTHON\\SEM-1\\Snakegame\\bbomb.gif")  # Replace "bomb.gif" with your actual image file

# Create the bomb turtle
bomb_turtle = turtle.Turtle("C:\\PYTHON\\SEM-1\\Snakegame\\bbomb.gif")
bomb_turtle.speed(1)  # Set the speed of the bomb

# Function to explode
def explode():
    turtle.color("red", "orange")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

# Move the bomb and trigger explosion
def move_bomb():
    bomb_turtle.forward(10)
    x, y = bomb_turtle.position()
    if x > 100:  # Replace 100 with the desired x-coordinate for explosion
        explode()

# Set up the animation loop
while True:
    move_bomb()
    screen.update()
    time.sleep(0.1)  # Adjust the sleep time for the desired speed

# Keep the window open until closed by the user
turtle.done()


