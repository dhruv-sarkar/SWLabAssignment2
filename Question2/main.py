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
        print(obj["file_name"])
        for caption in obj["captions"]:
            print(caption)
        

    #Download images to ./data/imgs/ folder using download object
    for i in range(length):
        obj = dataset.__getann__(i)
        #path = f'{outputs}{obj["file_name"]}'
        path = outputs + obj["file_name"]
        download(path,obj["url"])

    #Transform the required image (roll number mod 10) and save it seperately

    image = Image.open(outputs+ '3.jpg')
    img_list = dataset.__transformitem__(image)
    for i,img in enumerate(img_list):
        number = i+1
        path = 'data/transformed_imgs/' + str(number) + '.jpg'
        img.save(path)
    #Get the predictions from the captioner for the above saved transformed image
    print("The captions for the transformed images are")
    for i,img in enumerate(img_list):  
        number = i+1
        path = 'data/transformed_imgs/' + str(number) + '.jpg'
        print(f"The caption for transformed image {number} is ")
        print(captioner(path,3))

def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [RotateImage(0),FlipImage(),RescaleImage(2),RescaleImage(0.5), BlurImage(1),RotateImage(90),RotateImage(45)], './data/imgs/') # Sample arguments to call experiment()


if __name__ == '__main__':
    main()
