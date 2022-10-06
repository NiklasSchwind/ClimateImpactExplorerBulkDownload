# Climate Impact Explorer - Bulk Download Scripts
Some scripts to help with downloading data in bulk from the CIE API 

How to use: 
1. Have a look at Example.py to see a working bulk download script 
2. Fill in the script BulkDownloadMaps.py or BulkDownloadTimeseries.py with the parameter names (e.g. Countries and Impacts) of the data you want to download and run the script 

Helpful ressources to help with filling in the parameters: 
- All parameter names used in the Climate Impact Explorer can be found in the Metadata.py script 
- The format and meaning of parameter names is described in the Data Download page of the CIE -> https://climate-impact-explorer.climateanalytics.org/data-download/
- All metadata of the Climate Impact Explorer can be found on the metadata site of the Climate Impact Explorer API -> https://cie-api.climateanalytics.org/api/meta/ and countryspecific metadata (including the shapefile and available provinces) can be found with the help of the ISO-Alpha-3 code of each country -> https://cie-api.climateanalytics.org/api/geo-shapes/?iso=ISO_of_requested_Country
