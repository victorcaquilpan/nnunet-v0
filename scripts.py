import os
import subprocess

def main():
    # Set environment variables
    os.environ['CUDA_VISIBLE_DEVICES'] = '1'
    os.environ['nnUNet_raw'] = "/data/nnunet-environment/nnUNet_raw/"
    os.environ['nnUNet_preprocessed'] = "/data/nnunet-environment/nnUNet_preprocessed/"
    os.environ['nnUNet_results'] = "/data/nnunet-environment/nnUNet_results/"
    
    # Set the working directory
    workdir = "/workspace/nnunet-v0"
    os.chdir(workdir)
    
    # Add the directory to PYTHONPATH
    pythonpath = os.environ.get('PYTHONPATH', '')
    os.environ['PYTHONPATH'] = f"{workdir}:{pythonpath}"
    
    # Print PYTHONPATH for debugging purposes
    print(f"PYTHONPATH: {os.environ['PYTHONPATH']}")
    
    # Run preprocessing 
    # preprocess_command = [
    #     "python", "./nnunetv2/experiment_planning/plan_and_preprocess_entrypoints.py",
    #     "-d", "1", "--verify_dataset_integrity"
    # ]
    # subprocess.run(preprocess_command, check=True)
    
    # Run training 
    # training_command = [
    #     "python", "./nnunetv2/run/run_training.py",
    #     "1", "3d_fullres", "all", "--npz"
    # ]
    # subprocess.run(training_command, check=True)
    
    # Run inference
    inference_command = [
        "python", "./nnunetv2/inference/predict_from_raw_data.py",
        "-i", "/data/nnunet-environment/nnUNet_preprocessed/Dataset001_BrainTumourBrats2023/nnUNetPlans_3d_fullres/",
        "-o", "/data/nnunet-environment/nnUNet_results/Dataset001_BrainTumourBrats2023/nnUNetTrainer__nnUNetPlans__3d_fullres/predictions/",
        "-m", "data/nnunet-environment/nnUNet_results/Dataset001_BrainTumourBrats2023/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_all/checkpoint_best.pth"
    ]
    subprocess.run(inference_command, check=True)

    # Run best config
    # best_conf_command = [
    #     "python", "./nnunetv2/evaluation/find_best_configuration.py",
    #     "dataset_name_or_id", "1",
    # ]
    # subprocess.run(best_conf_command, check=True)

    # Run evaluation
    eval_conf_command = [
        "python", "./nnunetv2/evaluation/evaluate_predictions.py"]
    subprocess.run(eval_conf_command, check=True)


if __name__ == "__main__":
    main()