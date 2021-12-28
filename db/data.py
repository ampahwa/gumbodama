
import db.db_connect as dbc

SOUPS = "soups"
USERS = "users"

# field names in our DB:
USER_NM = "userName"
SOUP_NM = "soupName"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)
else: print(f"{client=}")


def get_soup():
    """
    A function to return a dictionary of all soups.
    """
    return dbc.fetch_all(SOUPS, SOUP_NM)


def soup_exists(soupname):
    """
    See if a soup with soupname is in the db.
    Returns True of False.
    """
    rec = dbc.fetch_one(SOUPS, filters={SOUP_NM: soupname})
    print(f"{rec=}")
    return rec is not None


def del_soup(soupname):
    """
    Delete roomname from the db.
    """
    if not soup_exists(soupname):
        return NOT_FOUND
    else:
        dbc.del_one(SOUPS, filters={SOUP_NM: soupname})
        return OK


def add_soup(soupname):
    """
    Add a room to the room database.
    """
    print(f"{soupname=}")
    if soup_exists(soupname):
        return DUPLICATE
    else:
        dbc.insert_doc(SOUPS, {SOUP_NM: soupname,
                               "Inventory": 0,
                               "Desc:": ""})
        return OK


def user_exists(username):
    """
    See if a user with username is in the db.
    Returns True of False.
    """
    rec = dbc.fetch_one(USERS, filters={USER_NM: username})
    print(f"{rec=}")
    return rec is not None


def get_users():
    """
    A function to return a dictionary of all users.
    """
    return dbc.fetch_all(USERS, USER_NM)


def add_user(username):
    """
    Add a user to the user database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    if user_exists(username):
        return DUPLICATE
    else:
        dbc.insert_doc(USERS, {USER_NM: username})
        return OK


def del_user(username):
    """
    Delete username from the db.
    """
    if not user_exists(username):
        return NOT_FOUND
    else:
        dbc.del_one(USERS, filters={USER_NM: username})
        return OK