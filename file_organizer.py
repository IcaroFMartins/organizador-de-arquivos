import shutil
from pathlib import Path


CATEGORIAS = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "documentos": [".pdf", ".doc", ".docx", ".txt", ".md", ".csv", ".xlsx"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "audios": [".mp3", ".wav", ".ogg", ".flac"],
    "compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "codigos": [".py", ".js", ".html", ".css", ".json", ".sh"],
}


def obter_categoria(extensao):
    extensao = extensao.lower()

    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria

    return "outros"


def organizar_pasta(caminho_pasta):
    pasta = Path(caminho_pasta)

    if not pasta.is_dir():
        raise FileNotFoundError(f"A pasta não existe: {caminho_pasta}")

    movidos = []

    for item in pasta.iterdir():
        if not item.is_file():
            continue

        if item.name in (".gitignore", "README.md"):
            continue

        categoria = obter_categoria(item.suffix)
        pasta_destino = pasta / categoria
        pasta_destino.mkdir(exist_ok=True)

        destino = pasta_destino / item.name
        shutil.move(item, destino)

        movidos.append({
            "arquivo": item.name,
            "categoria": categoria,
            "destino": destino,
        })

    return movidos