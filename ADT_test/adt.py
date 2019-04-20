import urllib.request
from urllib.parse import quote, urlsplit, urlunsplit
import json


def input_track_name():
    name = input('Type track name title: ').split()
    name = ' '.join(name)
    return name


class PlayList:
    def __init__(self):
        """
        Creates empty playlist.

        """
        self._data = []
        self._clipboard = []

    def length(self):
        """
        Returns the length of the playlist.

        :return: Returns the length of the playlist.
        """
        return len(self._data)

    def update_clipboard(self):
        """
        Updates the clipboard.

        """
        if self.length() != 0:
            self._clipboard = self._data[:]

    def clear(self):
        """
        Clears the playlist. Updates the clipboard. Returns data from the clipboard.

        :return: Returns data from the clipboard
        """
        self.update_clipboard()
        self._data = []
        return self._clipboard

    def __setitem__(self, index, song):
        """
        Sets the song into new position.

        :param index: position.
        :param song: song that have to be placed.
        """
        assert index >= 0 and index < self.length(), 'Wrong index variable.'
        assert type(song) == Song, 'Wrong item type.'
        self.update_clipboard()
        self._data[index] = song

    def __getitem__(self, index):
        """
        Returns the contents of the element at position [index]

        :param index: position.
        :return: Returns item on that position
        """
        assert index >= 0 and index < self.length(), 'Wrong index variable.'
        return self._data[index]

    def __contains__(self, song):
        """
        Checks if the song in the playlist, song must be Song type.

        :param song: Song type object
        :return: Returns True if song in playlist and False otherwise
        """
        assert type(song) == Song, 'Wrong item type.'
        for songs in self._data:
            if song == songs:
                return True
        return False

    def add(self, song):
        """
        Sets the song into new position.

        :param song: song that have to be placed.
        """
        assert type(song) == Song, 'Wrong item type.'
        if song not in self._data:
            self.update_clipboard()
            self._data.append(song)

    def pull_back(self):
        """
        Sets playlist to the previous status.

        """
        self._data = self._clipboard[:]

    def __str__(self):
        return str([(song.artist, song.track_name) for song in self._data])

    def print_clipboard(self):
        return str([(song.artist, song.track_name) for song in self._clipboard])

    def remove(self, index):
        """
        Deletes song on the position index.

        :param index: song position
        :return: Returns deleted song
        """
        assert index >= 0 and index < self.length(), 'Wrong index variable.'
        self.update_clipboard()
        return self._data.pop(index)

    def change_position(self, index1, index2):
        """
        Changes two songs in places.

        :param index1: position of the first song
        :param index2: position of the second song
        """
        assert index1 >= 0 and index1 < self.length(), 'Wrong index1 variable.'
        assert index2 >= 0 and index2 < self.length(), 'Wrong index2 variable.'
        assert index1 != index2, "index1 can't be equal to the index2"
        self.update_clipboard()
        song1 = self._data[index1]
        song2 = self._data[index2]
        self._data[index1] = song2
        self._data[index2] = song1

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.length() == other.length():
                for song_index in range(self.length()):
                    if self[song_index] != other[song_index]:
                        return False
                return True
            return False
        else:
            return type(self) == type(other)


def create_lyrics(author, name):
    try:
        url = "https://private-anon-dbc5463fb7-lyricsovh.apiary-proxy.com/v1/" + author + "/" + name
        # print(url)
        content = urllib.request.urlopen(url)
        f = json.load(content)
        for ind in range(len(f)):
            try:
                if f[ind] == '\n' and f[ind + 1] == '\n':
                    f[ind + 1] == ''
            except:
                None
        return f['lyrics']
    except:
        print('Error, wrong track titles')


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
        print(url)
        print(self.artist)
        print(self.track)
        content = urllib.request.urlopen(url)
        f = json.load(content)
        i = 0
        try:
            while f['items'][i]['id']['kind'] != 'youtube#video':
                i += 1
                if i > 25:
                    break
            self.title = f['items'][i]['snippet']['title']
            self.url = 'https://www.youtube.com/watch?v=' + f['items'][i]['id']['videoId']
        except:
            print('Wrong artist/track name!', f['items'])


class Itunes:
    def __init__(self, inpt):
        self.songs = []
        self.inpt = inpt
        self.ids = 0

    def get_songs(self):
        content = urllib.request.urlopen('https://itunes.apple.com/search?term=' + self.inpt)
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
        self.lyrics = None

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

    def get_artist_id(self, songs, index):
        try:
            self.artist_id = songs[index]['artistId']
        except KeyError:
            pass

    def get_track_url(self, songs, index):
        try:
            self.track_url = songs[index]['trackViewUrl']
        except KeyError:
            pass

    def get_genre(self, songs, index):
        try:
            self.genre = songs[index]['primaryGenreName']
        except KeyError:
            pass

    def get_track_id(self, songs, index):
        try:
            self.track_id = songs[index]['trackId']
        except KeyError:
            pass

    def get_artist_name(self, songs, index):
        try:
            self.artist = iri_conventer(' '.join(songs[index]['artistName'].split()))
        except KeyError:
            pass

    def get_track_name(self, songs, index):
        try:
            self.track_name = iri_conventer(' '.join(songs[index]['trackName'].split()))
        except KeyError:
            pass

    def get_type(self, songs, index):
        try:
            self.type = songs[index]['wrapperType']
        except KeyError:
            pass

    def get_lyrics(self):
        self.lyrics = create_lyrics(self.artist, self.track_name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.track_id == self.track_id
        else:
            return type(self) == type(other)

    def __str__(self):
        return self.artist + ' : ' + self.track_name


def maiin():
    name = input_track_name()
    name = iri_conventer(name)
    print(name)
    itunes_info = Itunes(name)
    title_list = []
    songs = itunes_info.return_songs()
    print(songs)
    for i in range(itunes_info.ids):
        if songs[i]['wrapperType'] == 'track':
            song = Song()
            song.get_data(songs, i)
            if not (song.artist, song.track_name) in title_list:
                youtube = YouTube(song.artist, song.track_name)
                #	youtube.get_info()
                #	video = youtube.url
                #	title = youtube.title
                #	print(title)
                #song.get_lyrics()
                print(song.track_name, song.artist, song.track_url, song.track_id)
                print()
                print(song.lyrics)
                #	print(video)
                print()
                title_list.append((song.artist, song.track_name))


def create_output_json_file(lst):
    f = open('output.json', 'w', encoding='utf-8')
    data_dict = dict()
    for el in lst:
        data_dict[el[0]] = el[1]
    json.dump(data_dict, f)
    f.close()


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


if __name__ == '__main__':
    maiin()
