from requests import get
from pathlib  import Path
headers = {'authority': 'b.tile.openstreetmap.org','method':'GET','scheme':'https','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en,en-US;q=0.9','Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Windows"','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def downloader(x, y, level):
    if not Path.exists(Path("output/osm/{}/{}".format(str(level), str(x)))):
        Path("output/osm/{}/{}".format(str(level), str(x))).mkdir(parents=True)
    output = 'output/osm/{}/{}/{}.png'.format(str(level), str(x), str(y))
    if not Path.exists(Path(output)):
        url = 'https://b.tile.openstreetmap.org/'+str(level)+'/'+str(x)+'/'+str(y)+'.png'
        image = get(url, stream=True, headers= headers).content
        with open(output, 'wb') as handler:
            handler.write(image)