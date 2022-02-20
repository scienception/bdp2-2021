import requests
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
import os.path

url = "https://storage.googleapis.com/bucket_bdp/" #URL of public S3 file
IMAGE_DIR = "/bucket_data"
OUT_DIR = "/home/enigma/bdp2-2021/cloud_storage/download_from_s3/"

def convert(filename):
    # convert an image to its BW equivalent
    # it creates a pdf with the original name + "_bw"
    name, ext = os.path.splitext(filename)
    read_name = os.path.basename(filename)
    write_name = name + "_bw.pdf"

    if ext.lower() != '.jpg':
        print("Skipping file %s (not a jpg)" % read_name)
        return
    else:
        print("Processing file " + read_name)

    r = requests.get(url+read_name)
    open(OUT_DIR+read_name, 'wb').write(r.content) 
    original = io.imread(OUT_DIR+read_name)
    grayscale = rgb2gray(original)
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()

    ax[0].imshow(original)
    ax[0].set_title('Original')
    ax[1].imshow(grayscale, cmap=plt.cm.gray)
    ax[1].set_title('Grayscale')

    fig.tight_layout()
    plt.savefig(write_name)
    plt.cla()
    plt.close()


start = time.time()

for root, dirs, files in os.walk(IMAGE_DIR):
    for name in files:
        convert(os.path.join(root, name))

end = time.time()

print(end-start)


    
