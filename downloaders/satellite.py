from requests import get
from pathlib  import Path
from .head    import headers

def downloader(level, x, y):
    if not Path.exists(Path("output/satellite/{}/{}".format(str(level), str(x)))):
        Path("output/satellite/{}/{}".format(str(level), str(x))).mkdir(parents=True)
    output = 'output/satellite/{}/{}/{}.png'.format(str(level), str(x), str(y))
    url = 'https://mt0.google.com/vt/lyrs=s&hl=en&x='+str(x)+'&y='+str(y)+'&z='+str(level)+'&s=Ga'
    image = get(url, stream=True, headers= headers()).content
    with open(output, 'wb') as handler:
        handler.write(image)