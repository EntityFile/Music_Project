from data_module import Song


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
            self._clipboard.append(self._data[:])

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
        #assert index >= 0 and index < self.length(), 'Wrong index variable.'
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
        print(self._data)
        print(self._clipboard)
        if len(self._clipboard) == 0:
            self._data = self._clipboard[:]
        else:
            self._data = self._clipboard[len(self._clipboard) - 1]
            self._clipboard.pop()

    def __str__(self):
        songs = ''
        for song_num in range(self.length()):
            songs += str(song_num + 1) + ' ' + self._data[song_num].artist + ' : ' +\
                     self._data[song_num].track_name + '\n'
        return '''
Songs:
{}
        '''.format(songs)

    def print_clipboard(self):
        if len(self._clipboard) == 0:
            return str([(song.artist, song.track_name) for song in self._clipboard])
        else:
            return str([(song.artist, song.track_name) for song in self._clipboard[len(self._clipboard) - 1]])

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