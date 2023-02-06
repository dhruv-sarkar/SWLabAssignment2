from PIL import Image
import requests
from io import BytesIO
import urllib
import jsonlines
class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''

    def __call__(self, path, url):
        '''
            Arguments:
            path: download path with the file name
            url: required image URL
        '''
        req = requests.get(url, stream=True)
        if req.status_code == 200:
            img = Image.open(BytesIO(req.content))
            img.save(path,'JPEG')
