#!/bin/bash

# Set environment variables
export nnUNet_raw="/data/nnunet-environment/nnUNet_raw/"
export nnUNet_preprocessed="/data/nnunet-environment/nnUNet_preprocessed/"
export nnUNet_results="/data/nnunet-environment/nnUNet_results/"

WORKDIR="/workspace/nnUNet"
# Change to the working directory
cd "$WORKDIR" || { echo "Failed to change directory to $WORKDIR"; exit 1; }

# Add the directory to PYTHONPATH
export PYTHONPATH="$WORKDIR:$PYTHONPATH"

# Print PYTHONPATH for debugging purposes
echo "PYTHONPATH: $PYTHONPATH"


# Run preprocessing
# python ./nnunetv2/experiment_planning/plan_and_preprocess_entrypoints.py -d 1 --verify_dataset_integrity
# Run training
python ./nnunetv2/run/run_training.py dataset_name_or_id  1 fold 0 configuration 2d