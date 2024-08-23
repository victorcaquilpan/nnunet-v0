import nibabel as nib
import numpy as np
from scipy.spatial.distance import dice
import argparse

# Defining main functions 
def read_nii_file(filepath):
    """Read a .nii.gz file and return the image data as a numpy array."""
    nii = nib.load(filepath)
    return nii.get_fdata()

def compute_dice_score(segmentation1, segmentation2):
    """Compute the Dice score between two binary segmentation masks."""
    segmentation1 = np.asarray(segmentation1).astype(bool)
    segmentation2 = np.asarray(segmentation2).astype(bool)
    
    if segmentation1.shape != segmentation2.shape:
        raise ValueError("Shape mismatch: segmentation masks must have the same shape.")
    
    intersection = np.sum(segmentation1 & segmentation2)
    volume_sum = np.sum(segmentation1) + np.sum(segmentation2)
    
    if volume_sum == 0:
        return 1.0  # If both segmentations are empty, return Dice score of 1.0
    
    return 2. * intersection / volume_sum

if __name__ == "__main__":

    # Call the parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--results_folder', default='testing', help='path to results')
    args = parser.parse_args()

    
