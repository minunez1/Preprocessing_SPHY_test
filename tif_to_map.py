from os import chdir
from pcraster import *
from osgeo import gdal, gdalconst
import matplotlib.pyplot as plt

#Create function to convert from tif to map
def ConvertToPCRaster (src_fname,dst_fname,ot,VS):
    src_ds = gdal.Open(src_fname)
    dst_ds = gdal.Translate(dst_fname, src_ds, format="PCRaster", outputType=ot, metadataOptions=VS)
    src_ds = None
    dst_ds = None

dir="D:\PuertoCisnes_prueba\\250m_pixel"
chdir(dir)
# Ruta al archivo .jp2
tif_file = 'DEM_mask.tif'

ConvertToPCRaster(tif_file,"dem.map",gdalconst.GDT_Float32,"VS_SCALAR")
dem = readmap("dem.map")
#demf = lddcreatedem(dem,1e31,1e31,1e31,1e31)
#report(demf,"dem500f.map")
aguila(dem)

