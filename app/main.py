from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.models.game_model import GameModel

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# In-memory storage for active games
active_games = {}

@app.get("/")
async def root():
    return {"message": "Welcome to Continental Card Game API"}

@app.websocket("/ws/{game_id}")
async def websocket_endpoint(websocket: WebSocket, game_id: str):
    await websocket.accept()
    
    if game_id not in active_games:
        active_games[game_id] = GameModel(4)  # Start a new 4-player game
    
    game = active_games[game_id]
    
    try:
        while True:
            data = await websocket.receive_json()
            # Process the received data and update the game state
            # This is where you'll implement the game logic
            action = data.get('action')
            if action == 'draw_card':
                game.draw_card(data['player_index'])
            elif action == 'play_card':
                game.play_card(data['player_index'], data['card_index'])
            # Add more actions as needed
            
            # Send updated game state back to the client
            await websocket.send_json(game.get_game_state())
    except WebSocketDisconnect:
        # Handle disconnection
        # You might want to implement logic to remove the game if all players have disconnected
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)