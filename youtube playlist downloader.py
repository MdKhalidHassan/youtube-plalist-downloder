import pytube

# Choose the URL of the YouTube playlist you want to download
url = 'https://youtube.com/playlist?list=PLaCUFUZ_YQwVGxKqjXaQcWEeTMIWeEFjX'

# Create a Playlist object with the URL
pl = pytube.Playlist(url)

# Get a list of all the video URLs in the playlist
video_urls = pl.parse_links()

# Download each video in the playlist
for url in video_urls:
    # Create a YouTube object with the video URL
    yt = pytube.YouTube(url)

    # Get the first video stream available
    video_stream = yt.streams.first()

    # Set the output file name
    output_name = yt.title

    # Download the video to the current directory
    video_stream.download(output_name=output_name)
    print(f'Finished downloading {output_name}')

print('All videos in the playlist have been downloaded!')
