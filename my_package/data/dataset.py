#Imports
import jsonlines
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''
#by dataitems we mean the filename and the correspoding captions
    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file = annotation_file
        self.transforms = transforms

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        fd = os.open(self.annotation_file,'r')
        lines = len(fd.readlines())
        return lines


    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        id = 0 
        reader = jsonlines.open(self.annotation_file)
        obj = reader[idx]
        return obj


    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        img = Image.open(path)
        for transform in self.transform:
            return transform.__call__(img)