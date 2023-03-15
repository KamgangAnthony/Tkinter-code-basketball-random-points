import tkinter as tk
import random

# Define the size of the simulation area
WIDTH = 940
HEIGHT = 500

# Define the size of the basketball field
BASKETBALL_FIELD_WIDTH = 940
BASKETBALL_FIELD_HEIGHT = 500

# Define the number of players per team
NUM_PLAYERS_PER_TEAM = 5

# Define the colors of the two teams
TEAM_COLORS = ["blue", "red"]

# Create a list to store the player objects
players = []

# Define the Player class
class Player:
    def __init__(self, canvas, team_color):
        self.canvas = canvas
        self.team_color = team_color
        self.x = random.randint(0, BASKETBALL_FIELD_WIDTH)
        self.y = random.randint(0, BASKETBALL_FIELD_HEIGHT)
        self.radius = 10
        self.speed = 2
        self.dx = random.uniform(-self.speed, self.speed)
        self.dy = random.uniform(-self.speed, self.speed)
        self.object = canvas.create_oval(self.x-self.radius, self.y-self.radius,
                                         self.x+self.radius, self.y+self.radius,
                                         fill=team_color)

    def move(self):
        # Move the player
        self.x += self.dx
        self.y += self.dy

        # Check if the player hits the edge of the simulation area
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.dx *= -1
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.dy *= -1

        # Update the position of the player on the canvas
        self.canvas.move(self.object, self.dx, self.dy)

# Create the Tkinter window and canvas
root = tk.Tk()
root.title("Basketball Players Simulation")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Create the player objects and add them to the players list
for i in range(NUM_PLAYERS_PER_TEAM * 2):
    team_color = TEAM_COLORS[i // NUM_PLAYERS_PER_TEAM]
    player = Player(canvas, team_color)
    players.append(player)

# Define the update function for the animation
def update():
    for player in players:
        player.move()
    canvas.after(10, update)

# Start the animation
update()
root.mainloop()