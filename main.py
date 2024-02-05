from geometry2tiles import TileList, TileFrame
from downloaders    import cartodb_light, cartodb_dark, osm, lima, satellite, bing_satellite, bing_road
import pandas as pd
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import shutil


refrence = osm
zoom = 13
s = datetime.utcnow()
for region in [f.stem for f in Path('data/Tile numbers/'+str(zoom)).iterdir()]:
    numbs = pd.read_csv('/workspaces/Tile-Server/data/Tile numbers/'+str(zoom)+'/'+region+'.csv')
    with ThreadPoolExecutor(max_workers=100) as pool:
        pool.map(refrence.downloader,numbs['X'], numbs['Y'], [zoom]*len(numbs))
e = datetime.utcnow()
shutil.make_archive('/workspaces/Tile-Server/output/osm/'+str(zoom), 'zip', '/workspaces/Tile-Server/output/osm', str(zoom))
print(e-s)



'''
tiles = TileFrame.Frame('data/irn_admbnda_adm0_unhcr_20190514.shp',zoom)

tiles = TileList.LOT('data/irn_admbnda_adm0_unhcr_20190514.shp',zoom)
for tile in tiles:
    x, y = tile
    reference = bing_satellite #change reference
    reference.downloader(zoom, x, y)

'''