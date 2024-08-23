import os
import shutil
import random
import json

# Set the seed for reproducibility
random.seed(123)

BRATS_TRAIN_DIRECTORY = '../../data/ped-brats2023/train/'
BRATS_VAL_DIRECTORY = '../../data/ped-brats2023/test/'
NNUNET_DIRECTORY = '../../data/nnunet-environment/nnUNet_raw/Dataset001_BrainTumourBrats2023/'

# Reading training data
main_train_folders = os.listdir(BRATS_TRAIN_DIRECTORY)
test_folders = os.listdir(BRATS_VAL_DIRECTORY)

# We are splitting the train set into train and validation

# Shuffle the list
random.shuffle(main_train_folders)

# Determine the split index
split_index = int(len(main_train_folders) * 0.8)

# Split the list
train_folders = main_train_folders[:split_index]
val_folders = main_train_folders[split_index:]

# Creating train and val folder if they dont exist
if os.path.exists(f"{NNUNET_DIRECTORY}"):
    shutil.rmtree(f"{NNUNET_DIRECTORY}")
os.makedirs(f"{NNUNET_DIRECTORY}")
os.makedirs(f"{NNUNET_DIRECTORY}imagesTr/")
os.makedirs(f"{NNUNET_DIRECTORY}labelsTr/")
os.makedirs(f"{NNUNET_DIRECTORY}imagesTs/")
os.makedirs(f"{NNUNET_DIRECTORY}labelsTs/")

# Sort train images
for train_folder in train_folders:
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
for val_folder in val_folders:
    # Get the images
    val_modalities = os.listdir(BRATS_TRAIN_DIRECTORY + val_folder)
    # Get different modalities
    for modality in val_modalities:
        if 't2f' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + val_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTs/' + val_folder + '_0000.nii.gz')
        elif 't2w' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + val_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTs/' + val_folder + '_0001.nii.gz')
        elif 't1c' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + val_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTs/' + val_folder + '_0002.nii.gz')
        elif 't1n' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + val_folder + '/' + modality,NNUNET_DIRECTORY + 'imagesTs/' + val_folder + '_0003.nii.gz')
        elif 'seg' in modality:
            shutil.copyfile(BRATS_TRAIN_DIRECTORY + val_folder + '/' + modality,NNUNET_DIRECTORY + 'labelsTs/' + val_folder + '.nii.gz')


# Create json file

dataset_json ={
    "channel_names": {
    "0": "T2F",
    "1": "T2W",
    "2": "T1C",
    "3": "T1N"
    },
    "labels": {
    "background": 0,
    "NC": 1,
    "ED": 2,
    "ET": 3
    },
    "numTraining": len(train_folders),
    "file_ending": ".nii.gz",
    "overwrite_image_reader_writer": "NibabelIO"
    }
    
with open(f"{NNUNET_DIRECTORY}dataset.json", 'w') as json_file:
        json.dump(dataset_json, json_file, indent=4)


        
    






