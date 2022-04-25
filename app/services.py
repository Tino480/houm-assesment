import requests
import json
from typing import List


def get_pokemons_with_at_in_name_and_two_a() -> int:
    results = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=5000").json()[
        "results"
    ]
    pokemons = [
        pokemon["name"]
        for pokemon in results
        if "at" in pokemon["name"] and pokemon["name"].count("a") == 2
    ]
    return len(pokemons)


def get_number_of_species_raichu_can_procreate() -> int:
    result = requests.get("https://pokeapi.co/api/v2/pokemon-species/raichu/").json()
    egg_groups = result["egg_groups"]
    species_in_egg_groups = set()
    for egg_group in egg_groups:
        species = requests.get(
            "https://pokeapi.co/api/v2/egg-group/" + egg_group["name"] + "/"
        ).json()["pokemon_species"]
        for species_name in species:
            species_in_egg_groups.add(species_name["name"])
    return len(species_in_egg_groups)


async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def get_max_min_fighting_type(client) -> List[int]:
    fighting_pokemon = requests.get("https://pokeapi.co/api/v2/type/fighting/").json()[
        "pokemon"
    ]
    pokemon_urls = [
        url["pokemon"]["url"]
        for url in fighting_pokemon
        if int(
            url["pokemon"]["url"]
            .replace("https://pokeapi.co/api/v2/pokemon/", "")
            .replace("/", "")
        )
        <= 151
    ]
    pokemons = []
    for url in pokemon_urls:
        pokemon = await get_json(client, url)
        pokemons.append(
            {
                "species": json.loads(pokemon.decode("utf-8"))["species"],
                "weight": json.loads(pokemon.decode("utf-8"))["weight"],
            }
        )
    gen_one_pokemons = requests.get("https://pokeapi.co/api/v2/generation/1/").json()[
        "pokemon_species"
    ]
    gen_one_urls = [url["url"] for url in gen_one_pokemons]
    weights = []
    for pokemon in pokemons:
        if pokemon["species"]["url"] in gen_one_urls:
            weights.append(int(pokemon["weight"]))
    return [max(weights), min(weights)]
