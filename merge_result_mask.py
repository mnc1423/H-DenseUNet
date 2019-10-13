from medpy.io import load, save
import numpy as np
import nibabel as nib
import argparse

parser = argparse.ArgumentParser(description="Merge Mask with results file")
parser.add_argument('-mask_data', type=str, default='data/mask/')
parser.add_argument('-results_data', type=str, default='data/results/')
parser.add_argument('-save_path', type=str, default='data/merged_results/')
parser.add_argument('-label_data', type=str, default='data/segmentation/')
args = parser.parse_args()

def dice(result_array, label_array, empty_score=1.0):

    result_array = np.asarray(result_array).astype(np.bool)
    label_array = np.asarray(label_array).astype(np.bool)

    if result_array.shape != label_array.shape:
        raise ValueError("Shape mismatch! Results shape: " + result_array.shape + " Label shape: " + label_CT.shape)

    sum = result_array.sum() + label_array.sum()
    if sum == 0:
        return empty_score

    # Compute Dice coefficient
    intersection = np.logical_and(result_array, label_array)

    return 2. * intersection.sum() / (result_array.sum() + label_array.sum())


for idx in range(1):
    seg = nib.load(args.results_data + 'test-segmentation-' + str(idx) + '.nii').get_data()
    print("loading results: " + str(idx))
    mask = nib.load(args.mask_data + 'segmentation-' + str(idx) + '.nii').get_data()
    print("Loading mask: " + str(idx))

    mask_shape_array = np.zeros(mask.shape)
    print("mask shape: " + str(mask_shape_array.shape))

    seg_shape_array = np.zeros(mask.shape)
    print('results shape: ' + str(seg_shape_array.shape))

    seg_cords = np.where(seg==2)
    seg_shape_array[seg_cords] = 2

    mask_cords = np.where(mask==1)
    mask_shape_array[mask_cords] = 1


    merged_cords = np.logical_and(mask_shape_array,seg_shape_array)

    mask[merged_cords] = 2
    print('Saving Merged Results')
    save(mask, args.save_path + 'merged_results-' + str(idx) + '.nii')

    print('Loading segmentation file: ' + str(idx))
    label = nib.load(args.label_data + 'segmentation-' + str(idx) + '.nii').get_data()
    
    result_tumor = np.where(mask==2)
    label_tumor = np.where(label==2)

    tumor_dice = dice(result_tumor,label_tumor)

    results_kidney = np.where(mask==1) and np.where(mask==2)
    label_kidney = np.where(label==1) and np.where(label==2)

    kidney_dice = dice(results_kidney, label_kidney)

    print("Tumor Dice score: " + str(tumor_dice) + 'Kidney Dice score: ' + str(kidney_dice))
