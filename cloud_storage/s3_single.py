import requests

url = 'https://storage.googleapis.com/bucket_bdp/test/1.jpeg' # this is the URL of your S3 file (it must be public)
r = requests.get(url)
open('1.jpeg', 'wb').write(r.content) # put a name for the output file here
