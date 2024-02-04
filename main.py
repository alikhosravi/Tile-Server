from geometry2tiles import TileList, TileFrame
from downloaders    import cartodb_light, cartodb_dark, osm, lima, satellite, bing_satellite, bing_road

zoom = 8

tiles = TileFrame.Frame('data/irn_admbnda_adm0_unhcr_20190514.shp',zoom)
'''
tiles = TileList.LOT('data/irn_admbnda_adm0_unhcr_20190514.shp',zoom)
for tile in tiles:
    x, y = tile
    reference = bing_satellite #change reference
    reference.downloader(zoom, x, y)

'''
