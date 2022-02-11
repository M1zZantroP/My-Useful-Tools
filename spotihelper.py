import requests
from time import time


TOKEN = input('Enter your token (https://developer.spotify.com/console/post-playlist-tracks/?playlist_id=&position=&uris=)\n>> ').strip()
ENTRYPOINT = 'https://api.spotify.com/v1/'
HEADERS = {'Authorization': f'Bearer {TOKEN}'}
ARTIST_NAME = input('Enter necessary artist >> ')


class Artist:

    def get_artist_id(self, name: str) -> str:
        params = {'type': 'artist',
                  'q': name}
        query = requests.get(f'{ENTRYPOINT}search', headers=HEADERS, params=params).json()
        # return query
        if query['artists']['items']:
            artist_id = query['artists']['items'][0]['id']
            return artist_id
        else:
            return ''

    def get_artist_albums(self, artist_id: str) -> list:
        query = requests.get(f'{ENTRYPOINT}artists/{artist_id}/albums', headers=HEADERS).json()
        collection = query['items']
        albums_id = [x['id'] for x in collection]
        return albums_id

    def get_songs_collection(self, albums_id: list) -> list:
        songs_collection = []
        for album_id in albums_id:
            query = requests.get(f'{ENTRYPOINT}albums/{album_id}/tracks', headers=HEADERS).json()
            songs_collection.extend([x["id"] for x in query["items"]])
        return songs_collection


class Playlist:

    # def get_exist_playlists(self):
    #     query = requests.get(f'{ENTRYPOINT}me/playlists', headers=HEADERS).json()
    #     playlist_collection = {}
    #     for i in query['items']:
    #         playlist_collection[i['name']] = i['id']
    #     return playlist_collection

    def add_songs(self, songs_list: list):
        playlist_id = input("Enter your urrent playlist >> ")
        try:
            counter = len(songs_list)
            for song_id in songs_list:
                # data = {'uris': f'spotify:track:{song_id}'}
                query = requests.post(f'{ENTRYPOINT}playlists/{playlist_id}/tracks',
                                      headers=HEADERS,
                                      params=f'uris=spotify%3Atrack%3A{song_id}')
                print(f'[{counter}] left ...')
                counter = counter - 1

        except Exception as _ex:
            print('Something wrong!')


if __name__ == '__main__':
    start = time()

    a = Artist()
    artist_id = a.get_artist_id('Asking')
    album_id = a.get_artist_albums(artist_id)
    songs_ids = a.get_songs_collection(album_id)

    b = Playlist()
    b.add_songs(songs_ids)

    print(f'Finished at {round(time()-start, 2)} sec.')
