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

HOME = os.environ["HOME"]
SOUP_DB = f"{HOME}/gumbodama/db/soup.json"
USERS_DB = f"{HOME}/gumbodama/db/users.json" # HAVE NOT MADE THE USERS.JSON YET


def write_soup(soup):  # Write to soup db
    with open(SOUP_DB, 'w') as f:
        json.dump(soup, f, indent=4)
        
def write_users(users):
    with open(USERS_DB, 'w') as f:
        json.dump(users, f, indent=4)

def get_soup():
    """
    A function to return all soup inventory.
    """
    try:
        with open(SOUP_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None
        
        
def get_users():
    """
    A function to return users database.
    """
    try:
        with open(USERS_DB) as file:
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
        soup[soupname] = {"Inventory": 1}
        write_soup(soup)
        return 0

def delete_soup(soupname):
    """
    Delete soup from the db.
    """
    soup = get_soup
    if soup is None:
        return NOT_FOUND
    elif soupname not in soup:
        return 
    else:
        del soup[soupname]
        write_soup(soup)
        return 0
        

def add_user(username):  # Add a soup to the inventory
    users = get_users
    if users is None:
        return NOT_FOUND
    elif username in users:
        return DUPLICATE
    else:
        users[username] = {"Loves Soup?": 1}
        write_soup(users)
        return 0

def delete_user(username):
    users = get_users
    if users is None: # repetetive programming ik, but straightforward
        return NOT_FOUND
    elif username not in users:
        return NOT_FOUND
    else:
        del users[username]
        write_soup(users)
        return 0
