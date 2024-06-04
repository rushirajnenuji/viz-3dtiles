import logging
import traceback
from Cesium3DTile import Cesium3DTile
from Cesium3DTileset import Tileset
import os

# Configure logging
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')

try:
    # Output Tileset directory -- view `tileset.json`
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_to= os.path.join(base_dir, "run-cesium", "tilesets", "Fishing zone")

    # Create a 3D Tile from the Example shp file
    tile = Cesium3DTile()   
    # tile.filter_by_attributes={"centroid_within_tile": True}
    tile.save_to=save_to # model.b3dm save path
    tile.from_file(os.path.join(base_dir, "input", "Fishing zone.shp"), crs="EPSG:3413", z=05.2)

    # Create a tileset to contain the 3D Tile just created
    tileset = Tileset.from_Cesium3DTiles(tile, os.path.join(save_to, "tileset.json"))

    print("b3dm generated")
except Exception as e:
    # Log the traceback
    logging.error(traceback.format_exc())
    print(e)
