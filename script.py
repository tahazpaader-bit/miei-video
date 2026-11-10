from moviepy.editor import ColorClip, TextClip, CompositeVideoClip

# 1. Crea uno sfondo nero verticale (formato Shorts/Reels 1080x1920) della durata di 5 secondi
sfondo = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=5)

# 2. Aggiunge una scritta al centro del video
testo = TextClip("Il mio video con il codice!", fontsize=70, color='white', size=(900, None)).set_duration(5)

# 3. Unisce lo sfondo e la scritta insieme
video = CompositeVideoClip([sfondo, testo.set_position('center')])

# 4. Salva il risultato finale in un file MP4
video.write_videofile("video_finale.mp4", fps=30)

