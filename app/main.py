import asyncio
import aiohttp
from fastapi import FastAPI, status
from typing import List
from . import services

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)

app = FastAPI()


@app.get(
    "/pokemons_with_at_in_name_and_two_a/",
    status_code=status.HTTP_200_OK,
    response_model=int,
)
def read_posts():
    """Returns an integer representing how many pokemons
    have "at" in their names and have 2 letter a's in their name,
    including the first "at". Note it will only return names that
    have exactly 2 letter a's in their name"""
    return services.get_pokemons_with_at_in_name_and_two_a()


@app.get(
    "/number_of_species_raichu_can_procreate/",
    status_code=status.HTTP_200_OK,
    response_model=int,
)
def read_posts():
    """Returns an integer representing how many species of Pokémon
    Raichu breed with (2 Pokemon can spawn if they are in the same
    egg group.)"""
    return services.get_number_of_species_raichu_can_procreate()


@app.get(
    "/max_min_fighting_type", status_code=status.HTTP_200_OK, response_model=List[int]
)
async def read_posts():
    """Returns a List of integers representing the maximum and
    minimum weight of the first generation fighting type pokémon
    (whose id is less than or equal to 151)."""
    return await services.get_max_min_fighting_type(client)
