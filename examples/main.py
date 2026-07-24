import viepy as vie

# Configuring
fm = vie.text.FontManager()

# Args
scene = vie.Scene(
    name="vieExample_Scene",
    width=1280,
    height=720,
    fps=30,
    anti_aliasing=True,
    final_delay=0.2,
    font_manager=fm,
)

# Audio
music = vie.audio.Music(path="examples/assets/Viepy.mp3", name="Viepy Theme", auto_play=True, artist="TuneWave")
scene.add_audio_to_channel(music, 0)

# Objects
circle = vie.objects.Circle(vie.objects.Transform(0, -20, 0, (1, 1)))
triangle = vie.objects.Triangle(vie.objects.Transform(0, 20, 0, (1, 1)))
rect = vie.objects.Rectangle(vie.objects.Transform(50, 0, 0, (1, 1)))
text = vie.text.Music_Name(vie.objects.Transform(0, 0, 0, (1, 1)), music=music)

scene.add(circle, triangle, rect, text)
scene.remove(circle)

# Render to video
vie.renderer.render(scene, True)
