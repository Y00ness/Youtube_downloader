from pytube import YouTube
from os import startfile

url = input('---Url:')  # YouTube Url

try:
    video = YouTube(url)
    print('\n\nTitle:\t', video.title)  # video title
    print('\n\nWait for Availabe streams...:)')
    streams_video = video.streams  # get available streams
except:
    print('connection lost :(')

# show all mp4 streams
for mp4_stream in streams_video.filter(progressive=True):
    print('\ntag:', mp4_stream.itag, '--type:', mp4_stream.type, '--resolution:',
          mp4_stream.resolution)
# show all audio streams
for audio_stream in streams_video.filter(only_audio=True):
    print('\ntag:', audio_stream.itag, '--type:', audio_stream.type, '--Quality:',
          audio_stream.abr)

try:
    itag = int(input('\n\nEnter itag:'))  # select the itag for download
    selected_stream = video.streams.get_by_itag(itag)
except:
    print('\n\nwrong itag !')
print('\nwait for download', selected_stream.type,'-', selected_stream.resolution, '...')

try:
    selected_stream.download()  # download the stream
except:
    print('\nconnection lost :(')

try:
    startfile(f'{video.title}.mp4')     # play the downloaded video
except:
    pass
input('\nHave a good day... :)\nDeveloped by ==Unes==\n[telegram:t.me/unes_h]')