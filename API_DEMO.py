import urllib.request
import json


def input_track_author():
	author = input('Type track author title: ').split()
	author = '%20'.join(author)
	return author


def input_track_name():
	name = input('Type track name title: ').split()
	name = '%20'.join(name)
	return name


def DEMO_create_official_name_youtube(author, name):
	content = urllib.request.urlopen('https://www.googleapis.com/youtube/\
v3/search?part=snippet&maxResults=25&q=' + author + '%20' + name + '&key=\
AIzaSyC3kzqz8N9kVTAKLXHUl2ZZTi6aYCwMZM0')
	f = json.load(content)
	#off_name = f['items'][0]['snippet']['title']
	video_title = f['items'][0]['snippet']['title']
	published_time = f['items'][0]['snippet']['publishedAt']
	channel_url = 'https://www.youtube.com/channel/' + f['items'][0]['snippet']['channelId']
	video_url = 'https://www.youtube.com/watch?v=' + f['items'][0]['id']['videoId']
	return([video_title, published_time, channel_url, video_url])


def create_lyrics(author, name):
	try:	
		content=urllib.request.urlopen("https://private-anon-a62af5a409-\
lyricsovh.apiary-proxy.com/v1/" + author + "/" + name)
		f = json.load(content)
		print(f['lyrics'])
	except:
		print('Error, wrong track titles')
	return f['lyrics']


def DEMO_read_itunes_data(author,name):
	content = urllib.request.urlopen('https://itunes.apple.com/search?term=' + author + '%20' + name)
	f = json.load(content)
	genre = f['results'][0]['primaryGenreName']
	track_url = f['results'][0]['trackViewUrl']
	itunes_artist_id = f['results'][0]['artistId']
	itunes_track_id = f['results'][0]['trackId']
	return [genre, track_url, itunes_track_id, itunes_artist_id]


def create_output_json_file(lst):
	f = open('output.json','w',encoding = 'utf-8')
	data_dict = dict()
	for el in lst:
		data_dict[el[0]] = el[1]
	json.dump(data_dict, f)
	f.close()


def main():
	author = input_track_author()
	name = input_track_name()
	youtube_demo_data_list = DEMO_create_official_name_youtube(author, name)
	itunes_demo_data_list = DEMO_read_itunes_data(author,name)
	youtube_title = 'YouTube video tite: ' + youtube_demo_data_list[0]
	youtube_published = 'Video was published at: ' + youtube_demo_data_list[1]
	youtube_channel_url = 'YouTube channel url: ' + youtube_demo_data_list[2]
	youtube_video_url = 'YouTube video url: ' + youtube_demo_data_list[3]
	iTunes_genre = 'Track genre due to itunes data base: ' + itunes_demo_data_list[0]
	iTunes_track_url = 'iTunes track url: ' + itunes_demo_data_list[1]
	iTunes_track_id = 'iTunes track id: ' + str(itunes_demo_data_list[2])
	iTunes_artist_id = 'iTunes artist id: ' + str(itunes_demo_data_list[3])
	print(youtube_title)
	print(youtube_published)
	print(youtube_channel_url)
	print(youtube_video_url, end = '\n\n')
	print(iTunes_genre)
	print(iTunes_track_url)
	print(iTunes_track_id)
	print(iTunes_artist_id, end = '\n\n')
	print('Lyrics:', end = '\n\n')
	lyrics = create_lyrics(author, name)
	try:
		create_output_json_file([('youtube_title', youtube_title), ('youtube_published',youtube_published),\
 ('youtube_channel_url', youtube_channel_url), ('youtube_video_url', youtube_video_url),\
 ('iTunes_genre', iTunes_genre), ('iTunes_track_url', iTunes_track_url), ('iTunes_track_id', iTunes_track_id)\
, ('iTunes_artist_id', iTunes_artist_id), ('lyrics', lyrics)])
	except:
		print('JSON file saving error')


main()