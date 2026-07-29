# Cricket Team Management System

class Player:
    def __init__(self, name, jersey_no, runs):
        self.name = name
        self.jersey_no = jersey_no
        self.runs = runs

    # Categorize player based on runs
    def category(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"

    # Display player details
    def display(self):
        print(f"Player Name   : {self.name}")
        print(f"Jersey Number : {self.jersey_no}")
        print(f"Runs          : {self.runs}")
        print(f"Category      : {self.category()}")
        print("-" * 30)


class Team:
    def __init__(self):
        self.players = []

    # Add player to team
    def add_player(self, player):
        self.players.append(player)

    # Display all players
    def display_players(self):
        print("\n------ Team Players ------")
        for player in self.players:
            player.display()


# Main Program
team = Team()

n = int(input("Enter number of players: "))

for i in range(n):
    print(f"\nEnter details of Player {i + 1}")
    name = input("Player Name: ")
    jersey = int(input("Jersey Number: "))
    runs = int(input("Runs: "))

    player = Player(name, jersey, runs)
    team.add_player(player)

team.display_players()
