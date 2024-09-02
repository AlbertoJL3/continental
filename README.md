# Continental Card Game

Continental is a multiplayer card game built for the web. This project implements the game using vanilla JavaScript with an MVC (Model-View-Controller) architecture and Observer pattern.

## Features

- Multiplayer gameplay with 2-10 players
- Real-time game updates using WebSockets
- Responsive design for desktop and mobile play
- Implementation of all Continental game rules and rounds

## Technologies Used

- Frontend: Vanilla JavaScript, HTML5, CSS3
- Backend: Node.js with Express.js
- Real-time Communication: Socket.io
- Build Tool: Webpack
- Testing: Jest

## Getting Started

### Prerequisites

- Node.js (v14.0.0 or later)
- npm (v6.0.0 or later)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/continental-card-game.git
   cd continental-card-game
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run dev
   ```

4. Open your browser and navigate to `http://localhost:3000`

## Project Structure

- `src/js/model/`: Contains the game logic and state management
- `src/js/view/`: Handles the rendering of game elements
- `src/js/controller/`: Manages user interactions and game flow
- `src/css/`: Contains all styling for the game
- `src/assets/`: Stores images and other static assets
- `server/`: Contains the server-side code for multiplayer functionality
- `tests/`: Contains unit and integration tests

## Running Tests

Run all tests:
```
npm test
```

Run tests with coverage:
```
npm run test:coverage
```

## Deployment

To build the project for production:
```
npm run build
```

This will create a `dist/` directory with all the compiled and minified files.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.