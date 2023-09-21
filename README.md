# Minesweeper

This is a version of the classic game Minesweeper coded by me. 
Additionally this project includes an automated solver.


## Description

Minesweeper is a logic puzzle video game. The game features a grid of clickable cells, with hidden "mines" scattered throughout the board. Each cell can have three states: unopened, opened, and flagged. 
A player selects a cell to open it (Double click Mouse-Button 1). If a player opens a mined cell, the game ends in a loss. Otherwise, the opened cell displays either a number, indicating the number of mines in its neighbouring cells, or a blank tile, and all adjacent non-mined cells will automatically be opened. Players can also flag a cell (Mouse-Button 3), visualised by a flag being put on the location, to denote that they believe a mine to be in that place. Flagged cells may be unflagged. 
The objective is to clear the board without detonating any mines, with help from clues about the number of neighboring mines in each field. 

The game can be played in 3 difficulty levels. As the difficulty level increases, so does the number of bombs and the size of the grid.


Alternativelly, there is a solver that once started, tries to solve the board using simple rules. However, a win is not guaranteed since in some game states this solver is forced to make a random guess which can result in a loss, namely:
-the first cell it chooses has a mine;
-the solver is stuck between two unopened cells and it must chose randomly;
-it reaches a dead-end and must choose a new random cell.

## Installation

Provide instructions on how to install and set up your project. Include any dependencies and prerequisites that need to be installed. You can use code blocks for clarity:


```bash
# Example installation commands
$ git clone https://github.com/yourusername/minesweeper.git
$ cd Minesweeper
$ python3 minesweeper.py




