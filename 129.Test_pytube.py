from pytube import YouTube
YouTube(
    'https://youtu.be/9bZkp7q19f0'
).streams.first().download()
