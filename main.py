import requests
import random
import json
import re

REGEX = "https://mega\.nz/((folder|file)/([^#]+)#(.+)|#(F?)!([^!]+)!(.+))"


def mega_checker(url: str) -> bool:
    if not bool(re.search(REGEX, url)):
        return False
        
    link_id = url.split("/")[4].split("#")[0]

    if url.split("/")[3] == "folder":
        payload = {'a': 'f', 'c': 1, 'r': 1, 'ca': 1}
    else:
        payload = {'a': 'g', 'p': link_id}

    sequence_num = random.randint(0, 0xFFFFFFFF)

    response = requests.post(
        f"https://g.api.mega.co.nz/cs?id={sequence_num}&n={link_id}",
        data=json.dumps([payload])
    ).json()

    if not type(response) is int:
        return True
    return False


# print(mega_checker("https://mega.nz/folder/OHQlaAT#y_pYR8b96o14ZKK8NxZRyA"))
