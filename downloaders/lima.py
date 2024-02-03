from requests import get
from pathlib  import Path
from .head    import headers

def downloader(level, x, y):
    if not Path.exists(Path("output/lima/{}/{}".format(str(level), str(x)))):
        Path("output/lima/{}/{}".format(str(level), str(x))).mkdir(parents=True)
    output = 'output/lima/{}/{}/{}.png'.format(str(level), str(x), str(y))
    url = 'https://cdn.lima-labs.com/'+str(level)+'/'+str(x)+'/'+str(y)+'.png?api=demo'
    image = get(url, stream=True, headers= headers()).content
    with open(output, 'wb') as handler:
        handler.write(image)