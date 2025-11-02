import os
from pathlib import Path #gak usah di download modulenya, kecuali kalo gak punya python

DIRECTORIES = { #kayak ada yang kurang tapi apa ya?
    "HTML": [".html5", ".html", ".htm", ".xhtml", ".xml", ".css", ".js"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd", ".xcf", ".webp"],
    "VIDEOS": [".avi", ".mov", ".mp4", ".mpeg", ".m2v"],
    "AUDIOS": [".mp3", ".wav", ".ogg", ".aac", ".flac", ".pcm", ".aup3", ".midi", ".mid", ".chart"],
    "DOCX": [".docx", ".doc", ".odt", ".pdf", ".rtf", ".wpd"],
    "EXCEL": [".xlsx", ".xls"],
    "PPT": [".ppt", ".pptx", ".pptm", ".potx"],
    "GOLANG": [".go", ".mod"],
    "PYTHON": [".py", ".md"],
    "C": [".cpp", ".c", ".cs"],
    "ARCHIVES": [".zip", ".tar", "gz", ".7z", ".rar", ".iso"],
    "EXECUTION": [".exe", ".bat", ".dll", ".scr"],
    "3D": [".obj", ".fbx", ".stl", ".glb", ".blend", ".skp", ".stl", ".rbz", ".dwg", ".f3d", ".iam", ".ipt"], #capek gua nyari-nyari informasi -_-
    "INSTALLER": [".msi", ".dmg", ".app", ".deb", ".apk", ".ipa", "sis", ".sisx", ".jar", ".jad", ".rpm", ".yum", ".dnf", ".sh"], #untuk pengguna linux juga bisa!
    "MILO": [".milo_ps2"],
    "DTB": [".dtb"],
    "ICON": [".ico"],
    "MANGA": [".cbz", ".cbr", ".cbt", ".mga", ".wmga"],
    "DOWNLOAD UNCOMPLETED": [".crdownload"],
    "TEXT": [".text", ".txt", ".log"]
}

FILE_FORMATS = {ext: category 
                for category, extensions in DIRECTORIES.items() 
                for ext in extensions}

SYSTEM_FILES = ["pagefile.sys", "hiberfil.sys", "swapfile.sys"]
SYSTEM_DIRS = ["System Volume Information", "$RECYCLE.BIN", "Windows"]

def organize():
    for entry in os.scandir('.'):
        if entry.is_dir():
            if entry.name in SYSTEM_DIRS:
                continue
            else:
                continue

        f_path = Path(entry)
        file_format = f_path.suffix.lower()

        if f_path.name in SYSTEM_FILES or not file_format:
            continue

        if file_format in FILE_FORMATS:
            dir_path = Path(FILE_FORMATS[file_format])
            dir_path.mkdir(exist_ok=True)
            f_path.rename(dir_path.joinpath(f_path.name))

            try:
                f_path.rename(dir_path.joinpath(f_path.name))
            except PermissionError:
                print(f"⚠️ Skip Access Being Used: {f_path.name}") #supaya gak error
            except OSError as e:
                print(f"⚠️ Can't Move {f_path.name}: {e}")

if __name__ == '__main__':
    organize()
