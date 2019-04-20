from adt import PlayList, Song


playlist = PlayList()

# Setting up
song1 = Song()
song2 = Song()
song3 = Song()
song4 = Song()

song1.track_id = 123
song1.artist = 'Adele'
song1.track_name = 'Hello'

song2.track_id = 124
song2.artist = 'Aerosmith'
song2.track_name = 'Dream on'

song3.track_id = 125
song3.artist = 'Led Zeppelin'
song3.track_name = 'Immigrant song'

song4.track_id = 126
song4.artist = 'OneRepublic'
song4.track_name = 'Love Runs Out'

# Printing current status.
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print()

# Adding song1 to the playlist.
playlist.add(song1)
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print()

# Adding song2 to the playlist.
playlist.add(song2)
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print()

# Trying to add song1 to the playlist.
playlist.add(song1)
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print()

# Clearing the playlist.
playlist.clear()
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print()

# Pulling back to the previous version.
playlist.pull_back()
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print()

# Changing first song into song3.
playlist[0] = song3
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print()

# Deleting and printing first song of the playlist.
deleted_song = playlist.remove(0)
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print(deleted_song)
print()

# Adding all the songs into the playlist.
playlist.add(song1)
playlist.add(song3)
playlist.add(song4)
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print()

# Changing first and last songs in places.
playlist.change_position(0, 3)
print('Clipboard:', playlist.print_clipboard())
print('Playlist:', playlist)
print()

# Creating new playlist with same songs.
playlist2 = PlayList()
playlist2.add(song4)
playlist2.add(song1)
playlist2.add(song3)
playlist2.add(song2)
print(playlist)
print(playlist2)
print(playlist == playlist2)
print()

# Changing second playlist.
playlist2.change_position(0, 1)
print(playlist)
print(playlist2)
print(playlist == playlist2)
print()
