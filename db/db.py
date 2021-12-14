"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""


import json
import os

# Errors
NOT_FOUND = 1
DUPLICATE = 2

DEMO_HOME = os.environ["DEMO_HOME"]
SOUP_DB = f"{DEMO_HOME}/gumbodama/db/soup.json"


def write_soup(soup):  # Write to soup db
    with open(SOUP_DB, 'w') as f:
        json.dump(soup, f, indent=4)


def get_soup():
    """
    A function to return all soup inventory.
    """
    try:
        with open(SOUP_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None


def add_soup(soupname):  # Add a soup to the inventory
    soup = get_soup
    if soup is None:
        return NOT_FOUND
    elif soupname in soup:
        return DUPLICATE
    else:
        soup[soupname] = {"Inventory": 0}
        write_soup(soup)
        return 0
