from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.database import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Playlist(Base):

    __tablename__ = "playlists"
    playlist_id = Column(Integer, primary_key=True)
    playlist_name = Column(String)
    artist = Column(String)
    spotify_id = Column(String)
    tracks = relationship("Track", back_populates="playlist")

class Track(Base):
    
    __tablename__ = "tracks"
    track_id = Column(Integer, primary_key=True)
    track_name = Column(String)
    album = Column(String)
    duration_ms = Column(Integer)
    spotify_id = Column(String)
    playlist_id = Column(Integer, ForeignKey("playlists.playlist_id"))
    playlist = relationship("Playlist", back_populates="tracks")

Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    preferences = Column(JSON)
    playlists = relationship("Playlist", back_populates="user")
    playlists.user = relationship("User", back_populates="playlists")
    