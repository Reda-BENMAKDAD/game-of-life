# Game Of Life
> This is a simple implementation of Conway's Game of Life in Python.

## What is Conway's Game of Life?
According to wikipedia : 
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input (you don't actually play it with someone). One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

## Rules
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
## Implementation Details
This implementation uses the pygame library to create a visual representation of Conway's Game of Life. The grid is initialized with a random configuration of alive and dead cells. The evolution of the cells is then displayed on the screen, following the rules mentioned above.

## Usage
You can run the game using the following command:
```bash
python main.py
```

### Parameters
> the script can be ran with some parameters to customize it :
- **Screen Dimensions**: The dimensions of the screen can be set using command-line arguments (`-sw` for screen width, `-sh` for screen height).
- **Cell Dimensions**: The dimensions of each individual cell can also be specified (`-cw` for cell width, `-ch` for cell height).
- **Initial Configuration**: The number of cells alive at the start of the game can be set using the `-a` or `--alive` argument.
- **Frames per Second (FPS)**: The speed of the game, or how much time each generation is shown on the screen, can be controlled with the `-f` or `--fps` argument.

### Example
```bash
python game_of_life.py -sw 800 -sh 600 -cw 20 -ch 20 -a 150 -f 5
```

### you can display the help message using the `-h` or `--help` argument.
```bash
python main.py -h
```

## Future Improvements
- [ ] Add a camera to be able to scroll through a large number of cells.
- [ ] make an feature where the user can draw the first generation of cells, and lunch the game from there

## Contributing
If you have any suggestions or improvements, or notice a bug, please feel free to open a pull request or an issue. Any contributions are welcome.

## Conclusion
This was a fun project to work on, and I learned a lot about Conway's Game of Life and pygame. I hope you enjoy playing around with it as much as I did. Recreational programming for life !


