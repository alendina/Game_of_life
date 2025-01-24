import matplotlib.pyplot as plt

class GameOfLife(object):
    """
    Implementation of Conway's Game of Life.
    """
    def __init__(self, x_dim, y_dim):
        """ row, column
        Initializes the Game of Life grid.

        Parameters:
        x_dim (int): Number of rows  in the grid.
        y_dim (int): Number of columns in the grid.
        """
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.max_steps = 50
        self.counts_life = []
        self.init_state = [[0] * y_dim for _ in range(x_dim)]
        self.current_state = self.init_state

    def set_max_steps(self, max_steps: int):
        """
        Sets the maximum number of steps the game will run.

        Parameters:
        max_steps (int): The maximum number of steps.
        """
        self.max_steps = max_steps

    def get_grid(self):
        """
        Retrieves the current state of the grid.

        Returns:
        list: A 2D list representing the current state of the grid.
        """
        return self.current_state

    def print_grid(self):
        """
        Prints the current state of the grid in a human-readable format.
        """
        for row in self.get_grid():
            print(*row, sep=' ')
        print()

    def populate_grid(self, coord):
        """
        Populates the game grid with live cells at the specified coordinates.

        Parameters:
        coord: A list of tuples. Each tuple represents the (x, y) coordinates of a live cell.

        Returns:
        The updated life_grid with the new live cells.
        """
        for x, y in coord:
            self.current_state[x][y] = 1

    def count_neighbors(self, x: int, y: int) -> int:
        """
        Prints the current state of the grid in a human-readable format.

        Parameters:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        """
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x + i < self.x_dim and 0 <= y + j < self.y_dim:
                    count += self.current_state[x + i][y + j]
        return count

    def make_step(self):
        """
        Updates the game state according to the rules of Conway's Game of Life.
        """
        # Calculate sums of neighbors for each cell to new matrix
        neighbors_sums = [[self.count_neighbors(i, j) for j in range(self.y_dim)] for i in range(self.x_dim)]

        # Update the game state each cell based on the matrix neighbors_sums

        for i in range(self.x_dim):
            for j in range(self.y_dim):
                neighbors = neighbors_sums[i][j]
                if self.current_state[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        self.current_state[i][j] = 0
                else:
                    if neighbors == 3:
                        self.current_state[i][j] = 1

    def get_count_life(self):
        """
        Returns the number of live cells in the grid.

        Returns:
        int: The number of live cells in the grid.
        """
        sum_life = 0
        for i in range(self.x_dim):
            sum_life += sum(self.current_state[i])

        return sum_life

    def draw_changing_life(self):
        """
        Plots the number of live cells over time.
        """
        x = range(1, len(self.counts_life) + 1)
        plt.figure(figsize=(40, 2),)
        plt.plot(x, self.counts_life, label="Live cells")
        plt.xlabel("Step")
        plt.ylabel("Number of live cells")
        plt.title("Number of live cells over time")
        plt.show()

    def make_n_steps(self):
        """
        Runs the game for a specified number of steps (defined by max_steps).
        Prints the grid at each step.
        """
        for i in range(self.max_steps):
            print(f"Step {i + 1}")
            self.make_step()
            self.counts_life.append(self.get_count_life())
            self.print_grid()
            # self.draw_grid()
        self.draw_changing_life()

    def new_x_y(self):
        """
        Separates the coordinates of live and dead cells for plotting.

        Returns:
        tuple: Four lists containing x and y coordinates for live and dead cells.
        """
        x1, x2, y1, y2 = [], [], [], []
        for j in range(self.y_dim):
            for i in range(self.x_dim):
                if self.current_state[i][j] == 1:
                    x1.append(i+1)
                    y1.append(j+1)
                else:
                    x2.append(i+1)
                    y2.append(j+1)
        return x1, x2, y1, y2

    def draw_grid1(self):
        """
        Visualizes the grid using a scatter plot. Updates the plot dynamically
        for each step of the game.
        """
        x3, x, y3, y = self.new_x_y()
        plt.ion()
        fig, ax = plt.subplots()

        # Create initial scatter plots (placeholders)
        scatter1 = ax.scatter([], [], color='white', edgecolor='black', s=50, alpha=0.5, label="Group 2")
        scatter2 = ax.scatter([], [], color='grey', edgecolor='black', s=50, alpha=0.2, label="Group 2")
        scatter3 = ax.scatter([], [], color='green', edgecolor='black', s=50, alpha=0.7, label="Group 1")

        # Set up the plot
        ax.set_xlim(0, self.y_dim + 1)
        ax.set_ylim(0, self.x_dim + 1)
        # Invert the y-axis so that the plot visually matches the printed version of the grid
        ax.invert_yaxis()
        plt.xticks(range(0, self.y_dim + 1, 2))  #  X-axis numbers
        plt.yticks(range(0, self.x_dim + 1, 2))

        # Update the scatter plot in a loop
        for i in range(self.max_steps):
            self.make_step()
            x1, x2, y1, y2 = self.new_x_y()

            # Update data for both scatter plots
            ax.set_title("Game of Life. Step " + str(i + 1) + " of " + str(self.max_steps))
            # scatter1.set_offsets(list(zip(x2, y2)))
            # scatter2.set_offsets(list(zip(x3, y3)))
            # scatter3.set_offsets(list(zip(x1, y1)))

            scatter1.set_offsets(list(zip(y2, x2)))
            scatter2.set_offsets(list(zip(y3, x3)))
            scatter3.set_offsets(list(zip(y1, x1)))

            plt.draw()  # Redraw the figure
            x3 = x1
            y3 = y1
            plt.pause(1)  # Pause for 1 second

        plt.ioff()  # Turn off interactive mode
        plt.show()  # Keep the plot open


    def draw_grid2(self):
        """
        Visualizes the grid using a heatmap. Updates the plot dynamically
        for each step of the game.
        """
        plt.ion()  # Enable interactive mode
        fig, ax = plt.subplots()
        im = ax.imshow(self.current_state, cmap="binary", vmin=0, vmax=1)

        # Set up the plot
        plt.xticks(range(0, self.x_dim + 1, 2))  # X-axis numbers
        plt.yticks(range(0, self.y_dim + 1, 2))

        # Update the plot in a loop
        for i in range(self.max_steps):
            ax.set_title("Game of Life. Step " + str(i + 1) + " of " + str(self.max_steps))
            self.make_step()
            im.set_data(self.current_state) # Make the Step and Update the plot data
            plt.draw()  # Redraw the plot
            plt.pause(1)  # Pause for 500ms

        plt.ioff()  # Disable interactive mode
        plt.show()

    def draw_grid(self, dtype="scatter", steps=10):
        """
        Visualizes the grid using different types of drawing (1'scatter',  2'heatmap', 3'n_steps').

        Parameters:
        dtype (str): Type of plot to draw. Default is 'scatter'.
        steps (int): Number of steps to run the game. Default is 10.
        """
        self.set_max_steps(steps)
        if dtype == "scatter" or dtype == '1': # Scatter plot
            self.draw_grid1()
        elif dtype == "heatmap" or dtype == '2': # Heatmap plot
            self.draw_grid2()
        elif dtype == "nsteps" or dtype == '3':
            self.make_n_steps() # print each step and show the plot draw_changing_life




life = GameOfLife(25, 25)
life.populate_grid([(14, 15), (15, 15), (16, 15), (15, 14), (16, 16), (14, 16), (15, 17)])
life.print_grid()
life.draw_grid(dtype="3", steps=20)
