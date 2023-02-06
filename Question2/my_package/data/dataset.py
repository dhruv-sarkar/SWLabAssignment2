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
        with jsonlines.open(annotation_file) as annotation:
            self.__annotations__ = [obj for obj in annotation]
        self.transforms = transforms

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.__annotations__)


    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        return self.__annotations__[idx]


    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        
        img_list =[]
        for transform in self.transforms:
             img_list.append(transform(path))
        
        return img_list