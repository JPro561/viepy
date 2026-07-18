import viepy as vie

# Configuring
fm = vie.text.FontManager()

# Args
scene = vie.Scene(
    width=1280,
    height=720,
    fps=60,
    anti_aliasing=True,
    objects=[],
    audio_channels=[],
    final_delay=0.2,
    duration=10,
    font_manager=fm
)

# Objects
circle = vie.objects.Circle(vie.objects.Transform(0, 0, 0, (1, 1)))

scene.add(circle)
scene.remove(circle)
scene.clear()

# Audio
audio = vie.audio.Audio()

scene.create_channel(1)
scene.add_audio_to_channel(audio, 1)

# Render to video
vie.render(scene, False)
