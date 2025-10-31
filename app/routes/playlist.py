from pydoc import plainpager
from services import parse_vibe, generate_playlist
import fastapi


app = fastapi.FastAPI()


@app.get("/playlist")
async def get_playlist():
    """
    Retrieves a playlist.
    """
    return {"message": "Hello World"}


@app.post("/parse-vibe")
async def parse_vibe():
    """
    Parses the user request to the LLM.
    """
    # TODO: Implement parsing logic
    # Example:
    # vibe = request.json()
    # parsed_vibe = parse_vibe(vibe)
    # return parsed_vibe

    return {"message": "Hello World"}


@app.post("/generate-playlist")
async def generate_playlist():
    """
    Generates a playlist based on the parsed vibe.
    """
    # TODO: Implement playlist generation logic
    # Example:
    # parsed_vibe = await parse_vibe()
    # playlist = generate_playlist(parsed_vibe)
    # return playlist
    playlist = generate_playlist()

    return {"playlist": playlist}

    """
    This returns something like this

    {
        playlist: [
        {
            "title": "Song Title",
            "artist": "Artist Name",
            "duration": "3:45",
            "url": "https://example.com/song.mp3"
        },
        {
            "title": "Another Song Title",
            "artist": "Another Artist Name",
            "duration": "4:12",
            "url": "https://example.com/another_song.mp3"
        }
    ]}
    """
