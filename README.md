# Sea Battle 2 Project
## Introduction
Sea Battle 2 is a mobile game where you and the enemy each have a 10x10 matrix to position your fleets, composed of 4 ships with 1 cell, 3 ships with 2 cells, 2 ships with 3 cells, and 1 ship with 4 cells. The goal is to hit cells that contain parts or entire enemy ships before they hit yours.

## Motivation
1. The default UI doesn't provide a way to keep track of how many and what types of ships the enemy still has on the playground. Therefore, I needed a way to monitor this information, hence the Flutter project.
2. It would be wasteful not to screenshot all players visible matrices at the end of each game and utilize this data to create a heatmap, allowing me to make informed decisions, study player behavior, and potentially identify patterns. Hence, the Python project.

## Features
- **Flutter UI Overlay:** Track enemy ship status with a modern Flutter interface overlay.
- **Behavioral Analysis:** Study player actions to identify strategic patterns and tendencies.
- **Heatmap Visualization:** Visualize popular player moves with a heatmap, from frequent (green) to rare (red).
- **Decision Support:** Utilize data insights for strategic planning and optimized gameplay.

## Installation
### Python
1. Clone the repository.
2. Navigate to the python folder and execute this command to install all required libraries. `pip install -r requirements.txt`
3. Insert more images of enemy's playground in the images/ folder.
4. Execute main.py.

### Flutter
1. Clone the repository.
2. Either compile an APK or execute the app on your device, which will automatically create an APK for you.

## Potential Features
1. Create a backend in Python with Flask that includes a route for receiving pictures and another for providing the next most recurring cell.
2. Add a "take screenshot" button in the Flutter overlay that sends the picture to a backend at the end of the game or have it taken automatically based on computer vision on the Flutter app side.
3. Implement a "show suggestion" button in the Flutter overlay that highlights the cell with the highest probability of containing an enemy ship.
4. Gather more data than just the cell counts and implement machine learning to automate gameplay (create a bot).
5. Explore reinforcement learning techniques.

## Contributing
Contributions are welcome! Improve UI, enhance analysis algorithms, or suggest new features by submitting a pull request.
