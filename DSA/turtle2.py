import turtle

# Create a Turtle screen and set its attributes
screen = turtle.Screen()
screen.title("Turtle Diagram")
screen.bgcolor("white")

# Create a Turtle object
fishbone = turtle.Turtle()

# Function to draw a fishbone diagram branch
def draw_branch(branch_name):
    fishbone.penup()
    fishbone.goto(0, 0)
    fishbone.pendown()
    fishbone.write(branch_name, align="center", font=("Arial", 12, "normal"))
    fishbone.forward(100)
    fishbone.backward(100)

# Draw the head of the fishbone
draw_branch("Problem")

# Draw major categories
categories = ["People", "Process", "Equipment", "Materials", "Environment"]
for category in categories:
    fishbone.left(45)
    fishbone.forward(50)
    draw_branch(category)
    fishbone.right(45)

# Close the Turtle graphics window on click
screen.exitonclick()
