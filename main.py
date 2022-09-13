import os
import zipfile
from flask import Flask, render_template, request
from zipfile import ZipFile
import geopandas as gpd
import matplotlib.pyplot as plt

# Initial app
app = Flask(__name__)


# Routes
# First for upload page where user will load archive
@app.route('/')
def upload_file():
    return render_template('upload.html')


# Second the main work: unzip, find needed file .shp and work with them
# once user load a file script checks if it zip file and then go ahead
@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        fn = f.filename
        if zipfile.is_zipfile(fn):
            f.save(f.filename)
            print(f'file {fn} uploaded successfully')

# unzipping files to directory "unzipped_files"
            with ZipFile(fn, 'r') as zip:
                zip.printdir()
                print('Extracting all files now...')
                zip.extractall(path='unzipped_files')
                print("Done!")

# finding the needed_file with .shp format
            dir_path = 'unzipped_files'
            res = os.listdir(dir_path)
            print(res)
            for i in res:
                if i[-3:] == 'shp':
                    needed_file = i
            print(needed_file)

# open needed_file with geopandas library
            ROOT_DIR = os.path.abspath(os.curdir)
            aoi = gpd.read_file(ROOT_DIR + '/' + dir_path + '/' + needed_file)
            print(aoi.shape)
            print(aoi.head)
            aoi.plot()
            plt.show()
            return 'All processing done correctly'

        else:
            return 'Please load only zip archives'
# unfortunately here my knowledge is end... Need to learn in details the work with fonts and shapes.


if __name__ == '__main__':
    app.run(debug=True)
