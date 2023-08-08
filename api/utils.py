import mariadb
import os
# def object_to_dict(obj):
#     return {c: getattr(obj, c) for c in dir(obj) if not c.startswith('_')}

def object_to_dict(obj)->dict:
    """Convert an object to a dictionary.
    Input:
        obj: any object
    Output:
        dict: returns a dictionary of the object"""
    return vars(obj)


def get_env_dict()->dict:
    user: str | None  = os.getenv("DB_USER")
    password: str | None  = os.getenv("DB_PASS")
    host: str | None  = os.getenv("DB_HOST")
    database: str | None = os.getenv("DB_DATABASE")
    dict_env: dict = {
        "user": user,
        "password": password,
        "host": host,
        "database": database
    }
    return dict_env

env_dict = get_env_dict()
print(env_dict)
connection = mariadb.connect(host=env_dict["host"], user=env_dict["user"], password=env_dict["password"], database=env_dict["database"])
print(connection)