from dataclasses import dataclass
from fastapi import FastAPI
app = FastAPI()
from app.routes import router
app.include_router(router)


@app.post('/generate-playlist/')
def generate_playlist():

    # TODO: Implement playlist generation logic here

    return {"message": "Playlist generated"}


@app.get("/playlists/{playlist_id}")
def get_playlist(playlist_id: int):
    # TODO: Implement logic to retrieve a playlist by its ID
    return {"playlist_id": playlist_id}


@app.post("/users/")
def create_user():
    # TODO: Implement user creation logic here
    return {"message": "User created"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    # TODO: Implement logic to retrieve a user by their ID
    return {"user_id": user_id}


@app.get("/tracks/{track_id}")
def get_track(track_id: int):
    # TODO: Implement logic to retrieve a track by its ID
    return {"track_id": track_id}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)