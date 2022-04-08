from pytube import YouTube
from os import startfile
import time, subprocess, sys, re

# ping youtube.com and find the loos percentage
print("Checking your connection to 'youtube.com' ")
ping_st = subprocess.getoutput(['ping', 'youtube.com']) #ping youtube
loss_percent = float(re.findall(r'\d+% loss', ping_st, flags=re.IGNORECASE)[0].split('%')[0])   #fing the loss percentage
if loss_percent > 30.0:
    input("Sorry, your connection have problem. Check your Internet and try again")
    sys.exit()
    

url = input('\nOk, now enter the Url:')  # YouTube Url
for i in range(3):
    try:
        print(f'Try to find Video ({i+1} of 3)')
        video = YouTube(url)
        print('\n\nTitle:\t', video.title)  # video title
        break
    except:
        if i == 2:
            input('Poor connection, check your Internet and try again later...')
            sys.exit()
        print('Poor connection..wait for try again')
        time.sleep(5)

# get available streams
for i in range(3):
    try:
        print(f"Try to find available stream ({i+1} of 3)")
        streams_video = video.streams  
        break
    except:
        if i == 2:
            input("Can't find any streams, or Poor connection...")
            sys.exit()
        print('wait for try again...')
        time.sleep(5)

# try to show all mp4 streams
try:
    for mp4_stream in streams_video.filter(progressive=True):
        print('\ntag:', mp4_stream.itag, '--type:', mp4_stream.type, '--resolution:',
            mp4_stream.resolution)
except:
    print("Sorry, There isn't any -mp4- stream..")

# show all audio streams
try:
    for audio_stream in streams_video.filter(only_audio=True):
        print('\ntag:', audio_stream.itag, '--type:', audio_stream.type, '--Quality:',
            audio_stream.abr)
except:
    print("Sorry, There isn't any -Video- stream..")

# select the tag for download
while True:
    try:
        itag = int(input('\n\nEnter tag:'))  # select the itag for download
        selected_stream = video.streams.get_by_itag(itag)
        break
    except:
        print('\n\nwrong tag !')

print('\nwait for download', selected_stream.type,'-', selected_stream.resolution, '...')   # print the selected stream's info

try:
    selected_stream.download()  # download the stream
    print('done!')
except:
    print('\nconnection lost for downloading the selected stream :(')

try:
    startfile(f'{video.title}.mp4')
except:
    pass
input('Have a good day... :)\n\ndeveloped by ==Unes==')