from data_module import Song


class BlackList:
    def __init__(self):
        """
        Creates empty playlist.

        """
        self._artist_data = []
        self._songs_data = []
        self._genres_data = []

    def songs_length(self):
        """
        Returns the songs quantity in blacklist.

        :return: Returns the songs quantity in blacklist.
        """
        return len(self._songs_data)
    
    def genres_length(self):
        """
        Returns the genres quantity in blacklist.

        :return: Returns the genres quantity in blacklist.
        """
        return len(self._genres_data)
    
    def artists_length(self):
        """
        Returns the artists quantity in blacklist.

        :return: Returns the atrists quantity in blacklist.
        """
        return len(self._artist_data)

    def clear(self):
        """
        Clears the playlist. Updates the clipboard. Returns data from the clipboard.

        :return: Returns data from the clipboard
        """
        self._songs_data = []
        self._artist_data = []
        self._genres_data = []

    def __setitem__(self, index, song):
        """
        Sets the song into new position.

        :param index: position.
        :param song: song that have to be placed.
        """
        assert index >= 0 and index < self.songs_length(), 'Wrong index variable.'
        assert type(song) == Song, 'Wrong item type.'
        self._songs_data[index] = song
    
    def set_genre(self, index, genre):
        """
        Sets the genre into new position.

        :param index: position.
        :param genre: genre that have to be placed.
        """
        assert index >= 0 and index < self.genres_length(), 'Wrong index variable.'
        self._genres_data[index] = genre
        
    def set_artist(self, index, artist):
        """
        Sets the atist into new position.

        :param index: position.
        :param artist: artist that have to be placed.
        """
        assert index >= 0 and index < self.artists_length(), 'Wrong index variable.'
        self._artist_data[index] = artist

    def __getitem__(self, index):
        """
        Returns the contents of the element at position [index]

        :param index: position.
        :return: Returns item on that position
        """
        assert index >= 0 and index < self.songs_length(), 'Wrong index variable.'
        return self._songs_data[index]
    
    def get_genre(self, index):
        """
        Returns the contents of the element at position [index]

        :param index: position.
        :return: Returns item on that position
        """
        assert index >= 0 and index < self.genres_length(), 'Wrong index variable.'
        return self._genres_data[index]
    
    def get_artist(self, index):
        """
        Returns the contents of the element at position [index]

        :param index: position.
        :return: Returns item on that position
        """
        assert index >= 0 and index < self.artists_length(), 'Wrong index variable.'
        return self._artist_data[index]

    def __contains__(self, song):
        """
        Checks if the song is in the blacklist, song must be Song type.

        :param song: Song type object
        :return: Returns True if song in blacklist and False otherwise
        """
        assert type(song) == Song, 'Wrong item type.'
        for songs in self._songs_data:
            if song == songs:
                return True
        return False
    
    def contains_genre(self, genre):
        """
        Checks if the genre is in the blacklist.

        :param genre: Genre type object
        :return: Returns True if genre in blacklist and False otherwise
        """
        for genres in self._genres_data:
            if genre == genres:
                return True
        return False
    
    def contains_artist(self, artist):
        """
        Checks if the artist is in the blacklist.

        :param artist: Genre type object
        :return: Returns True if genre in blacklist and False otherwise
        """
        for artists in self._artist_data:
            if artist == artists:
                return True
        return False
    
    def add_song(self, song):
        """
        Sets the song into new position.

        :param song: song that have to be placed.
        """
        assert type(song) == Song, 'Wrong item type.'
        if song not in self._songs_data:
            self._songs_data.append(song)
            
    def add_genre(self, genre):
        """
        Sets the genre into new position.

        :param genre: genre that have to be placed.
        """
        if genre not in self._genres_data:
            self._genres_data.append(genre)
            
    def add_artist(self, artist):
        """
        Sets the artist into new position.

        :param artist: genre that have to be placed.
        """
        if artist not in self._artist_data:
            self._artist_data.append(artist)

    def __str__(self):
        songs = ''
        for song_num in range(self.songs_length()):
            songs += str(song_num + 1) + ' ' + self._songs_data[song_num].artist + ' : ' +\
                     self._songs_data[song_num].track_name + '\n'
        genres = ''
        for genre_num in range(self.genres_length()):
            genres += str(genre_num + 1) + ' ' + str(self._genres_data[genre_num]) + '\n'
        artists = ''
        for artist_num in range(self.artists_length()):
            artists += str(artist_num + 1) + ' ' + str(self._artist_data[artist_num]) + '\n'
        return '''
Songs:
{}
Genres:
{}
Artists:
{}
        '''.format(songs, genres, artists)

    def remove_song(self, index):
        """
        Deletes song on the position index.

        :param index: song position
        :return: Returns deleted song
        """
        assert index >= 0 and index < self.songs_length(), 'Wrong index variable.'
        return self._songs_data.pop(index)
    
    def remove_genre(self, index):
        """
        Deletes genre on the position index.

        :param index: genre position
        :return: Returns deleted genre
        """
        assert index >= 0 and index < self.genres_length(), 'Wrong index variable.'
        return self._genres_data.pop(index)
    
    def remove_artist(self, index):
        """
        Deletes artist on the position index.

        :param index: artist position
        :return: Returns deleted artist
        """
        assert index >= 0 and index < self.artists_length(), 'Wrong index variable.'
        return self._artist_data.pop(index)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.songs_length() == other.songs_length():
                if self.genres_length() == other.genres_length():
                    if self.artists_length() == other.artists_length():                
                        for song in self._songs_data:
                            if song not in other._songs_data:
                                return False
                        for genre in self._genres_data:
                            if genre not in other._genres_data:
                                return False
                        for artist in self._artist_data:
                            if artist not in other._artist_data:
                                return False
                        return True
                    return False
                return False
            return False
        else:
            return type(self) == type(other)
