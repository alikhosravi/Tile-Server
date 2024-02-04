from requests import get
from pathlib  import Path
from .head    import headers

def quadKey(level, x, y):
    quad_key = ""
    i = level
    while i > 0:
        digit = 0
        mask = 1 << (i - 1)
        if ((x & mask) != 0):
            digit += 1
        if ((y & mask) != 0):
            digit += 2
        quad_key += str(digit)
        i -= 1
    return quad_key

def downloader(level, x, y):
    if not Path.exists(Path("output/bing_satellite/{}/{}".format(str(level), str(x)))):
        Path("output/bing_satellite/{}/{}".format(str(level), str(x))).mkdir(parents=True)
    output = 'output/bing_satellite/{}/{}/{}.png'.format(str(level), str(x), str(y))
    url = 'http://h0.ortho.tiles.virtualearth.net/tiles/a' + quadKey(level, x, y) + ".png?g=131"
    image = get(url, stream=True, headers= headers()).content
    with open(output, 'wb') as handler:
        handler.write(image)