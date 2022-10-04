from DownloadingFunctions import BulkDownloadTimeSeries


'''
TODO: Fill out the following parameters to download the desired data
The internal variable names of the CIE-API can be found in the Metadata script or in the CIE metadata https://cie-api.climateanalytics.org/api/meta/
For an example on how to fill out the lists see the example.py script
@param: SAVEPATH Path of the diretory on your computer the data should be saved at
@param: format Format of the downloaded data, can be csv, png and pdf
@param: Countries List of the Alpha-3 Codes of desired Countries, Countries available in the CIE can be found in the Metadata
@param: isSubdivisionalLevel True if data should be downloaded for every Subdivision of a Country, False if data should be downloaded only for overall Countries
@param: Impacts List of the Variable Codes of desired Impacts, Variable Codes Available in the CIE can be found in the Metadata
@param: SpatialAggregations List of the desired Spatial Aggregation Methods, can be area, pop, gdp and other (other is only used for economic indicators)
@param: Seasons List of the desired Seasonal Averaging Methods, can be annual, MAM, JJA, SON, DJF
@param: Scenarios List of the desired Scenarios, only needed if fromat = png or format = pdf, can be rcp26, rcp45, rcp60, rcp85, h_cpol, o_1p5c, d_delfrag, cat_current
'''

SAVEPATH = ''
format = ''
Countries = []
isSubdivisionalLevel = False
Impacts = []
SpatialAggregations = []   #Always add 'other' if you selected 'ec2', 'ec3' or 'ec4' as impacts
Seasons = []
Scenarios = [] #can be left empty if format = 'csv'


BulkDownloadTimeSeries(SAVEPATH,format,Countries,isSubdivisionalLevel,Impacts,SpatialAggregations,Seasons,Scenarios)
