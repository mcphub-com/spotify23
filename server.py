import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Glavier/api/spotify23'

mcp = FastMCP('spotify23')

@mcp.tool()
def search(q: Annotated[str, Field(description='Search query')],
           type: Annotated[str, Field(description='multi or one of these: albums artists episodes genres playlists podcasts tracks users')],
           offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           limit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None,
           numberOfTopResults: Annotated[Union[int, float, None], Field(description='Default: 5')] = None,
           gl: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search'''
    url = 'https://spotify23.p.rapidapi.com/search/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'type': type,
        'offset': offset,
        'limit': limit,
        'numberOfTopResults': numberOfTopResults,
        'gl': gl,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def explore() -> dict: 
    '''Explore (Browse All)'''
    url = 'https://spotify23.p.rapidapi.com/browse_all/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_artists(ids: Annotated[str, Field(description='Artist IDs (you can use commas)')]) -> dict: 
    '''Get one or more artists'''
    url = 'https://spotify23.p.rapidapi.com/artists/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_overview(id: Annotated[str, Field(description='Artist ID')]) -> dict: 
    '''Get artist overview'''
    url = 'https://spotify23.p.rapidapi.com/artist_overview/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_discography_overview(id: Annotated[str, Field(description='Artist ID')]) -> dict: 
    '''Get artist discography overview'''
    url = 'https://spotify23.p.rapidapi.com/artist_discography_overview/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_albums(id: Annotated[str, Field(description='Artist ID')],
                  offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                  limit: Annotated[Union[int, float, None], Field(description='Default: 100')] = None) -> dict: 
    '''Get artist albums'''
    url = 'https://spotify23.p.rapidapi.com/artist_albums/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_singles(id: Annotated[str, Field(description='Artist ID')],
                   offset: Annotated[Union[str, None], Field(description='')] = None,
                   limit: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get artist singles'''
    url = 'https://spotify23.p.rapidapi.com/artist_singles/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_appears_on(id: Annotated[str, Field(description='Artist ID')]) -> dict: 
    '''Get artist appears on albums (max 50)'''
    url = 'https://spotify23.p.rapidapi.com/artist_appears_on/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_discovered_on(id: Annotated[str, Field(description='Artist ID')]) -> dict: 
    '''Artist discovered on playlists (max 50)'''
    url = 'https://spotify23.p.rapidapi.com/artist_discovered_on/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_featuring(id: Annotated[str, Field(description='Artist ID')]) -> dict: 
    '''Artist featuring'''
    url = 'https://spotify23.p.rapidapi.com/artist_featuring/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artist_related(id: Annotated[str, Field(description='Artist ID')]) -> dict: 
    '''Artist related'''
    url = 'https://spotify23.p.rapidapi.com/artist_related/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_tracks(ids: Annotated[str, Field(description='Track IDs (you can use commas)')]) -> dict: 
    '''Get one or more tracks'''
    url = 'https://spotify23.p.rapidapi.com/tracks/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def track_credits(id: Annotated[str, Field(description='Track ID')]) -> dict: 
    '''Get track credits'''
    url = 'https://spotify23.p.rapidapi.com/track_credits/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def track_lyrics(id: Annotated[str, Field(description='Track ID')]) -> dict: 
    '''Get track lyrics'''
    url = 'https://spotify23.p.rapidapi.com/track_lyrics/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def track_recommendations(limit: Annotated[Union[int, float, None], Field(description='The target size of the list of recommended tracks. Default: 20. Minimum: 1. Maximum: 100. Default: 20')] = None,
                          seed_tracks: Annotated[Union[str, None], Field(description='A comma separated list of Spotify IDs for a seed track. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres.')] = None,
                          seed_artists: Annotated[Union[str, None], Field(description='A comma separated list of Spotify IDs for seed artists.')] = None,
                          seed_genres: Annotated[Union[str, None], Field(description='A comma separated list of any genres in the set of available genre seeds.')] = None) -> dict: 
    '''Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details. For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.'''
    url = 'https://spotify23.p.rapidapi.com/recommendations/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'seed_tracks': seed_tracks,
        'seed_artists': seed_artists,
        'seed_genres': seed_genres,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_playlist(id: Annotated[str, Field(description='Playlist ID')]) -> dict: 
    '''Get playlist'''
    url = 'https://spotify23.p.rapidapi.com/playlist/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def playlist_tracks(id: Annotated[str, Field(description='Playlist ID')],
                    offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                    limit: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get playlist tracks'''
    url = 'https://spotify23.p.rapidapi.com/playlist_tracks/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def genre_view(id: Annotated[str, Field(description='Genre ID')],
               content_limit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None,
               limit: Annotated[Union[int, float, None], Field(description='Default: 20')] = None) -> dict: 
    '''Genre View'''
    url = 'https://spotify23.p.rapidapi.com/genre_view/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'content_limit': content_limit,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def podcast_episodes(id: Annotated[str, Field(description='Podcast Show ID')],
                     offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                     limit: Annotated[Union[int, float, None], Field(description='Default: 50')] = None) -> dict: 
    '''Podcast Episodes'''
    url = 'https://spotify23.p.rapidapi.com/podcast_episodes/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_episode(id: Annotated[str, Field(description='Episode ID')]) -> dict: 
    '''Get Episode'''
    url = 'https://spotify23.p.rapidapi.com/episode/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def episode_sound(id: Annotated[str, Field(description='Episode ID')]) -> dict: 
    '''Episode Sound'''
    url = 'https://spotify23.p.rapidapi.com/episode_sound/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_profile(id: Annotated[str, Field(description='User ID')],
                 playlistLimit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None,
                 artistLimit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None) -> dict: 
    '''Get user profile'''
    url = 'https://spotify23.p.rapidapi.com/user_profile/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'playlistLimit': playlistLimit,
        'artistLimit': artistLimit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_followers(id: Annotated[str, Field(description='User ID')]) -> dict: 
    '''Get user followers'''
    url = 'https://spotify23.p.rapidapi.com/user_followers/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_radio_playlist(uri: Annotated[str, Field(description='Artist or song URI')]) -> dict: 
    '''Get artist or song radio'''
    url = 'https://spotify23.p.rapidapi.com/seed_to_playlist/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'uri': uri,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def concerts(gl: Annotated[str, Field(description='')]) -> dict: 
    '''Concerts'''
    url = 'https://spotify23.p.rapidapi.com/concerts/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'gl': gl,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_concert(id: Annotated[str, Field(description='Concert ID')]) -> dict: 
    '''Get Concert'''
    url = 'https://spotify23.p.rapidapi.com/concert/'
    headers = {'x-rapidapi-host': 'spotify23.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
