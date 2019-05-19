from flask import Flask, render_template, request, redirect, url_for, session
from data_module import Song, YouTube
from adt_playlist import PlayList
from adt_blacklist import BlackList
from test_module import create_search_list, find_by_playlist

app = Flask(__name__)

global playlist, blacklist

play_list = PlayList()
black_list = BlackList()

songs = dict()


@app.route("/")
def index():
    """
    Creates starting page
    :return: index.html
    """
    return render_template("index.html")


@app.route("/playlist")
def playlist():
    """
    Shows playlist page
    :return: playlist.html
    """
    return render_template("playlist.html", name=play_list)


@app.route("/blacklist")
def blacklist():
    """
    Shows blacklist page
    :return: blacklist.html
    """
    return render_template("blacklist.html", name=black_list)


@app.route("/playlist_remove", methods=['GET'])
def remove_playlist():
    """
    Removes song from the playlist
    :return: playlist.html
    """
    song_id = int(request.args ["song"])
    for i in range(play_list.length()):
        if play_list._data [i].track_id == song_id:
            play_list.remove(i)
            return render_template("playlist.html", name=play_list)


@app.route("/blacklist_remove_song", methods=['GET'])
def remove_blacklist_song():
    """
    Removes song from the blacklist
    :return: blacklist.html
    """
    song_id = int(request.args ["song"])
    for i in range(black_list.songs_length()):
        if black_list._songs_data [i].track_id == song_id:
            black_list.remove_song(i)
            return render_template("blacklist.html", name=black_list)


@app.route("/blacklist_remove_genre", methods=['GET'])
def remove_blacklist_genre():
    """
    Removes genre from the blacklist
    :return: blacklist.html
    """
    genre = request.args ["song"]
    for i in range(black_list.genres_length()):
        if genre == black_list._genres_data [i]:
            black_list.remove_genre(i)
            return render_template("blacklist.html", name=black_list)


@app.route("/playlist_clear", methods=['POST'])
def playlist_clear():
    """
    Clears the playlist.
    :return: playlist.html
    """
    play_list.clear()
    return render_template("playlist.html", name=play_list)


@app.route("/blacklist_remove_artist", methods=['GET'])
def remove_blacklist_artist():
    """
    Removes artist from the blacklist
    :return: blacklist.html
    """
    artist = request.args ["song"]
    for i in range(black_list.artists_length()):
        if artist == black_list._artist_data [i]:
            black_list.remove_artist(i)
            return render_template("blacklist.html", name=black_list)


@app.route("/blacklist_add")
def add_blacklist():
    """
    Adds song to the blacklist.
    :return: track.html
    """
    name = songs [request.args ["song"]]
    black_list.add_song(name)
    video = YouTube(name.iri_artist, name.iri_track_name)
    video.get_info()
    return render_template("track.html", name=name, video=video)


@app.route("/blacklist_add_genre")
def add_blacklist_genre():
    """
    Adds genre to the blacklist.
    :return: track.html
    """
    name = songs [request.args ["song"]]
    black_list.add_genre(name.genre)
    video = YouTube(name.iri_artist, name.iri_track_name)
    video.get_info()
    return render_template("track.html", name=name, video=video)


@app.route("/blacklist_add_artist")
def add_blacklist_artist():
    """
    Adds artist to the blacklist.
    :return: track.html
    """
    name = songs [request.args ["song"]]
    black_list.add_artist(name.artist)
    video = YouTube(name.iri_artist, name.iri_track_name)
    video.get_info()
    return render_template("track.html", name=name, video=video)


@app.route("/playlist_add")
def add_playlist():
    """
    Adds song to the playlist.
    :return: track.html
    """
    name = songs [request.args ["song"]]
    play_list.add(name)
    video = YouTube(name.iri_artist, name.iri_track_name)
    video.get_info()
    return render_template("track.html", name=name, video=video)


@app.route("/playlist_add_static", methods=['GET'])
def add_playlist_static():
    """
    Adds song to the playlist.
    :return: success.html
    """
    name = songs [request.args ["song"]]
    play_list.add(name)
    return render_template("success.html", name=[songs [i] for i in songs])


@app.route("/blacklist_add_static", methods=['GET'])
def add_blacklist_static():
    """
    Adds song to the blacklist.
    :return: success.html
    """
    name = songs [request.args ["song"]]
    black_list.add_song(name)
    return render_template("success.html", name=[songs [i] for i in songs])


@app.route("/blacklist_add_genre_static")
def add_blacklist_genre_static():
    """
    Adds genre to the blacklist.
    :return: success.html
    """
    name = songs [request.args ["song"]]
    black_list.add_genre(name.genre)
    return render_template("success.html", name=[songs [i] for i in songs])


@app.route("/blacklist_add_artist_static")
def add_blacklist_artist_static():
    """
    Adds artist to the blacklist.
    :return: success.html
    """
    name = songs [request.args ["song"]]
    black_list.add_artist(name.artist)
    return render_template("success.html", name=[songs [i] for i in songs])


@app.route("/track")
def show_track_info(name):
    """
    Shows track info.
    :param name: track full name
    :return:
    """
    name = songs [name]
    # name.get_lyrics()
    # name.lyrics = name.lyrics.split('\n')
    video = YouTube(name.iri_artist, name.iri_track_name)
    video.get_info()
    return render_template("track.html", name=name, video=video)


@app.route("/get_info")
def get_info():
    """
    Gets track full name.
    :return: show_track_info(name)
    """
    name = request.args ["song"]
    return show_track_info(name)


@app.route("/get_pl_info")
def get_pl_info():
    song_id = int(request.args["song"])
    for i in range(play_list.length()):
        if play_list._data[i].track_id == song_id:
            name = play_list._data[i]
            video = YouTube(name.iri_artist, name.iri_track_name)
            video.get_info()
            return render_template("track.html", name=name, video=video)


@app.route("/get_bl_info")
def get_bl_info():
    song_id = int(request.args["song"])
    for i in range(black_list.songs_length()):
        if black_list._songs_data[i].track_id == song_id:
            name = black_list._songs_data[i]
            video = YouTube(name.iri_artist, name.iri_track_name)
            video.get_info()
            return render_template("track.html", name=name, video=video)


@app.route("/register", methods=["POST"])
def register():
    """
    Makes first search.
    :return: success.html
    """
    global songs
    name = request.form.get("domain")
    if not name:
        return index()
    answer = create_search_list(name, black_list)
    songs = {str(song): song for song in answer}
    return render_template("success.html", name=answer)


@app.route("/search")
def search():
    """
    Shows songs list.
    :return: success.html or index.html
    """
    if songs:
        return render_template('success.html', name=[songs [i] for i in songs])
    else:
        return render_template('index.html')


@app.route("/find_by_playlist", methods=['POST'])
def find_by_pl():
    """
    Creates songs list by the playlist.
    :return: success.html
    """
    global songs
    songs_list = find_by_playlist([songs [i] for i in songs], play_list, black_list)
    songs = {str(song): song for song in songs_list}
    return render_template('success.html', name=[songs [i] for i in songs])


@app.route("/find_by_genre", methods=['GET'])
def find_by_genre():
    """
    Creates songs list by song's genre
    :return: success.html
    """
    global songs
    song = songs [request.args ["song"]]
    songs_list = create_search_list(song.genre, black_list)
    songs = {str(song): song for song in songs_list}
    return render_template('success.html', name=[songs [i] for i in songs])


@app.route("/find_by_artist", methods=['GET'])
def find_by_artist():
    """
    Creates songs list by song's artist
    :return: success.html
    """
    global songs
    song = songs [request.args ["song"]]
    songs_list = create_search_list(song.artist, black_list)
    songs = {str(song): song for song in songs_list}
    return render_template('success.html', name=[songs [i] for i in songs])


@app.route("/lyrics")
def lyrics():
    """
    Creates lyrics
    :return: lyrics.html
    """
    song = songs [request.args ["song"]]
    song.get_lyrics()
    song.lyrics = song.lyrics.split('\n')
    return render_template('lyrics.html', name=song)


if __name__ == "__main__":
    app.run()
