#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output_size = output_size


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        if isinstance(self.output_size, tuple):
            image = image.resize(self.output_size)

        else: 
            x,y = image.shape
            if(x>=y):
                image = image.resize([x*self.output_size/y,self.output_size])

            else:
                image = image.resize([self.output_size,y*self.output_size/x])
        
        return image