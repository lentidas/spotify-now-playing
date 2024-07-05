import requests
from os import getenv
from random import randrange


def get_token():
    """Get a new access token"""
    r = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": getenv("REFRESH_TOKEN"),
            "client_id": getenv("CLIENT_ID"),
            "client_secret": getenv("CLIENT_SECRET"),
        },
    )
    try:
        return r.json()["access_token"]
    except BaseException:
        raise Exception(r.json())


def spotify_request(endpoint):
    """Make a request to the specified endpoint"""
    r = requests.get(
        f"https://api.spotify.com/v1/{endpoint}",
        headers={"Authorization": f"Bearer {get_token()}"},
    )
    return {} if r.status_code == 204 else r.json()


def main():
    data = spotify_request("me/player/currently-playing")
    if data:
        item = data["item"]
    else:
        n = randrange(10)
        print(spotify_request("me/player/recently-played?limit=10")["items"][n]["track"])
        print("/n")
        print("/n")
        n = randrange(50)
        print(spotify_request("me/top/tracks?limit=50&time_range=medium_term")["items"][n])

if __name__ == "__main__":
    main()
