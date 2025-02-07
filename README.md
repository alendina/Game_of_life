# Game of life
Conway’s Game of Life is a zero-player game requiring only an initial state and no further input. In its original setting, the game takes place on an infinite grid of square cells, each in one of two possible states: live or dead. Inplemented on Python, visualized by the scatter plot in an interactive step-by-step mode

## Description

This project was created in Python as part of the "Python Bootcamp" course offered by the 365 Data Science platform.

### The Game of Life evolves based on simple rules:

**Survival:**

- A live cell with 2 or 3 live neighbors remains alive.

- Otherwise, the cell dies due to loneliness (fewer than 2 neighbors) or overpopulation (4 or more neighbors).

**Reproduction:**

- A dead cell with exactly 3 live neighbors becomes a live cell.

- Any other number of neighbors keeps the cell dead.


This implementation allows you to set an initial state and visualize the game's evolution step-by-step.


## Requirements

To run this project, ensure you have:

- Python 3 installed on your system

- The matplotlib library for visualization

Install the required library using:

    pip install matplotlib
    
## Usage

**Running the Project**

- Clone or download the repository.

- Open a terminal or command prompt and navigate to the project directory.

 - Run the main.py file:

    python main.py
   

## Customization Options

You can customize the simulation by modifying parameters in the main.py file:

**Set Grid Dimensions:**

Define the grid size using x_dim (number of columns) and y_dim (number of rows).

    x_dim = 20
    y_dim = 20

**Initialize Live Cells:**

Specify the coordinates of live cells as a list of tuples:

    initial_cells = [(9, 17), (10, 17), (11, 17), (10, 16), (11, 18), (9, 18), (10, 19)]

**Select Visualization Method:**

Use game.draw_grid(dtype="method", steps=n) to choose the visualization type and set the maximum number of steps.

Available methods:

- 'scatter': Visualize using scatter plots.

- 'heatmap': Visualize using binary matrix.

- 'n_steps': Print each step and show the changing grid.

Example:

    game.draw_grid(dtype="scatter", steps=50)

## Example Visualizations

Different visualization methods:

Scatter Plot: Highlights live and dead cells interactively using scatter points.

<img width="600" alt="image" src="https://github.com/user-attachments/assets/9f51062e-87cb-4896-989d-291daae33366" />

N_steps: Print each step at the consol and Heatmap : Displays the grid as a binary matrix.

<img width="600" alt="image" src="https://github.com/user-attachments/assets/9b760ac2-6376-4782-a9b0-780e587c0372" />

Show the changing grid in time:

<img width="600" alt="image" src="https://github.com/user-attachments/assets/ff6ffc2c-a87e-4de3-aafe-400b5a19547e" />


## Notes

Make sure to install all dependencies before running the project.

Experiment with different grid sizes and initial states for unique outcomes!




