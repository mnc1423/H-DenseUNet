from medpy.io import load, save
import numpy as np
import nibabel as nib
import argparse

parser = argparse.ArgumentParser(description="Merge Mask with results file")
parser.add_argument('-mask_data', type=str, default='data/mask/')
parser.add_argument('-results_data', type=str, default='data/results/')
parser.add_argument('-save_path', type=str, default='data/merged_results/')
args = parser.parse_args()

for idx in range(205):
    seg = nib.load(args.results_data + 'test-segmentation-' + str(idx) + '.nii').get_data()
    print("loading segmenation: " + str(idx))
    mask = nib.load(args.mask_data + 'segmentation-' + str(idx) + '.nii').get_data()
    print("Loading mask: " + str(idx))

    mask_shape_array = np.zeros(mask.shape)
    print("mask shape: " + str(mask_shape_array.shape))

    seg_shape_array = np.zeros(mask.shape)
    print('results shape: ' + str(seg_shape_array.shape))

    seg_cords = np.where(seg==1)
    seg_shape_array[seg_cords] = 1

    mask_cords = np.where(mask==2)
    mask_shape_array[mask_cords] = 2


    merged_cords = np.logical_and(mask_shape_array,seg_shape_array)

    seg[merged_cords] = 2

    save(seg, args.save_path + 'merged_results-' + str(idx) + '.nii')

