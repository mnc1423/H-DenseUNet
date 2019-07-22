import nibabel as nib
import os
import os.path
import numpy as np
from medpy.io import load, save
import argparse
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description='Convert .nii image to (512,512,z)')
parser.add_argument('-data', type=str, default='data/', help='test image')
parser.add_argument('-save_path', type=str, default='converted/')
parser.add_argument('-input',type=int, default=1)
args = parser.parse_args()
def convert(args):

    filelist = os.listdir('image/segmentation/')
    filelist = [item for item in filelist if 'segmentation' in item]
    for file in filelist:
        img = nib.load('image/segmentation/'+ file).get_data()
        print(img.shape)
        
        img = np.swapaxes(img, 0, 2)
        img = np.array(img, dtype='float32')
        print(img.shape)
        #data_reshape = np.array(data_reshape, dtype='float32')
        print("Save image " + file)
        save(img, args.save_path + file)


convert(args)

