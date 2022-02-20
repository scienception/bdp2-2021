import requests

url = 'https://storage.googleapis.com/bucket_bdp/n02088094_1003.jpg' # this is the URL of your S3 file (it must be public)
r = requests.get(url)
open('n02088094_1003.jpg', 'wb').write(r.content) # put a name for the output file here
