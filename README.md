# 🚀 SpacePilot

A classic space shooter game built with Python, featuring engaging gameplay, multiple power-ups, progressive difficulty levels, and polished visual effects.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎮 About

SpacePilot is an action-packed space shooter game where you pilot a spaceship to defend against waves of enemy invaders. Destroy all enemies to progress through levels, collect power-ups for advantages, and survive as long as possible to achieve the highest score!

## ✨ Features

### Core Gameplay
- **Smooth Movement**: Control your spaceship with arrow keys for precise movement
- **Combat System**: Shoot enemies with spacebar, each enemy type has unique behavior
- **Progressive Difficulty**: Enemy count increases with each level
- **Life System**: Start with 3 lives, lose lives when hit by enemies or when they escape

### Power-Ups
- **🛡️ Shield** (Blue): Provides temporary invincibility
- **⚡ Fire Rate Boost** (Red): Doubles your shooting speed
- **❤️ Extra Life** (Green): Adds one additional life

### Visual & Audio
- **Animated Sprites**: Smooth sprite sheet animations for all game entities
- **Particle Effects**: Visual feedback for explosions and power-up collection
- **Background Music**: Immersive background soundtrack
- **Sound Effects**: Audio cues for shooting, explosions, power-ups, and level transitions

### Game States
- **Start Menu**: Navigate between Start, Help, and Exit options
- **Help Screen**: Comprehensive game instructions
- **In-Game**: Main gameplay with real-time stats display
- **Level Transition**: Visual feedback when advancing levels
- **Game Over**: Display final score and level achieved

## 🎯 How to Play

### Controls
- **Arrow Keys**: Move spaceship (Up, Down, Left, Right)
- **Spacebar**: Shoot bullets
- **M**: Return to main menu (from Help or Game Over screen)
- **R**: Restart game (from Game Over screen)
- **E**: Exit game (from Game Over screen)

### Objectives
1. **Destroy Enemies**: Eliminate all enemies to advance to the next level
2. **Collect Power-Ups**: Pick up power-ups that drop from defeated enemies
3. **Survive**: Avoid enemy bullets and prevent enemies from escaping
4. **Score High**: Maximize your score by defeating enemies efficiently

### Game Mechanics
- Enemies spawn at the top and move downward
- Larger enemies move faster and shoot more frequently
- Taking damage or letting enemies escape reduces your lives
- When all lives are lost, the game ends
- Each level increases enemy count: `level * 2.5 + 3` enemies

## 📋 Requirements

- Python 3.x
- `SimpleGUICS2Pygame` or `simplegui` (for CodeSkulptor compatibility)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mahdiyyeh/SpacePilot.git
   cd SpacePilot
   ```

2. **Install dependencies**:
   ```bash
   pip install SimpleGUICS2Pygame
   ```

   Or if using CodeSkulptor/online Python environment, `simplegui` is already available.

3. **Run the game**:
   ```bash
   python Game.py
   ```

## 📁 Project Structure

```
SpacePilot/
├── Game.py                 # Main game loop and state management
├── Player.py               # Player ship logic and controls
├── Enemy.py                # Enemy entity implementation
├── EnemyManager.py         # Enemy spawning and management
├── Bullet.py               # Bullet physics and rendering
├── Powerup.py              # Power-up entity
├── PowerupManager.py       # Power-up spawning and effects
├── PowerupEffect.py        # Power-up effect types
├── CollisionHandler.py     # Collision detection system
├── Explosion.py            # Explosion effects
├── Effect.py               # Visual effects
├── ScoreIndicator.py       # Score display effects
├── Spritesheet.py          # Sprite animation system
├── Vector.py               # 2D vector math utilities
├── Clock.py                # Timer and clock utilities
├── GameState.py            # Game state enumeration
├── AssetLoader.py          # Image and sound loading utilities
├── Sound.py                # Audio management
├── Config.py               # Game configuration constants
├── assets/
│   ├── images/            # Game sprite sheets and backgrounds
│   └── sounds/            # Sound effects and music
└── README.md              # This file
```

## 🛠️ Technologies Used

- **Python 3**: Core programming language
- **SimpleGUI**: Graphics and input handling framework
- **SimpleGUICS2Pygame**: Alternative implementation for local execution
- **Object-Oriented Design**: Modular and maintainable code structure

## 🎨 Game Features Detail

### Enemy Types
- **Small Enemies**: Move slower, shoot less frequently
- **Medium Enemies**: Balanced movement and shooting
- **Large Enemies**: Fast movement, aggressive shooting patterns

### Scoring System
- Score increases based on enemy size and difficulty
- Visual score indicators appear when enemies are destroyed

### Level Progression
- Each level completion triggers a level-up animation
- Enemy count scales with level number
- Difficulty increases progressively

## 🚧 Future Enhancements

Potential features for future versions:
- [ ] High score persistence
- [ ] Boss battles
- [ ] Multiple weapon types
- [ ] Co-op multiplayer mode
- [ ] Additional power-up types
- [ ] Custom difficulty settings
- [ ] Achievement system

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/mahdiyyeh/SpacePilot/issues).

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Mahdiyyeh**

- GitHub: [@mahdiyyeh](https://github.com/mahdiyyeh)

## 🙏 Acknowledgments

- Inspired by classic space shooter games
- Built using SimpleGUI framework
- Assets created for educational/game development purposes

---

⭐ If you enjoy this game, please consider giving it a star!

