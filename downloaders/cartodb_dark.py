from requests import get
from pathlib  import Path
from .head    import headers

def downloader(level, x, y):
    if not Path.exists(Path("output/cartodb_dark/{}/{}".format(str(level), str(x)))):
        Path("output/cartodb_dark/{}/{}".format(str(level), str(x))).mkdir(parents=True)
    output = 'output/cartodb_dark/{}/{}/{}.png'.format(str(level), str(x), str(y))
    url = 'https://cartodb-basemaps-a.global.ssl.fastly.net/dark_all/'+str(level)+'/'+str(x)+'/'+str(y)+'.png'
    image = get(url, stream=True, headers= headers()).content
    with open(output, 'wb') as handler:
        handler.write(image)