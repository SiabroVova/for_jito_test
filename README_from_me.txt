Simple web-app to load zip archives with shapefiles .shp to analyzing and finding whole streets.

For loading archives was used simple flask server with html template.

Then we are checking the archive is it truly zip and if yes - go forward.

After unpacking archive we have gone through all files and found one which has .shp format.

Then we read the needed file with geopandas and show it.