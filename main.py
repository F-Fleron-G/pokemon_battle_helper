from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    types = Column(JSON)  # Array of Pokémon types
    strengths = Column(JSON)  # Array of strengths
    weaknesses = Column(JSON)  # Array of weaknesses
    moves = Column(JSON)  # Array of moves


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))


class DeckPokemon(Base):
    __tablename__ = "deck_pokemon"
    id = Column(Integer, primary_key=True, index=True)
    deck_id = Column(Integer, ForeignKey("decks.id"))
    pokemon_id = Column(Integer, ForeignKey("pokemon.id"))


app = FastAPI()


@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pokémon Battle Helper!"}


@app.get("/pokemon/{name}")
def get_pokemon(name: str):
    return {"name": name, "message": f"You searched for Pokémon: {name.capitalize()}"}


@app.get("/about")
def about_app():
    return {"info": "This app helps kids build Pokémon decks for the ultimate battle experience."}


@app.get("/search")
def search_pokemon(type: str = None):
    if type:
        return {"type": type, "message": f"Searching for Pokémon of type: {type}"}
    return {"message": "Please provide a type to search for Pokémon."}


@app.get("/pokemon/{name}/filter")
def filter_pokemon(name: str, type: str = None):
    if type:
        return {
            "name": name,
            "type": type,
            "message": f"Filtering Pokémon {name.capitalize()} for type: {type}",
        }
    return {"name": name, "message": f"No type filter applied for Pokémon: {name.capitalize()}"}
