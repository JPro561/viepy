# Creating Your First Video

<p style="margin-top: 1rem;">Now that the Viepy library is finally installed, let's create something with it!</p>

# Summary

In this tutorial, you will learn how to:

* [Create a scene](first_video.md/#scene)
* [Create shapes](first_video.md/#adding-shapes) (circle, triangle, rectangle)
* [Create text](first_video.md/#text) and apply fonts
* [Play music](first_video.md/#adding-music) in your scenes
* [Render your video](first_video.md/#rendering-your-scene)

# Programming

## Scene

The scene is the most important element of your video. It is where objects (shapes, text, music, etc.) and key variables (such as width and height, scene name, fps, duration, etc.) are stored. If you don't set up a scene in your project, it won't work—and you'll find out why later on.
That’s why we’re going to start programming by using it. So, let’s get started!

---

The scene is declared as `Scene()`. Let’s give it a try:

```python title="main.py"
import viepy as vie

MyScene = vie.Scene(
    name="My Project Name",
    width=1280,
    height=720,
    fps=60,
    duration=120,
    anti_aliasing=True,
    final_delay=0.2,
    font_manager=None,
)
```

Let's see what each line means:

```python title="main.py"
MyScene = Scene()
```

This line of code indicates what we are doing: setting up our `Scene` class and creating a variable to store it. If you don't know what a class is, we strongly recommend learning more about **OOP** (**O**bject-**O**riented **P**rogramming).

```python title="main.py"
name="My Project Name",
```

This is the line where you can set the `name` of your project or video.

```python title="main.py"
width=1280,
height=720,
```

Here, we define the video dimensions by entering the `width` and `height`. It is important to have a basic understanding of dimensions. Here is a reference to use for your video:

* **4K UHD [16:9]: 3840 x 2160 (More definition, good for working)**
* **Full HD (1080p) [16:9]: 1920 x 1080 (Normal, good for social media)**
* **HD (720p) [16:9]: 1280 x 720 (Less definition, ideal for drafts)**
* **Vertical [9:16]: 720 x 1280 (Youtube Shorts, TikTok, Reels, etc.)**
* **Square [1:1]: 1080 x 1080 (Inusual, social media like Instagram, Facebook, etc.)**

```python title="main.py"
fps=60,
```

`fps` stands for ***Frames Per Second***. This value indicates the **frame rate** used to display the video: the higher the FPS, the smoother the video. The most common rates are 12, 24, 30, and 60 FPS, while 120, 240, and 480 FPS are used more rarely, typically for slow-motion effects.

```python
duration=120,
```

The `duration` field refers to the length of your video. If your video contains music, **do not use it**; this can cause errors and result in the music being cut off.

```python title="main.py"
anti_aliasing=True,
```

The `anti_aliasing` field is where you specify whether you want to use **Anti-aliasing**—a computer graphics technique used to smooth out jagged or "stepped" edges that appear on diagonal lines or curves. To learn more, [visit this article at web.dev](https://web.dev/articles/antialiasing-101). It is a useful feature, but depending on what you are doing with the library, it might not be suitable for your specific use case.
<p style="margin-top: 0.5rem !important;">*<small>The link redirects to an article from <a href="https://web.dev">web.dev</a> licensed under the <a href="https://creativecommons.org/licenses/by/4.0/"><b>Creative Commons Attribution 4.0 International (CC BY 4.0)</b></a></small></p>

```python title="main.py"
final_delay=0.2,
```

The `final_delay` field adds extra seconds to the end as a safety measure, in case the audio is cut off due to the video's duration.

```python title="main.py"
font_manager=None
```

This is the last field. It is used to insert your `font_manager`, which we will learn about shortly in the text section. It is set to `None` because we do not yet know what it is or how to use it.

---

There are a few methods we need to know about Scene before studying Objects, which is the next topic. There are three methods in the `Scene` class:

### The `add()` method

The `add()` function is used to add objects to the Scene, which we will study later. We use it as follows:

```python
add(object1, object2, object3...)
```

So, if you want to access the objects that are already in the scene, simply use the `objects` attribute:

```python
print("my_scene.objects = " + str(my_scene.objects))
```

So, when typing `python ./my_file.py`, we get this:

```bash
my_scene.objects = ((object1, object2), (object1, object2, object3))
```



## Adding Shapes

## Text

## Adding Music

## Rendering Your Scene
