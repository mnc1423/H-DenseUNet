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

    filelist = os.listdir('converted/')
    filelist = [item for item in filelist if 'volume' in item]
    for file in filelist:
        img = nib.load('converted/'+ file).get_data()
        print(img.shape)
        img = np.array(img, dtype='float32')
        print(file +' shape: ' + str(img.shape))

convert(args)

