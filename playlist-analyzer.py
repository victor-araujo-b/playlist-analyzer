import yt_dlp
from rapidfuzz import fuzz

def extrair_playlist(url):
    opcoes = {
        "extract_flat": True,
        "skip_download": True,
        "quiet": True,
        "ignoreerrors": True,
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        dados = ydl.extract_info(url, download=False)

    videos = []

    for video in dados.get("entries", []):
        if video:
            videos.append({
                "titulo": video.get("title", ""),
                "id": video.get("id", ""),
                "url": video.get("url", ""),
            })

    return videos


def comparar_titulos(videos, limite=85):
    resultados = []

    for i in range(len(videos)):
        for j in range(i + 1, len(videos)):
            titulo_a = videos[i]["titulo"]
            titulo_b = videos[j]["titulo"]

            pontuacao = fuzz.ratio(titulo_a, titulo_b)

            if pontuacao >= limite:
                resultados.append({
                    "Título A": titulo_a,
                    "Título B": titulo_b,
                    "Similaidade": pontuacao
                })

    return resultados


url = input("\nURL da Playlist: ")
videos = extrair_playlist(url)
resultados = comparar_titulos(videos)

for resultado in resultados:
    print(resultado)

