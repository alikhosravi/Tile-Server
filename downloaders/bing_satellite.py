from requests import get
from pathlib  import Path
headers = {'authority': 'b.tile.openstreetmap.org','method':'GET','scheme':'https','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en,en-US;q=0.9','Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Windows"','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

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