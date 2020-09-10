import io
from collections import Counter  # counts top colors
import coverpy  # gets album art
# all for color similarity
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000


def color_sim(c1, c2):
    # create colors in package
    color1_rgb = sRGBColor(int(c1[0])/255, int(c1[1])/255, int(c1[2])/255)
    color2_rgb = sRGBColor(int(c2[0])/255, int(c2[1])/255, int(c2[2])/255)
    # Convert from RGB to Lab Color Space
    color1_lab = convert_color(color1_rgb, LabColor)
    # Convert from RGB to Lab Color Space
    color2_lab = convert_color(color2_rgb, LabColor)
    # Find the color difference
    delta_e = delta_e_cie2000(color1_lab, color2_lab)

    return delta_e


# returns the album art in a given dimensions (200x200 for now)
def get_art(name):
    import coverpy  # not sure why this needs to be here but it breaks if I put them up top
    import html
    coverpy = coverpy.CoverPy()
    limit = 1
    try:
        result = coverpy.get_cover(name, limit)
    except:
        return
    return result.artwork(800)


# helper function used to get the image
def requests_image(name):  # not sure why this needs to be here but it breaks if I put them up top
    from PIL import Image
    import requests
    i = requests.get(get_art(name)).content
    image = Image.open(io.BytesIO(i))
    return image


def compute_top_image_colors(name):
    THRESHOLD = 5.4  # cutoff for similarity, closer to 0 is more similar
    img = requests_image(name)
    width, height = img.size
    colors = []
    for x in range(0, width):
        for y in range(0, height):
            # get pixel rgb
            r, g, b = img.getpixel((x, y))
            # turm into string so collections.Counter can work
            colors.append(str(r) + ' ' + str(g) + ' ' + str(b))
    top_colors = Counter(colors).most_common(250)
    to_pop = []
    for i, c1 in enumerate(top_colors):
        for j in range(i+1, len(top_colors)):
            c2 = top_colors[j]
            if color_sim(c1[0].split(), c2[0].split()) < THRESHOLD:
                to_pop.append(i)
    for bad_color in sorted(set(to_pop), reverse=True):
        del top_colors[bad_color]
    actual = []
    for color in top_colors:
        curr = []
        to_add = color[0].split()
        for c in to_add:
            curr.append(int(c))
        actual.append(curr)
    return actual
