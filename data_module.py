import json
import urllib.request
from urllib.parse import quote, urlsplit, urlunsplit


class YouTube:
    def __init__(self, artist, track):
        self.artist = artist
        self.track = track
        self.url = None
        self.title = None

    def get_info(self):
        url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=' + '%20'.join(
            self.artist.split()) + '%20' + '%20'.join(self.track.split()) \
              + '&key=AIzaSyC3kzqz8N9kVTAKLXHUl2ZZTi6aYCwMZM0'
        content = urllib.request.urlopen(url)
        f = json.load(content)
        i = 0
        try:
            while f['items'][i]['id']['kind'] != 'youtube#video':
                i += 1
                if i > 25:
                    break
            self.title = f['items'][i]['snippet']['title']
            self.url = 'https://www.youtube.com/embed/' + f['items'][i]['id']['videoId']
        except:
            print('Wrong artist/track name!', f['items'])


class Itunes:
    def __init__(self, inpt):
        self.songs = []
        self.inpt = inpt
        self.ids = 0

    def get_songs(self):
        inpt = iri_conventer(self.inpt)
        content = urllib.request.urlopen('https://itunes.apple.com/search?term=' + inpt)
        f = json.load(content)
        self.songs = f['results']
        self.ids = len(self.songs)

    def return_songs(self):
        self.get_songs()
        return self.songs


class Song:
    def __init__(self):
        self.artist_id = None
        self.track_url = None
        self.genre = None
        self.track_id = None
        self.artist = None
        self.track_name = None
        self.type = None
        self.lyrics = ''
        self.iri_artist = None
        self.iri_track_name = None
        self.icon = None

    def get_data(self, songs, index):
        """
        Receives data from iTunes output.

        :param songs: iTunes output list
        :param index: index of the song in songs list
        """
        self.get_artist_id(songs, index)
        self.get_track_url(songs, index)
        self.get_genre(songs, index)
        self.get_track_id(songs, index)
        self.get_artist_name(songs, index)
        self.get_track_name(songs, index)
        self.get_type(songs, index)
        self.get_icon(songs, index)

    def get_artist_id(self, songs, index):
        try:
            self.artist_id = songs [index] ['artistId']
        except KeyError:
            pass

    def get_track_url(self, songs, index):
        try:
            self.track_url = songs [index] ['trackViewUrl']
        except KeyError:
            pass

    def get_genre(self, songs, index):
        try:
            self.genre = songs [index] ['primaryGenreName']
        except KeyError:
            pass

    def get_track_id(self, songs, index):
        try:
            self.track_id = songs [index] ['trackId']
        except KeyError:
            pass

    def get_artist_name(self, songs, index):
        try:
            self.artist = ' '.join(songs [index] ['artistName'].split( ))
            self.iri_artist = iri_conventer(self.artist)

        except KeyError:
            pass

    def get_track_name(self, songs, index):
        try:
            self.track_name = ' '.join(songs [index] ['trackName'].split( ))
            self.iri_track_name = iri_conventer(self.track_name)
        except KeyError:
            pass

    def get_type(self, songs, index):
        try:
            self.type = songs [index] ['wrapperType']
        except KeyError:
            pass
    
    def get_icon(self, songs, index):
        try:
            self.icon = songs[index]['artworkUrl100']
        except KeyError:
            pass

    def get_lyrics(self):
        artist = iri_conventer(self.artist)
        track_name = iri_conventer(self.track_name)
        print(artist, track_name)
        try:
            url = "https://private-anon-dbc5463fb7-lyricsovh.apiary-proxy.com/v1/" + artist + "/" + track_name
            content = urllib.request.urlopen(url)
            f = json.load(content)
            #for ind in range(len(f)):
            #    try:
            #        if f[ind] == '\n' and f [ind + 1] == '\n':
            #            f[ind + 1] == ''
            #    except:
            #        None
            self.lyrics = f['lyrics']
        except:
            print('No available lyrics.')

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.track_id == self.track_id
        else:
            return type(self) == type(other)

    def __str__(self):
        return self.artist + ' - ' + self.track_name
    

def iri_conventer(text):
    parts = urlsplit(text)
    url_code = urlunsplit((
        parts.scheme,
        parts.netloc.encode('idna').decode('ascii'),
        quote(parts.path),
        quote(parts.query, '='),
        quote(parts.fragment),
    ))
    return url_code


def find_songs(name):
    """
    Creates tracks list by inputed string
    :param name: searching key
    :return: list of songs
    """
    name = iri_conventer(name)
    itunes_info = Itunes(name)
    title_list = []
    songs = itunes_info.return_songs()
    songs_list = []
    for i in range(itunes_info.ids):
        if songs[i]['wrapperType'] == 'track':
            song = Song()
            song.get_data(songs, i)
            if not (song.artist, song.track_name) in title_list:
                title_list.append((song.artist, song.track_name))
                songs_list.append(song)
    return songs_list
