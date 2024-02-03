from geometry2tiles import TileList
from downloaders    import cartodb_light, cartodb_dark, osm, lima, satellite


x, y = TileList.LOT('data/irn_admbnda_adm0_unhcr_20190514.shp',8)[0]

osm.downloader(8, x, y)

