import math
import os
import requests
from requests.auth import HTTPBasicAuth
import shutil

from tqdm import tqdm

import version


def update():
    # check version number
    current_version = version.v

    # check latest release version
    auth = HTTPBasicAuth("byte-le-royale-slave", "TheRockIsAStoner")
    payload = requests.get("https://api.github.com/repos/PixPanz/byte_le_royale_2020/releases/latest", auth=auth)

    if payload.status_code == 200:
        json = payload.json()
        remote_version = json["tag_name"]
        asset_id = json["assets"][0]["id"]
    else:
        print("There was an issue attempting to update: Bad Request: \"{0}\"".format(payload.body))
        exit()

    try:
        remote_version = remote_version
    except:
        print("There was an issue attempting to update: Invalid remote version: \"{0}\"".format(remote_version))
        exit()

    temp_current = current_version.split('.')
    temp_remote = remote_version.split('.')
    for curv, remv in zip(temp_current, temp_remote):
        curv = int(curv.replace('v', ''))
        remv = int(remv.replace('v', ''))

        if remv > curv:
            break
    else:
        print('You are already up to date!')
        exit()

    print("There is a new version available: v{0}. Downloading update!".format(remote_version))

    if not os.path.exists("br_updates"):
        os.makedirs("br_updates")

    remote_url = "https://api.github.com/repos/PixPanz/byte_le_royale_2020/releases/assets/{0}".format(asset_id)
    local_file = "br_updates/v{0}.pyz".format(remote_version)

    if not download_file(local_file, remote_url, auth):
        print("Update failed, please try again later.")
        exit()

    old_file = "launcher.pyz"
    print("Replacing {0} with updated launcher.".format(old_file))
    shutil.copyfile(local_file, old_file)
    shutil.rmtree('br_updates')

    print("Update complete!")


def download_file(local_filename, url, auth):
    r = requests.get(url, auth=auth, stream=True, headers={
        "Accept": "application/octet-stream"
    })

    if r.status_code not in [200, 302]:
        return False

    total_size = int(r.headers.get('content-length', 0));
    block_size = 1024
    wrote = 0
    with open(local_filename, 'wb') as f:
        for data in tqdm(r.iter_content(block_size), total=math.ceil(total_size // block_size), unit='KB',
                         unit_scale=True):
            wrote = wrote + len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        print("ERROR, something went wrong")

    return True
