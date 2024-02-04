#required libraries
import geopandas as gpd
import math
from shapely.geometry import Polygon
import pandas as pd

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 1 << zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
  return xtile, ytile
  
def StudyAreaTiles(minLat, minLon, maxLat, maxLon, zoom):
  cornTop = deg2num(maxLat, minLon, zoom)
  cornBottom = deg2num(minLat, maxLon, zoom)
  Pool = list()
  for column in range(cornTop[0], cornBottom[0]+1):
    for row in range(cornTop[1], cornBottom[1]+1):
      Pool.append([column, row, zoom])
  return Pool

def tileFinder(props):
  xtile, ytile, zoom = props[0], props[1], props[2]
  n = 1 << zoom
  lon_deg = xtile / n * 360.0 - 180.0
  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
  lat_deg = math.degrees(lat_rad)
  lon_deg2 = (xtile+1) / n * 360.0 - 180.0
  lat_rad2 = math.atan(math.sinh(math.pi * (1 - 2 * (ytile+1) / n)))
  lat_deg2 = math.degrees(lat_rad2)
  return Polygon(((lon_deg,lat_deg), (lon_deg2,lat_deg), (lon_deg2,lat_deg2), (lon_deg,lat_deg2), (lon_deg,lat_deg)))

def Frame(path, zoom):
  country = gpd.read_file(path) 
  if country.crs != 4326:
    country = country.to_crs(4326)
  country3857 = country.to_crs(3857)
  sTiles  = StudyAreaTiles(country.bounds['miny'][0], country.bounds['minx'][0], country.bounds['maxy'][0], country.bounds['maxx'][0], zoom)
  Tiles = gpd.GeoDataFrame(geometry=[tileFinder(props) for props in sTiles], crs=4326)
  Tiles['TileNum'] = sTiles
  Tiles = Tiles.to_crs(3857)
  indx = Tiles.geometry.intersects(country3857.geometry[0])
  return Tiles.loc[indx[indx].index]
