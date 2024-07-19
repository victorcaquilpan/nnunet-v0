import os
import shutil

BRATS_TRAIN_DIRECTORY = '../../data/brats2023/train/'
BRATS_TEST_DIRECTORY = '../../data/brats2023/val/'
NNUNET_DIRECTORY = '../../data/nnunet-environment/nnUNet_raw/Dataset001_BrainTumourBrats2023/'

# Reading training data
train_folders = os.listdir(BRATS_TRAIN_DIRECTORY)
test_folders = os.listdir(BRATS_TEST_DIRECTORY)

# Sort train images
for idx, train_folder in enumerate(train_folders):
    # Get the images
    train_modalities = os.listdir(BRATS_TRAIN_DIRECTORY + train_folder)
    # Get different modalities
    for modality in train_modalities:
        if 't2f' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + train_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTr/' + train_folder + '_0000.nii.gz')
        elif 't2w' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + train_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTr/' + train_folder + '_0001.nii.gz')
        elif 't1c' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + train_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTr/' + train_folder + '_0002.nii.gz')
        elif 't1n' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + train_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTr/' + train_folder + '_0003.nii.gz')
        elif 'seg' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + train_folder + '/' + modality,NNUNET_DIRECTORY + 'labelsTr/' + train_folder + '.nii.gz')

# Sorting test images
# Sort train images
for idx, test_folder in enumerate(test_folders):
    # Get the images
    test_modalities = os.listdir(BRATS_TEST_DIRECTORY + test_folder)
    # Get different modalities
    for modality in test_modalities:
        if 't2f' in modality:
            shutil.copyfile(BRATS_TEST_DIRECTORY + test_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTs/' + test_folder + '_0000.nii.gz')
        elif 't2w' in modality:
            shutil.copyfile(BRATS_TEST_DIRECTORY + test_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTs/' + test_folder + '_0001.nii.gz')
        elif 't1c' in modality:
            shutil.copyfile(BRATS_TEST_DIRECTORY + test_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTs/' + test_folder + '_0002.nii.gz')
        elif 't1n' in modality:
            shutil.copyfile(BRATS_TEST_DIRECTORY + test_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTs/' + test_folder + '_0003.nii.gz')




        
    






