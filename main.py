#Imports
from my_package.model import ImageCaptioningModel
from my_package.data import Dataset, Download
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    dataset = Dataset(annotation_file,transforms)
    download = Download()
    #Print image names and their captions from annotation file using dataset object
    length = dataset.__len__()
    for i in range(length):
        obj =  dataset.__getann__(i)
        print(f'{obj["name"]}:')
        for caption in obj["caption"]:
            print(caption)
        print(f'\n')

    #Download images to ./data/imgs/ folder using download object
    for i in range(length):
        obj = dataset.__getann__(i)
        path = f'{outputs}{obj["file_name"]}'
        download.__call__(path,obj["url"])

    #Transform the required image (roll number mod 10) and save it seperately

    image = Image.open(f'{outputs}/3.jpg')
    for transform in transform:
        transform(image)
    #Get the predictions from the captioner for the above saved transformed image
    for image in image:  
        captioner.__call__(image)

def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage(), BlurImage(1)], './data/imgs/') # Sample arguments to call experiment()


if __name__ == '__main__':
    main()
