import requests
import urllib.request
import Metadata
import itertools

def DownloadCSVfromURLtoPATH(URL, PATH, FILENAME):
    '''
    Function to download a csv file from the CIE-API to a certain directory on your Computer
    @param: URL The URL for downloading a File from the CIE API
    @param: PATH Path to the directory where the File should be saved
    @param: FILENAME Name of the File that should be safed
    '''
    try:
        req = requests.get(URL)
        url_content = req.content
        dummy_response_timeseries = str(
            b'{\n  "lower": null, \n  "median": null, \n  "upper": null, \n  "wlvl": null, \n  "year": null\n}\n')
        dummy_response_maps = str(
            b'{\n  "agreement": null, \n  "attrs": {}, \n  "coords": {\n    "ID": {\n      "attrs": {}, \n      "data": "HadGEM2-ES_rcp60", \n      "dims": []\n    }, \n    "lat": {\n      "attrs": {\n        "axis": "Y", \n        "long_name": "latitude", \n        "standard_name": "latitude", \n        "units": "degrees_north"\n      }, \n      "data": [\n        null, \n        null\n      ], \n      "dims": [\n        "lat"\n      ]\n    }, \n    "lon": {\n      "attrs": {\n        "axis": "X", \n        "long_name": "longitude", \n        "standard_name": "longitude", \n        "units": "degrees_east"\n      }, \n      "data": [\n        null, \n        null, \n        null\n      ], \n      "dims": [\n        "lon"\n      ]\n    }, \n    "region": {\n      "attrs": {}, \n      "data": "BEN", \n      "dims": []\n    }\n  }, \n  "data": null, \n  "dims": [\n    "lat", \n    "lon"\n  ], \n  "name": "var"\n}\n')
        if not (str(url_content) == dummy_response_timeseries or str(url_content) == dummy_response_maps):
            csv_file = open(PATH + '/' + FILENAME + '.csv', 'wb')
            csv_file.write(url_content)
            csv_file.close()
        else:
            print(f'Data for {URL} not available.')
    except:
        print(f'Download failed for {URL}')

def DownloadPNGfromURLtoPATH(URL,PATH,FILENAME):
    '''
    Function to download a png from the Climate Impact Explorer to a certain directory on your Computer
    @param: URL The URL for downloading a File from the CIE API
    @param: PATH Path to the directory where the File should be saved
    @param: FILENAME Name of the File that should be safed
    '''
    try:
        urllib.request.urlretrieve(URL,PATH + '/' + FILENAME+'.png')
    except:
        print(f'Download failed for {URL}')


def DownloadPDFfromURLtoPATH(URL,PATH,FILENAME):
    '''
    Function to download a png from the Climate Impact Explorer to a certain directory on your Computer
    @param: URL The URL for downloading a File from the CIE API
    @param: PATH Path to the directory where the File should be saved
    @param: FILENAME Name of the File that should be safed
    '''
    try:
        urllib.request.urlretrieve(URL,PATH + '/' + FILENAME+'.pdf')
    except:
        print(f'Download failed for {URL}')

def BulkDownloadMaps(SAVEPATH:str, format:str, Countries: list, Impacts: list, Seasons: list, WarmingLevels: list):
    '''
    Function to download all Maps defined by the parameters and available on the CIE
    @param: SAVEPATH Path of the diretory on your computer the data should be saved at
    @param: format Format of the downloaded data, can be csv, png and pdf
    @param: Countries List of the Alpha-3 Codes of desired Countries, Countries Available in the CIE can be found in the Metadata
    @param: Impacts List of the Variable Codes of desired Impacts, Variable Codes Available in the CIE can be found in the Metadata
    @param: Seasons List of the desired Seasonal Averaging Methods, can be annual, MAM, JJA, SON, DJF
    @param: WarmingLevels List of the desired Warming Levels, Strings of Numbers with one decimal place between 1.1 and 3.4
    '''
    for country, impact, season, warming_level in list(itertools.product(Countries, Impacts, Seasons, WarmingLevels)):

        if format == 'csv' and season in Metadata.AvailableSeasonalAverages[impact]:

            URL = f'https://cie-api.climateanalytics.org/api/geo-data/?iso={country}&var={impact}&season={season}&format=csv&scenarios=cat_current&warming_levels={warming_level}'
            FILENAME = f'CIE_MAP_{impact}_{country}_{season}_{warming_level}'
            DownloadCSVfromURLtoPATH(URL,SAVEPATH,FILENAME)

        elif format == 'png' and season in Metadata.AvailableSeasonalAverages[impact]:

            URL = f'http://climate-impact-explorer.climateanalytics.org/api/puppeteer/screengrab?url=http%3A%2F%2Fclimate-impact-explorer.climateanalytics.org%2Fembeds%3Fregion%3D{country}%26indicator%3D{impact}%26scenario%3Dh_cpol%26warmingLevel%3D{warming_level}%26temporalAveraging%3D{season}%26spatialWeighting%3Darea%26compareYear%3D2030%26embed%3Dimpact-map%26static%3Dtrue&format=png&width=1200&processingIntensity=2'
            FILENAME = f'CIE_MAP_{impact}_{country}_{season}_{warming_level}'
            DownloadPNGfromURLtoPATH(URL,SAVEPATH,FILENAME)

        elif format == 'pdf' and season in Metadata.AvailableSeasonalAverages[impact]:
            URL = f'http://climate-impact-explorer.climateanalytics.org/api/puppeteer/screengrab?url=http%3A%2F%2Fclimate-impact-explorer.climateanalytics.org%2Fembeds%3Fregion%3D{country}%26indicator%3D{impact}%26scenario%3Dh_cpol%26warmingLevel%3D{warming_level}%26temporalAveraging%3D{season}%26spatialWeighting%3Darea%26compareYear%3D2030%26embed%3Dimpact-map%26static%3Dtrue&format=pdf&width=1200&processingIntensity=2'
            FILENAME = f'CIE_MAP_{impact}_{country}_{season}_{warming_level}'
            DownloadPDFfromURLtoPATH(URL, SAVEPATH, FILENAME)

def BulkDownloadTimeSeries(SAVEPATH:str, format:str, Countries: list, isSubdivisionalLevel:bool, Impacts: list, SpatialAggregations:list , Seasons: list, Scenarios: list = []):
    '''
    Function to download all Maps defined by the parameters and available on the CIE
    @param: SAVEPATH Path of the diretory on your computer the data should be saved at
    @param: format Format of the downloaded data, can be csv, png and pdf
    @param: Countries List of the Alpha-3 Codes of desired Countries, Countries available in the CIE can be found in the Metadata
    @param: isSubdivisionalLevel True if data should be downloaded for every Subdivision of a Country, False if data should be downloaded only for overall Countries
    @param: Impacts List of the Variable Codes of desired Impacts, Variable Codes Available in the CIE can be found in the Metadata
    @param: SpatialAggregations List of the desired Spatial Aggregation Methods, can be area, pop, gdp and other (other is only used for economic indicators)
    @param: Seasons List of the desired Seasonal Averaging Methods, can be annual, MAM, JJA, SON, DJF
    @param: Scenarios List of the desired Scenarios, only needed if fromat = png or format = pdf, can be rcp26, rcp45, rcp60, rcp85, h_cpol, o_1p5c, d_delfrag, cat_current
    '''
    for country, impact, season, spatial_aggregation in list(
            itertools.product(Countries, Impacts, Seasons, SpatialAggregations)):

         if (spatial_aggregation in Metadata.AvailableSpatialAggregations[impact]) and (season in Metadata.AvailableSeasonalAverages[impact]):

                if isSubdivisionalLevel:

                    for subdivision in Metadata.Subdivisions[country]:

                        if format == 'csv':

                            URL = f'https://cie-api.climateanalytics.org/api/timeseries/?iso={country}&region={subdivision}&scenario=cat_current&var={impact}&season={season}&aggregation_spatial={spatial_aggregation}&format=csv'
                            FILENAME = f'CIE_Timeseries_{impact}_{country}_{subdivision}_allScenarios_{season}_{spatial_aggregation}'
                            DownloadCSVfromURLtoPATH(URL,SAVEPATH,FILENAME)

                        elif format == 'png':

                            for scenario in Scenarios:

                                URL = f'http://climate-impact-explorer.climateanalytics.org/api/puppeteer/screengrab?url=http%3A%2F%2Fclimate-impact-explorer.climateanalytics.org%2Fembeds%3Fregion%3D{country}%26indicator%3D{impact}%26scenario%3D{scenario}%26subregion%3D{subdivision}%26warmingLevel%3D1.5%26temporalAveraging%3D{season}%26spatialWeighting%3D{spatial_aggregation}%26compareYear%3D2030%26embed%3Dtimeseries%26static%3Dtrue&format=png&width=1025'
                                FILENAME = f'CIE_Timeseries_{impact}_{country}_{subdivision}_{season}_{spatial_aggregation}'
                                DownloadPNGfromURLtoPATH(URL, SAVEPATH, FILENAME)

                        elif format == 'pdf':

                            for scenario in Scenarios:

                                URL = f'http://climate-impact-explorer.climateanalytics.org/api/puppeteer/screengrab?url=http%3A%2F%2Fclimate-impact-explorer.climateanalytics.org%2Fembeds%3Fregion%3D{country}%26indicator%3D{impact}%26scenario%3D{scenario}%26subregion%3D{subdivision}%26warmingLevel%3D1.5%26temporalAveraging%3D{season}%26spatialWeighting%3D{spatial_aggregation}%26compareYear%3D2030%26embed%3Dtimeseries%26static%3Dtrue&format=pdf&width=1025'
                                FILENAME = f'CIE_Timeseries_{impact}_{country}_{subdivision}_{season}_{spatial_aggregation}'
                                DownloadPDFfromURLtoPATH(URL, SAVEPATH, FILENAME)

                elif not isSubdivisionalLevel:

                    if format == 'csv':

                        URL = f'https://cie-api.climateanalytics.org/api/timeseries/?iso={country}&region={country}&scenario=cat_current&var={impact}&season={season}&aggregation_spatial={spatial_aggregation}&format=csv'
                        FILENAME = f'CIE_Timeseries_{impact}_{country}_allScenarios_{season}_{spatial_aggregation}'
                        DownloadCSVfromURLtoPATH(URL, SAVEPATH, FILENAME)

                    elif format == 'png':

                        for scenario in Scenarios:

                            URL = f'http://climate-impact-explorer.climateanalytics.org/api/puppeteer/screengrab?url=http%3A%2F%2Fclimate-impact-explorer.climateanalytics.org%2Fembeds%3Fregion%3D{country}%26indicator%3D{impact}%26scenario%3D{scenario}%26warmingLevel%3D1.5%26temporalAveraging%3D{season}%26spatialWeighting%3D{spatial_aggregation}%26compareYear%3D2030%26embed%3Dtimeseries%26static%3Dtrue&format=png&width=1025'
                            FILENAME = f'CIE_Timeseries_{impact}_{country}_{season}_{spatial_aggregation}'
                            DownloadPNGfromURLtoPATH(URL, SAVEPATH, FILENAME)

                    elif format == 'pdf':

                        for scenario in Scenarios:

                            URL = f'http://climate-impact-explorer.climateanalytics.org/api/puppeteer/screengrab?url=http%3A%2F%2Fclimate-impact-explorer.climateanalytics.org%2Fembeds%3Fregion%3D{country}%26indicator%3D{impact}%26scenario%3D{scenario}%26warmingLevel%3D1.5%26temporalAveraging%3D{season}%26spatialWeighting%3D{spatial_aggregation}%26compareYear%3D2030%26embed%3Dtimeseries%26static%3Dtrue&format=pdf&width=1025'
                            FILENAME = f'CIE_Timeseries_{impact}_{country}_{season}_{spatial_aggregation}'
                            DownloadPDFfromURLtoPATH(URL, SAVEPATH, FILENAME)


