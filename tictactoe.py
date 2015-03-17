def draw_grid(grid):
    # Draws the given tic tac toe grid.
    print("\n" + grid[0] + ' | ' + grid[1] + ' | ' + grid[2])
    print('---------')
    print(grid[3] + ' | ' + grid[4] + ' | ' + grid[5])
    print('---------')
    print(grid[6] + ' | ' + grid[7] + ' | ' + grid[8])

def grid_full(grid):
    # Returns True if the given grid is full, False if not.
    for i in grid:
        if(i == " "):
            return False
    return True

def winner(p, g):
    # Returns True if the given player has won on the given grid
    return ((g[0] == p and g[1] == p and g[2] == p) or
    (g[3] == p and g[4] == p and g[5] == p) or
    (g[6] == p and g[7] == p and g[8] == p) or
    (g[0] == p and g[3] == p and g[6] == p) or
    (g[1] == p and g[4] == p and g[7] == p) or
    (g[2] == p and g[5] == p and g[8] == p) or
    (g[0] == p and g[4] == p and g[8] == p) or
    (g[2] == p and g[4] == p and g[6] == p))

def check_win(grid):
    # Returns True if either player has won.
    return winner("X", grid) or winner("O", grid)

def who_won(pX, pO, grid):
    # Returns a string explaining who won the game.
    if(winner("X", grid)):
        return "\n" + pX + " wins!\n"
    elif(winner("O", grid)):
        return "\n" + pO + " wins!\n"
    else:
        return "\nA tie...how boring!\n"

def name_entry(player):
    # Returns the entered player's name truncated to 20 characters
    return input("Please enter player " + player + "'s name.\n>>> ")[0:20]

def space_taken(grid, move):
    # Returns True if the space "move" is taken in the given grid
    return grid[move] != " "

def human_move(grid):
    # Takes a valid human move for the current grid
    move = ""
    print("Please select a spot on the grid (1-9).")
    print("The grid is numbered starting at the top left and moving right.")
    while move not in "1 2 3 4 5 6 7 8 9".split() or space_taken(grid, int(move) - 1):
        move = input(">>> ")
        if(move not in "1 2 3 4 5 6 7 8 9".split()):
            print("Please enter a number between 1 and 9")
        elif(move in "1 2 3 4 5 6 7 8 9".split() and space_taken(grid, int(move) - 1)):
            print("That space is already taken. Please pick another.")
    return int(move) - 1
        
def human_turn(name, player, grid):
    # Runs a human's turn, returning the resulting grid
    print(name + "'s turn. (" + player + ")")
    draw_grid(grid)
    grid[human_move(grid)] = player
    return grid
    
def vs_human():
    # Runs a two-player game, returns empty string to main menu
    pX = name_entry("X")
    pO = name_entry("O")
    grid = [" "] * 9
    turn = True
    while(not grid_full(grid) and not check_win(grid)):
        if(turn):
            grid = human_turn(pX, "X", grid)
        else:
            grid = human_turn(pO, "O", grid)
        turn = not turn
    print(who_won(pX, pO, grid))
    return ""

def vs_cpu():
    # WILL RUN A VS CPU GAME
    print("NOT DONE")
    return ""

def leave():
    # Bids farewell
    print("Goodbye!")
    return "q"

# Fancy title menu as a string
menu = """ _______       ______           ______         __
/_  __(_)___  /_  __/__ _____  /_  __/__  ___ / /
 / / / / __/   / / / _ `/ __/   / / / _ \/ -_)_/ 
/_/ /_/\__/   /_/  \_,_/\__/   /_/  \___/\__(_)  
In Python! By John Bujalski!

(T)wo Player Game!
(V)s. CPU Game!
(Q)uit!

>>> """

# Menu selections as a dictionary
menu_selections = {
    "t" : vs_human,
    "v" : vs_cpu,
    "q" : leave,
}

# The whole game, main menu, etc.
def game():
    selection = ""
    while(selection != "q"):
        while(selection == ""):
            selection = input(menu)
        selection = selection[0].lower()
        if selection in menu_selections:
            selection = menu_selections[selection]()
        else:
            print("Please pick a valid menu option!")
            selection = ""

game()
