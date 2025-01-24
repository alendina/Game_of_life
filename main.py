from game_of_life import GameOfLife  # Import the GameOfLife class

def main():
    # Initialize the grid dimensions
    x_dim = 20  # Number of columns
    y_dim = 25  # Number of rows

    # Create an instance of the GameOfLife
    game = GameOfLife(x_dim, y_dim)

    # Define initial live cells (x, y) coordinates
    initial_cells = [(9, 17), (10, 17), (11, 17), (10, 16), (11, 18), (9, 18), (10, 19),
                     (9, 7), (10, 7), (11, 7), (10, 6), (11, 8), (9, 8), (10, 9)]
    game.populate_grid(initial_cells)  # Populate the grid with initial live cells

    # Print the initial grid
    print("Initial Grid:")
    game.print_grid()

    # Draw the grid and run the simulation
    # Choose your preferred draw method:
    #       1'scatter' : Visualization method with scatter plots,
    #       2'heatmap' : Visualization method with binary matrix
    #       3'n_steps' : Print each step and show the plot draw_changing_life
    # Set the maximum number of steps
    game.draw_grid(dtype="1", steps=70)

    # Print the grid after the simulation
    print(f"The greed after {game.max_steps}:")
    game.print_grid()


if __name__ == "__main__":
    main()