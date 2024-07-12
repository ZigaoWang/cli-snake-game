# Snake Game

Welcome to the Snake Game! This project is a modernized and slightly simplified version of the original game from [KevinMarquesP's Snake Game](https://github.com/kevinmarquesp/snake_game). The game is implemented using Python's `curses` library and features a simple menu, a playable snake game, and a scoreboard to keep track of your high scores.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Classes and Structure](#classes-and-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

To run the Snake Game, you need Python 3.x installed on your machine. You also need to ensure you have the `curses` library, which is typically included with Python on Unix-based systems.

1. **Clone the repository:**
    ```sh
    git clone https://github.com/ZigaoWang/cli-snake_game.git
    cd cli-snake_game
    ```

2. **Run the game:**
    ```sh
    python run.py
    ```

## Usage

1. **Menu Navigation:**
   - Use `W` or `Up Arrow` to move up.
   - Use `S` or `Down Arrow` to move down.
   - Press `Space` or `Enter` to select an option.

2. **Playing the Game:**
   - Use `W`, `A`, `S`, `D` or the arrow keys to move the snake.
   - Press `Space` or `Enter` to pause/unpause the game.
   - Collect apples (`░`) to grow the snake and increase your score.
   - Avoid hitting the walls or the snake's own body.

3. **Scoreboard:**
   - View your high scores in the "Scoreboard" menu option.
   - Scores are displayed along with the date and time of the game.

## Classes and Structure

### Globals
Stores essential game constants and configurations such as key mappings, menu items, and direction lists.

### Menu
Handles the game menu, allowing users to navigate through options like "Play", "Scoreboard", and "Exit".

### Play
Manages the core game logic, including the snake's movement, apple spawning, score tracking, and game-over conditions.

### ScoreBoard
Maintains a history of scores along with the date and time of each game. Displays the score list on the screen.

### Files

- **Game.py**: Contains the main game logic and class definitions.
- **run.py**: Entry point to start the game.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or create a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Original project by [KevinMarquesP](https://github.com/kevinmarquesp/snake_game).
- Python `curses` library for terminal handling.

Enjoy playing the Snake Game! 🐍🎮