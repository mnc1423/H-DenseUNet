# converts segmentation files to one value
import nibabel as nib
import os
from medpy.io import load, save
import numpy as np

save_path='/datassd/mjcho/convertedKitsData/'


for idx in range(205):
    seg, seg_header  = load('data/TrainingData/'+ 'segmentation-' + str(idx) + '
.nii')
    print('Loading Segmentation-' + str(idx))
    seg[seg==2]=1
    save(seg, save_path + 'image' + str(idx) + '.nii')
