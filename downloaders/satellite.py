from requests import get
from pathlib  import Path
from .head    import headers

def downloader(level, x, y):
    if not Path.exists(Path("output/osm/{}/{}".format(str(level), str(x)))):
        Path("output/osm/{}/{}".format(str(level), str(x))).mkdir(parents=True)
    output = 'output/osm/{}/{}/{}.png'.format(str(level), str(x), str(y))
    url = 'https://b.tile.openstreetmap.org/'+str(level)+'/'+str(x)+'/'+str(y)+'.png'
    image = get(url, stream=True, headers= headers()).content
    with open(output, 'wb') as handler:
        handler.write(image)