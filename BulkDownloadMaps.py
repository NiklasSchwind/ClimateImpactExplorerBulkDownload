from DownloadingFunctions import BulkDownloadMaps

'''
TODO: Fill out the following parameters to download the desired data
The internal variable names of the CIE-API can be found in the Metadata script or in the CIE metadata https://cie-api.climateanalytics.org/api/meta/
For an example on how to fill out the lists see the example.py script
@param: SAVEPATH Path of the diretory on your computer the data should be saved at
@param: format Format of the downloaded data, can be csv, png and pdf
@param: Countries List of the Alpha-3 Codes of desired Countries, Countries Available in the CIE can be found in the Metadata
@param: Impacts List of the Variable Codes of desired Impacts, Variable Codes Available in the CIE can be found in the Metadata
@param: Seasons List of the desired Seasonal Averaging Methods, can be annual, MAM, JJA, SON, DJF
@param: WarmingLevels List of the desired Warming Levels, Strings of Numbers with one decimal place between 1.1 and 3.4
'''


SAVEPATH = ''
format = ''
Countries = []
Impacts = []
Seasons = []
WarmingLevels = []



BulkDownloadMaps(SAVEPATH, format, Countries, Impacts, Seasons, WarmingLevels)
