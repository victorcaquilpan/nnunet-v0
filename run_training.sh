#!/bin/bash

# ==============================
# nnU-Net training wrapper script
# ==============================

# Environment variables
export CUDA_VISIBLE_DEVICES=0
export nnUNet_raw="/data/nnunet-environment/nnUNet_raw/"
export nnUNet_preprocessed="/data/nnunet-environment/nnUNet_preprocessed/"
export nnUNet_results="/data/nnunet-environment/nnUNet_results/"

# (Optional) show envs for debugging
echo "CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"
echo "nnUNet_raw=$nnUNet_raw"
echo "nnUNet_preprocessed=$nnUNet_preprocessed"
echo "nnUNet_results=$nnUNet_results"

#1) Preprocessing
# python -m nnunetv2.experiment_planning.plan_and_preprocess_entrypoints \
# -d 2 \
#  --verify_dataset_integrity

#2) Training
python -m nnunetv2.run.run_training \
    2 \
    3d_fullres \
    all \
    --npz

# 3) Inference
# python -m nnunetv2.inference.predict_from_raw_data \
#     -d \
#     2 \
#     -c \
#     3d_fullres \
#     -f \
#     all \
#     -i \
#     imagesTs \
#     -o \
#     'exp20images1000epochs' \
#     -chk \
#      checkpoint_best.pth

# Making the evaluation
# python -m nnunetv2.evaluation.evaluate_predictions 

