import nibabel as nib
import os
import os.path
import numpy as np
from medpy.io import load, save
import argparse
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description='Convert .nii image to (512,512,z)')
parser.add_argument('-data_vol', type=str, default='data/TrainingData/', help='test image')
parser.add_argument('-save_path', type=str, default='seg_converted/')
parser.add_argument('-data_seg', type=str, default='data/TrainingData/')
args = parser.parse_args()



def convert(args):

    for idx in range(205):
        seg = nib.load(args.data_seg + 'image' + str(idx) + '.nii').get_data()
        seg_original = nib.load('data/TrainingData/' + 'segmentation-' + str(idx) + '.nii').get_data()

        index = np.where(seg==1)
        mini = np.min(index, axis = -1)
        maxi = np.max(index, axis = -1)
        #Add buffer to each end of CT 
        data_reshape_seg_original = seg_original[:,:,mini[2]-1:maxi[2]+1]
        print("Saving seg...... shape: " + str(data_reshape_seg_original.shape))
        save(data_reshape_seg_original, args.save_path + "segmentation/segmentation-" + str(idx) + ".nii")

convert(args)
