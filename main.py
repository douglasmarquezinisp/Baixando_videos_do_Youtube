from pytube import YouTube

def download_video(url):
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()

# Substitua 'URL_DO_VIDEO' pela URL do vídeo que você deseja baixar
download_video('URL do video')


print("Download concluído com sucesso !!")