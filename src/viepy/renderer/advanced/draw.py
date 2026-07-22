import skia

from ...objects import Circle, Triangle, Rectangle, Group
from ...text import Text
from ...scene import Scene
from ...Exceptions import DrawError


colors = {
    "red": skia.ColorRED,
    "blue": skia.ColorBLUE,
    "green": skia.ColorGREEN,
    "white": skia.ColorWHITE,
    "black": skia.ColorBLACK,
}


def draw_object(canvas, obj, scene: Scene, center_x: float, center_y: float, fonts: dict[str, str],):
    if not obj.visible:
        return

    paint = skia.Paint(
        Color=colors.get(
            obj.color,
            skia.ColorBLACK
        )
    )

    paint.setAntiAlias(scene.anti_aliasing)
    paint.setAlphaf(obj.opacity)

    if isinstance(obj, Group):
        canvas.save()

        canvas.translate(
            obj.transform.x,
            obj.transform.y
        )

        canvas.rotate(
            obj.transform.rotate
        )

        canvas.scale(
            obj.transform.scale[0],
            obj.transform.scale[1]
        )

        for child in obj.objects:
            draw_object(
                canvas,
                child,
                scene,
                0,
                0,
                fonts
            )

        canvas.restore()
        return

    canvas.save()

    canvas.translate(
        obj.transform.x + center_x,
        obj.transform.y + center_y
    )

    canvas.rotate(
        obj.transform.rotate
    )

    canvas.scale(
        obj.transform.scale[0],
        obj.transform.scale[1]
    )

    if isinstance(obj, Rectangle):
        width = obj.width
        height = obj.height

        rect = skia.Rect.MakeXYWH(
            -width / 2,
            -height / 2,
            width,
            height
        )

        canvas.drawRect(
            rect,
            paint
        )

    elif isinstance(obj, Circle):
        canvas.drawCircle(
            0,
            0,
            obj.radius,
            paint
        )

    elif isinstance(obj, Triangle):
        path = skia.Path()

        path.moveTo(
            obj.points[0][0] - obj.transform.x,
            obj.points[0][1] - obj.transform.y
        )

        path.lineTo(
            obj.points[1][0] - obj.transform.x,
            obj.points[1][1] - obj.transform.y
        )

        path.lineTo(
            obj.points[2][0] - obj.transform.x,
            obj.points[2][1] - obj.transform.y
        )

        path.close()

        canvas.drawPath(
            path,
            paint
        )

    elif isinstance(obj, Text):
        if obj.font:
            font_path = fonts.get(
                str(obj.font),
                str(obj.font)
            )
        else:
            font_path = fonts["Open_Sans"]

        typeface = skia.Typeface.MakeFromFile(
            font_path
        )

        if typeface is None:
            raise DrawError(
                f"Could not load font: {font_path}"
            )

        font = skia.Font(
            typeface,
            obj.size
        )

        canvas.drawString(
            obj.text,
            0,
            0,
            font,
            paint
        )

    else:
        raise DrawError(
            f"The object '{obj}' isn't a valid object"
        )

    canvas.restore()


def draw(scene: Scene, current_time: float):
    font_path = scene.font_manager.fonts_path

    fonts = {
        "Figtree": str(font_path / "Figtree.ttf"),
        "Google_Sans": str(font_path / "Google_Sans.ttf"),
        "Inter": str(font_path / "Inter.ttf"),
        "Montserrat": str(font_path / "Montserrat.ttf"),
        "Noto_Sans": str(font_path / "Noto_Sans.ttf"),
        "Open_Sans": str(font_path / "Open_Sans.ttf"),
        "Roboto": str(font_path / "Roboto.ttf"),
    }

    surface = skia.Surface(
        scene.width,
        scene.height
    )

    canvas = surface.getCanvas()

    canvas.clear(
        skia.ColorWHITE
    )

    center_x = scene.width / 2
    center_y = scene.height / 2

    for layer in scene.objects:
        for obj in layer:
            draw_object(
                canvas,
                obj,
                scene,
                center_x,
                center_y,
                fonts
            )

    return surface.makeImageSnapshot()
