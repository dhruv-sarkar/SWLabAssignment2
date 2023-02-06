#Imports
from PIL import Image
from random import randrange

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape = shape
        self.crop_type = crop_type
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        x,y = image.size
        h,w = self.shape
        if(self.crop_type == 'random'):
            x1 = randrange(0, x - h)
            y1 = randrange(0, y - w)
        elif(self.crop_type == 'center'):
            x1 = x/2 -h/2
            y1 = y/2 - w/2
        image = image.crop((x1, y1, x1 + h, y1 + w))
 