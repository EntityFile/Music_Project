from urllib.parse import quote, urlsplit, urlunsplit
from adt_playlist import PlayList
from adt_blacklist import BlackList
from data_module import Song, Itunes, YouTube


def input_track_name():
    name = input('Type track name title: ').split()
    name = ' '.join(name)
    return name


def iri_converter(text):
    parts = urlsplit(text)
    url_code = urlunsplit((
        parts.scheme,
        parts.netloc.encode('idna').decode('ascii'),
        quote(parts.path),
        quote(parts.query, '='),
        quote(parts.fragment),
    ))
    return url_code


def create_search_list(name, blacklist):
    itunes_info = Itunes(name)
    title_list = []
    songs = itunes_info.return_songs()
    songs_list = []
    for i in range(itunes_info.ids):
        if songs[i]['wrapperType'] == 'track':
            song = Song()
            song.get_data(songs, i)
            try:
                ind = song.artist.index('&')
                song.artist = song.artist[:ind] + song.artist[ind + 1:]
            except ValueError:
                pass
            try:
                ind = song.genre.index('&')
                song.genre = song.genre[:ind] + song.genre[ind + 1:]
            except ValueError:
                pass

            if not (song.artist, song.track_name) in title_list:
                if song not in blacklist:
                    if not blacklist.contains_artist(song.artist):
                        if not blacklist.contains_genre(song.genre):
                            title_list.append((song.artist, song.track_name))
                            songs_list.append(song)
    return songs_list


def track_information(song, youtube_info):
    print('''
Artist: {}
Track name: {}
Genre: {}
YouTube video title: {}
YouTube video URL: {}
    '''.format(song.artist, song.track_name, song.genre, youtube_info.title, youtube_info.url))


def show_search_results(blacklist):
    name = input_track_name()
    name = iri_converter(name)
    songs_list = create_search_list(name, blacklist)
    for track_num in range(len(songs_list)):
        print(track_num + 1, songs_list[track_num])
    return songs_list


def find_by_playlist(songs_list, playlist, blacklist):
    if not playlist.length() == 0:
        genres_list = []
        best_genre = (None, 0)
        try:
            for song in playlist:
                genres_list.append(song.genre)
        except AssertionError:
            pass
        for genre in genres_list:
            num = genres_list.count(genre)
            if num > best_genre[1]:
                best_genre = (genre, num)
        # print(best_genre[0])
        new_songs_list = create_search_list(best_genre[0], blacklist)
        for track_num in range(len(new_songs_list)):
            print(track_num + 1, new_songs_list[track_num])
        if not new_songs_list:
            new_songs_list = songs_list
        # print(best_genre[0])
        return new_songs_list
    else:
        return songs_list


def maiin():
    playlist = PlayList()
    blacklist = BlackList()

    songs_list = show_search_results(blacklist)

    while True:
        print()
        print('''
Commands:

playlist - Shows your playlist
blacklist - Shows your blacklist
track {track number} - Shows information about track(Input example: track 3)
search - Shows search menu
find - Shows potentially interesting songs by playlist 
exit - Stop the program
        ''')
        answer = input('>>> ')
        if answer == 'playlist':
            while True:
                print(playlist)
                print('''
Commands:

back - Back to the main menu
clear - Clears the playlist
remove {track number} - Removes this track from the playlist(Input example: remove 3)
return - Changes you playlist to the previous status
                    ''')
                answer = input('>>> ')
                if answer == 'clear':
                    playlist.clear()
                elif len(answer) >= 8:
                    if answer[:7] == 'remove ':
                        try:
                            playlist.remove(int(answer[7:]) - 1)
                        except AssertionError:
                            print('Wrong track.')
                elif answer == 'return':
                    playlist.pull_back()
                elif answer == 'back':
                    break
                else:
                    print('Wrong command.')
        elif answer == 'blacklist':
            while True:
                print(blacklist)
                print('''
Commands:

back - Back to the main menu
clear - Clears the blacklist
remove song {track number} - Removes this song from the blacklist(Input example: remove song 3)
remove genre {genre number} - Removes this genre from the blacklist(Input example: remove genre 3)
remove artist {artist number} - Removes this artist from the blacklist(Input example: remove artist 3)
                    ''')
                answer = input('>>> ')
                if answer == 'clear':
                    playlist.clear()
                elif len(answer) >= 12:
                    if answer[:12] == 'remove song ':
                        try:
                            blacklist.remove_song(int(answer[12:]) - 1)
                        except AssertionError:
                            print('Wrong track.')
                    if answer[:13] == 'remove genre ':
                        try:
                            blacklist.remove_genre(int(answer[13:]) - 1)
                        except AssertionError:
                            print('Wrong genre.')
                    if answer[:14] == 'remove artist ':
                        try:
                            blacklist.remove_artist(int(answer[14:]) - 1)
                        except AssertionError:
                            print('Wrong artist.')
                elif answer == 'back':
                    break
                else:
                    print('Wrong command.')
        elif len(answer) >= 7:
            if answer[:6] == 'track ':
                try:
                    song = songs_list[int(answer[6:]) - 1]
                    youtube_info = YouTube(song.artist, song.track_name)
                    youtube_info.get_info()
                    track_information(song, youtube_info)
                    while True:
                        print('''
Commands:

back - Back to the main menu
add to playlist - Add this song to the playlist
add to blacklist - Add this song to the blacklist
add genre to blacklist - Add the genre of this song to the blacklist
add artist to blacklist - Add the artist to the blacklist
lyrics - Get the lyrics
find by genre - Shows potentially interesting songs by genre
find by artist - Shows potentially interesting songs by artist 
                    ''')
                        answer = input('>>> ')
                        if answer == 'add to playlist':
                            playlist.add(song)
                            print('Added!')
                        elif answer == 'add to blacklist':
                            blacklist.add_song(song)
                            print('Added!')
                        elif answer == 'add genre to blacklist':
                            blacklist.add_genre(song.genre)
                            print('Added!')
                        elif answer == 'add artist to blacklist':
                            blacklist.add_artist(song.artist)
                            print('Added!')
                        elif answer == 'lyrics':
                            if not song.lyrics:
                                song.get_lyrics()
                            print('''
Lyrics:\n{}
                            '''.format(song.lyrics))
                        elif answer == 'find by genre':
                            songs_list = create_search_list(song.genre, blacklist)
                            for track_num in range(len(songs_list)):
                                print(track_num + 1, songs_list[track_num])
                            break
                        elif answer == 'find by artist':
                            songs_list = create_search_list(song.artist, blacklist)
                            for track_num in range(len(songs_list)):
                                print(track_num + 1, songs_list[track_num])
                            break
                        elif answer == 'back':
                            break
                        else:
                            print('Wrong command.')
                except IndexError:
                    print('Wrong track.')
        elif answer == 'search':
            songs_list = show_search_results(blacklist)
        elif answer == 'find':
            songs_list = find_by_playlist(songs_list, playlist, blacklist)
        elif answer == 'exit':
            break
        else:
            print('Wrong command')


if __name__ == '__main__':
    maiin()
