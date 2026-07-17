import skia
from ..objects import Circle, Triangle, Rectangle
from ..text import Text
from ..scene import Scene

colors = {
    "red": skia.ColorRED,
    "blue": skia.ColorBLUE,
    "green": skia.ColorGREEN,
    "white": skia.ColorWHITE,
    "black": skia.ColorBLACK,
}

font_path = "../../assets/fonts/"

fonts = {
    "Figtree": str(font_path + "Figtree.ttf"),
    "Google_Sans": str(font_path + "Google_Sans.ttf"),
    "Inter": str(font_path + "Inter.ttf"),
    "Montserrat": str(font_path + "Montserrat.ttf"),
    "Noto_Sans": str(font_path + "Noto_Sans.ttf"),
    "Open_Sans": str(font_path + "Open_Sans.ttf"),
    "Roboto": str(font_path + "Roboto.ttf"),
}

def draw(scene: Scene):
    surface = skia.Surface(scene.width, scene.height)
    canvas = surface.getCanvas()

    canvas.clear(skia.ColorWHITE)

    for obj in scene.objects:
        paint = skia.Paint(
            Color = colors.get(
                obj.color,
                skia.ColorBLACK
            )
        )
        paint.setAntiAlias(scene.anti_aliasing) 

        if isinstance(obj, Rectangle):
            rect = skia.Rect.MakeXYWH(
                obj.x + scene.width / 2,
                obj.y + scene.height / 2,
                obj.width * obj.scale[0],
                obj.height * obj.scale[1]
            )
            canvas.drawRect(rect, paint)
        elif isinstance(obj, Circle):
            canvas.drawCircle(
                obj.x + scene.width / 2,
                obj.y + scene.height / 2,
                obj.radius * ((obj.scale[0] + obj.scale[1]) / 2),
                paint
            )
        elif isinstance(obj, Triangle):
            path = skia.Path()
            p0_0 = obj.points[0][0] - obj.x
            p0_1 = obj.points[0][1] - obj.y
            p1_0 = obj.points[1][0] - obj.x
            p1_1 = obj.points[1][1] - obj.y
            p2_0 = obj.points[2][0] - obj.x
            p2_1 = obj.points[2][1] - obj.y

            path.moveTo((p0_0 * obj.scale[0]) + obj.x + scene.width / 2, (p0_1 * obj.scale[1]) + obj.y + scene.height / 2)
            path.lineTo((p1_0 * obj.scale[0]) + obj.x + scene.width / 2, (p1_1 * obj.scale[1]) + obj.y + scene.height / 2)
            path.lineTo((p2_0 * obj.scale[0]) + obj.x + scene.width / 2, (p2_1 * obj.scale[1]) + obj.y + scene.height / 2)

            path.close()

            canvas.drawPath(path, paint)
        elif isinstance(obj, Text):
            if obj.font:
                typeface = skia.Typeface.MakeFromFile(fonts.get(obj.font, obj.font))
            else:
                typeface = skia.Typeface.MakeFromFile("../../assets/fonts/Open_Sans.ttf")

            font = skia.Font(
                typeface,
                obj.size
            )

            canvas.drawString(
                obj.text,
                obj.x + scene.width / 2,
                obj.y + scene.height / 2,
                font,
                paint
            )
        else:
            raise Exception(f"The object '{obj}' isn't a valid object")

    return surface.makeImageSnapshot()
