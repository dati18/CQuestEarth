import ee
ee.Initialize()
#Add Dataset
color_palette = ['FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901','66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01','012E01', '011D01', '011301']
viridis_palette =['440154FF','481567FF','482677FF','453781FF','404788FF','39568CFF','33638DFF','2D708EFF','287D8EFF','238A8DFF','1F968BFF','20A387FF','29AF7FFF','3CBB75FF','55C667FF','73D055FF','95D840FF','B8DE29FF','DCE319FF','FDE725FF']


def merge_and_sort_collections(image_collection1, image_collection2):
  merged_collection = image_collection1.merge(image_collection2)
  sorted_collection = merged_collection.sort("system:time_start")
  return sorted_collection

#Merge and sort modis collections
modis_vi_combined = merge_and_sort_collections(
    ee.ImageCollection('MODIS/006/MOD13Q1'),                        #2000-02-18 - 2021-01-01
    ee.ImageCollection('MODIS/006/MYD13Q1')                         #2002-07-04 - 2020-12-26
)

def func_dmi(image):
      out_image = image.divide(10000)
      out_image = out_image.set({"system:time_start": image.get("system:time_start")})
      return out_image

modis_vi = modis_vi_combined.map(func_dmi)

#ndvi and evi
modis_collection = modis_vi.filter(ee.Filter.date("2020-01-01", "2021-01-01"))
ndvi = modis_collection.select('NDVI').median()
evi = modis_collection.select('EVI').median()
modisVis = {
    'min': 0.0,
    'max': 1.0,
    'palette': color_palette
}
#gpp
gpp_collection_unfiltered = ee.ImageCollection('MODIS/006/MOD17A2H')
gpp_collection = gpp_collection_unfiltered.filter(ee.Filter.date("2018-01-01", "2019-01-01"))
gpp = gpp_collection.select('Gpp').sum()
gppVis = {
  'min': 0.0,
  'max': 20000.0,
  'palette': color_palette
}
#npp
npp_collection_unfiltered = ee.ImageCollection('MODIS/006/MOD17A3HGF')
npp_collection = npp_collection_unfiltered.filter(ee.Filter.date("2018-01-01", "2019-01-01"))
npp = npp_collection.select('Npp').first()
nppVis = {
  'min': 0.0,
  'max': 20000.0,
  'palette': color_palette
}
#lai
lai_collection_unfiltered = ee.ImageCollection('MODIS/006/MCD15A3H') 
lai_collection = lai_collection_unfiltered.filter(ee.Filter.date("2020-01-01", "2021-01-01"))
lai = lai_collection.select('Lai').median()
laiVis = {
  'min': 0.0,
  'max': 100.0,
  'palette': color_palette
}
#landsat ndvi and evi
landsat7_ndvi_collection_unfiltered = ee.ImageCollection("LANDSAT/LE07/C01/T1_8DAY_NDVI")
landsat7_ndvi_collection = landsat7_ndvi_collection_unfiltered.filter(ee.Filter.date("2020-01-01", "2021-01-01"))
landsat7_ndvi = landsat7_ndvi_collection.select('NDVI').median()

landsat7_evi_collection_unfiltered = ee.ImageCollection("LANDSAT/LE07/C01/T1_8DAY_EVI")
landsat7_evi_collection = landsat7_evi_collection_unfiltered.filter(ee.Filter.date("2020-01-01", "2021-01-01"))
landsat7_evi = landsat7_evi_collection.select('EVI').median()

landsatVis = {
  'min': 0.0,
  'max': 1.0,
  'palette': color_palette
}

#soilgrid data (ocs, ocd, soc)
ocs_collection = ee.Image("projects/soilgrids-isric/ocs_mean")
ocs = ocs_collection.select('ocs_0-30cm_mean')
ocsVis = {
    'min': 0.0,
    'max': 100.0,
    'palette': viridis_palette
}

ocd_collection = ee.Image("projects/soilgrids-isric/ocd_mean")
ocd = ocd_collection.select("ocd_0-5cm_mean").divide(6).add(ocd_collection.select("ocd_5-15cm_mean").divide(3).add(ocd_collection.select("ocd_15-30cm_mean").divide(2)))

ocdVis = {
    'min': 0.0,
    'max': 500.0,
    'palette': viridis_palette
}

soc_collection = ee.Image("projects/soilgrids-isric/soc_mean")
soc = soc_collection.select("soc_0-5cm_mean").add(soc_collection.select("soc_5-15cm_mean").add(soc_collection.select("soc_15-30cm_mean")))
socVis = {
    'min': 0.0,
    'max': 5000.0,
    'palette': viridis_palette
}

veg_indices = {
    'MODIS NDVI (250m)':{
        'collection': modis_vi,
        'band': 'NDVI',
        'name': 'MODIS NDVI',
        'visual': ndvi,
        'vis_params': modisVis,
        'resolution': 250,
        'unit': 'NDVI'
    },
    'MODIS EVI (250m)':{
        'collection': modis_vi,
        'band': 'EVI',
        'name':'MODIS EVI',
        'visual': evi,
        'vis_params': modisVis,
        'resolution': 250,
        'unit': 'EVI'
    },
    'MODIS GPP (500m)':{
        'collection': gpp_collection_unfiltered,
        'band': 'Gpp',
        'name':'MODIS GPP',
        'visual': gpp,
        'vis_params': gppVis,
        'resolution': 500,
        'unit': 'GPP kg*C/m²'
    },
    'MODIS NPP (500m)':{
        'collection': npp_collection_unfiltered,
        'band': 'Npp',
        'name':'MODIS NPP',
        'visual': npp,
        'vis_params': nppVis,
        'resolution': 500,
        'unit': 'NPP kg*C/m²'
    },
    'MODIS LAI (500m)':{
        'collection': lai_collection_unfiltered,
        'band': 'Lai',
        'name':'MODIS LAI',
        'visual': lai,
        'vis_params': laiVis,
        'resolution': 500,
        'unit': 'LAI %'
    },
    'LANDSAT 7 NDVI (30m)':{
        'collection': landsat7_ndvi_collection_unfiltered,
        'band': 'NDVI',
        'name':'LANDSAT 7 NDVI',
        'visual': landsat7_ndvi,
        'vis_params': landsatVis,
        'resolution': 30,
        'unit': 'NDVI'
    },
    'LANDSAT 7 EVI (30m)':{
        'collection': landsat7_evi_collection_unfiltered,
        'band': 'EVI',
        'name':'LANDSAT 7 EVI',
        'visual': landsat7_evi,
        'vis_params': landsatVis,
        'resolution': 300,
        'unit': 'EVI'
    },
    'Organic carbon density':{
      'collection': ocd_collection,
      'name': 'Organic carbon density',
      'visual': ocd,
      'vis_params':ocdVis,
    },
    'Organic carbon stock':{
      'collection': ocs_collection,
      'name': 'Organic carbon stock',
      'visual': ocs,
      'vis_params':ocsVis,
    },
    'Soil organic carbon':{
      'collection': soc_collection,
      'name': 'Soil organic carbon',
      'visual': soc,
      'vis_params':socVis,
    },
}