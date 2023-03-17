import tkinter as tk
import random
import time
import math

# Define the size of the simulation area
WIDTH = 1400
HEIGHT = 750
time_counter = 0
# Define the size of the basketball field
BASKETBALL_FIELD_WIDTH = 1400
BASKETBALL_FIELD_HEIGHT = 750

# Define the number of players per team
NUM_PLAYERS_PER_TEAM = 5

# Define the colors of the two teams
TEAM_COLORS = ["blue", "red"]

#player names
PLAYER_NAMES = ["Mikael", "Carlos Antonio", "Titouan", "Thomas", "Elisa",
"Alois", "Marie", "Enora", "Arrel", "Eva"]

# Create a list to store the player objects
players = []

# Create the Tkinter window and canvas
root = tk.Tk()
root.title("Basketball Players Simulation")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

# Load the background image
bg_img = tk.PhotoImage(file="basketball_court (1).png")
canvas.create_image(0, 0, anchor=tk.NW, image=bg_img)

canvas.pack()

# Define the Player class
class Player:
    def __init__(self, canvas, team_color, player_name):
        self.canvas = canvas
        self.team_color = team_color
        self.player_name = player_name
        self.x = random.randint(0, BASKETBALL_FIELD_WIDTH)
        self.y = random.randint(0, BASKETBALL_FIELD_HEIGHT)
        self.radius = 15
        self.speed = 2
        self.dx = random.uniform(-self.speed, self.speed)
        self.dy = random.uniform(-self.speed, self.speed)
        self.object = canvas.create_oval(self.x-self.radius, self.y-self.radius,
                                         self.x+self.radius, self.y+self.radius,
                                         fill=team_color)
        self.text_object = canvas.create_text(self.x, self.y - 20, text=self.player_name,
                                              fill="white", font=("Arial", 12))

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
        self.canvas.move(self.text_object, self.dx, self.dy)

# Create the player objects and add them to the players list
for i in range(NUM_PLAYERS_PER_TEAM * 2):
    team_color = TEAM_COLORS[i // NUM_PLAYERS_PER_TEAM]
    player_name = PLAYER_NAMES[i % NUM_PLAYERS_PER_TEAM + (i // NUM_PLAYERS_PER_TEAM) * NUM_PLAYERS_PER_TEAM]
    player = Player(canvas, team_color, player_name)
    players.append(player)


def display_position(players):
    # Get the coordinates of the four corners of the basketball field
    corners = [("bottom_left", 0, 0), ("top_left", 0, BASKETBALL_FIELD_HEIGHT),
               ("bottom_right", BASKETBALL_FIELD_WIDTH, 0), ("top_right", BASKETBALL_FIELD_WIDTH, BASKETBALL_FIELD_HEIGHT)]

    # Loop over each player and calculate the distance to each corner
    for player in players:
        distances = []
        for corner in corners:
            # Calculate the distance between the player and the corner using the Pythagorean theorem
            distance = math.sqrt((player.x - corner[1]) ** 2 + (player.y - corner[2]) ** 2)
            distances.append(int(distance))

        # Print the distances for the current player with labels for the corners
        print(f"{player.player_name}: {corners[0][0]}: {distances[0]}, {corners[1][0]}: {distances[1]}, {corners[2][0]}: {distances[2]}, {corners[3][0]}: {distances[3]}")

    # Add a separator between each player's distances for readability
    print("----------------------------------------------------------------\n\n")


# Define the update function for the animation
def update():
    global time_counter
    for player in players:
        player.move()
    time_counter += 1
    if time_counter % 150 == 0:  # display positions every 5 seconds
        display_position(players)
    canvas.after(10, update)


# Start the animation
update()
root.mainloop()
