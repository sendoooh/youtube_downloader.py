import tkinter as tk
import yt_dlp


def stahni_video():
    url = entry.get().strip()
    if not url.startswith("https://www.youtube.com/watch?v="):
        status_label.config(text="Neplatná YouTube URL")
        return

    status_label.config(text="Stahuji...")
    ydl_opts = {
        'format': 'best',  # stáhne nejlepší dostupné video
        'outtmpl': '%(title)s.%(ext)s'  # uloží video pod názvem videa
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_label.config(text="Staženo!")
    except Exception as e:
        status_label.config(text=f"Chyba: {e}")
#okno GUI

o = tk.Tk()
o.title("YouTube Downloader")
tk.Label(o, text="Vlož odkaz").pack()

entry = tk.Entry(o, width=50)
entry.pack()

tk.Button(o, text="Stáhnout", command=stahni_video).pack()
status_label = tk.Label(o, text="")
status_label.pack()

o.mainloop()
