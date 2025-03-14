import os
from pytubefix import YouTube, Playlist

def download_video(url, resolution="1080p"):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution, file_extension="mp4").first()
        
        if video:
            video.download()
            print(f'Sucesso: {yt.title} baixado em {resolution}')
        else:
            print(f"Nenhum vídeo encontrado em {resolution}. Baixando na maior resolução disponível.")
            yt.streams.get_highest_resolution().download()
    
    except Exception as e:
        print(f"Erro ao baixar {url}: {str(e)}")

def download_playlist(playlist_url, resolution="1080p"):
    try:
        playlist = Playlist(playlist_url)
        print(f"Baixando playlist: {playlist.title}")
        for video_url in playlist.video_urls:
            download_video(video_url, resolution)
    except Exception as e:
        print(f"Erro ao baixar a playlist: {str(e)}")

if __name__ == "__main__":
    url = input("Digite o URL do vídeo ou da playlist do YouTube: ")
    if 'playlist' in url:
        download_playlist(url)
    else:
        download_video(url)
