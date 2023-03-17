import tkinter as tk
import random
import time

WIDTH = 1400
HEIGHT = 750

BASKETBALL_FIELD_WIDTH = 1400
BASKETBALL_FIELD_HEIGHT = 750

NUM_PLAYERS_PER_TEAM = 5

TEAM_COLORS = ["blue", "red"]

PLAYER_NAMES = ["Mikael", "Carlos Antonio", "Titouan", "Thomas", "Elisa",
"Alois", "Marie", "Enora", "Arrel", "Eva"]

players = []

root = tk.Tk()
root.title("Basketball Players Simulation")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

bg_img = tk.PhotoImage(file="basketball_court (1).png")
canvas.create_image(0, 0, anchor=tk.NW, image=bg_img)

canvas.pack()

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
        self.x += self.dx
        self.y += self.dy

        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.dx *= -1
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.dy *= -1

        self.canvas.move(self.object, self.dx, self.dy)
        self.canvas.move(self.text_object, self.dx, self.dy)

def update(elapsed_time):
    for player in players:
        if elapsed_time % 5 == 0:
            print(f"{player.player_name} : ({player.x}, {player.y}), top-left: (0, 0), top-right: ({BASKETBALL_FIELD_WIDTH}, 0), bottom-left: (0, {BASKETBALL_FIELD_HEIGHT}), bottom-right: ({BASKETBALL_FIELD_WIDTH}, {BASKETBALL_FIELD_HEIGHT})")
    if elapsed_time < 60:
        time.sleep(1)
        update(elapsed_time+1)

for i in range(NUM_PLAYERS_PER_TEAM * 2):
    team_color = TEAM_COLORS[i // NUM_PLAYERS_PER_TEAM]
    player_name = PLAYER_NAMES[i % NUM_PLAYERS_PER_TEAM + (i // NUM_PLAYERS_PER_TEAM) * NUM_PLAYERS_PER_TEAM]
    player = Player(canvas, team_color, player_name)
    players.append(player)

update(0)
root.mainloop()
