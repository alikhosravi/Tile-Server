import pandas as pd
import geopandas as gpd
from pathlib import Path
import numpy as np 
from shapely.geometry import Polygon
import math


def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 1 << zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
  return xtile, ytile

def StudyAreaTiles(minLon, minLat, maxLon, maxLat, zoom):
  cornTop = deg2num(maxLat, minLon, zoom)
  cornBottom = deg2num(minLat, maxLon, zoom)
  Pool = list()
  for column in range(cornTop[0], cornBottom[0]+1):
    for row in range(cornTop[1], cornBottom[1]+1):
      Pool.append([column, row, zoom])
  return Pool

def num2Tiles (sTiles, zoom):
  n = 1 << zoom
  Xs = np.array(sTiles).T[0]
  Ys = np.array(sTiles).T[1]
  lon_deg = Xs/n * 360.0 - 180.0
  lat_rad = np.arctan(np.sinh(math.pi * (1 - 2 * Ys / n)))
  lat_deg = np.degrees(lat_rad)
  lon_deg2 = (Xs+1)/n * 360.0 - 180.0
  lat_rad2 = np.arctan(np.sinh(math.pi * (1 - 2 * (Ys+1) / n)))
  lat_deg2 = np.degrees(lat_rad2)
  r = []
  for a, b, c , d , e in zip(np.vstack((lon_deg,lat_deg)).T, np.vstack((lon_deg2,lat_deg)).T, np.vstack((lon_deg2,lat_deg2)).T, np.vstack((lon_deg,lat_deg2)).T, np.vstack((lon_deg,lat_deg)).T):
    f = []
    f.append(tuple(a))
    f.append(tuple(b))
    f.append(tuple(c))
    f.append(tuple(d))
    f.append(tuple(e))
    r.append(tuple(f))
  pls = []
  for p in r:
    pls.append(Polygon(p))
  Tiles = gpd.GeoDataFrame(geometry=pls, crs=4326)
  Tiles['X'] = sTiles.T[0]
  Tiles['Y'] = sTiles.T[1]
  Tiles = Tiles.to_crs(3857)
  return Tiles


zoom = 16
country = gpd.read_file('/workspaces/Tile-Server/data/irn_admbnda_adm1_unhcr_20190514.shp')
if country.crs != 4326:
  country = country.to_crs(4326)
country3857 = country.to_crs(3857)


for i, row in country.iterrows():
    print(row['ADM1_EN'])
    minx, miny, maxx, maxy = country.loc[[i]].bounds.values[0]
    cornTop = deg2num(maxy, minx, zoom)
    cornBottom = deg2num(miny, maxx, zoom)
    list1 = np.arange(cornTop[0], cornBottom[0]+1)
    list2 = np.arange(cornTop[1], cornBottom[1]+1)
    sTiles = np.array(np.meshgrid(list1, list2)).T.reshape(-1, 2)
    Tiles = num2Tiles (sTiles, zoom)
    Out = gpd.sjoin(Tiles, country3857.loc[[i]], op = 'within')
    Out = Out.reset_index(drop=True)
    save = Out[['X', 'Y']].to_csv('/workspaces/Tile-Server/data/Tile numbers/Tiles_'+str(zoom)+'/'+row['ADM1_EN']+'.csv')
    